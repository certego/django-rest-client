try:
    import click
except ImportError:
    click = None
import json
from typing import List, Callable
from functools import partial

from .api_client import APIClient
from .exceptions import APIClientException
from .types import TParams


__all__ = [
    "make_groups_for_api_resources",
]


__method_names = ["get", "retrieve", "list", "create", "update", "delete"]
__filter_param_options = [
    click.Option(
        ("--fields", "fields"),
        required=False,
        type=click.STRING,
        help="CSV of fields to include",
    ),
    click.Option(
        ("--omit", "omit"),
        required=False,
        type=click.STRING,
        help="CSV of fields to exclude",
    ),
    click.Option(
        ("--expand", "expand"),
        required=False,
        type=click.STRING,
        help="CSV of fields to expand",
    ),
]
__list_param_options = [
    click.Option(
        ("--ordering", "ordering"),
        required=False,
        type=click.STRING,
        help="CSV of fields with +,- prefix to perform ordering on",
    ),
    click.Option(
        ("--page", "page"),
        required=False,
        type=click.INT,
        help="Page number",
    ),
    click.Option(
        ("--page_size", "page_size"),
        required=False,
        type=click.INT,
        help="Number of entries in each page",
    ),
]
__retrieve_param_options = [
    click.Argument(
        ("object_id",),
        required=True,
        type=click.STRING,
    ),
]
__mutable_param_options = [
    click.Argument(
        ("json_data",),
        required=True,
        type=click.STRING,
    )
]


def __parse_kwargs_into_params(pargs: dict) -> TParams:
    params = TParams()
    for key, value in pargs.items():
        if value is not None and value != "":
            if key in ["fields", "omit", "expand", "ordering"]:
                params[key] = value.split(",")
            else:
                params[key] = value
    return params


if click:

    def cmd_callback(
        apiresource_method: Callable,
        object_id: str = None,
        json_data: str = None,
        **kwargs,
    ):
        try:
            params = __parse_kwargs_into_params(kwargs)
            if json_data:
                data = json.loads(json_data)  # FIXME: needs proper parsing
                if object_id:
                    resp = apiresource_method(
                        object_id=object_id, data=data, params=params
                    )
                else:
                    resp = apiresource_method(data=data, params=params)
            else:
                if object_id:
                    resp = apiresource_method(object_id=object_id, params=params)
                else:
                    resp = apiresource_method(params=params)
            click.echo(resp.data)
        except APIClientException as exc:
            click.echo(str(exc), err=True)

    def make_groups_for_api_resources(api_client_class: APIClient) -> List[click.Group]:
        groups = []
        resources_map = api_client_class._get_resources_map()
        # one group for each APIResource class
        for attrkey, klass in resources_map.items():
            grp_name = attrkey.lower()
            grp_commands = []
            # make commands
            for method_name in __method_names:
                method_fn = getattr(klass, method_name, None)
                if method_fn is not None:
                    params = []
                    if method_fn.__name__ == "retrieve":
                        params.extend(__retrieve_param_options)
                        params.extend(__filter_param_options)
                    elif method_fn.__name__ == "list":
                        params.extend(__list_param_options)
                        params.extend(__filter_param_options)
                    elif method_fn.__name__ == "update":
                        params.extend(__retrieve_param_options)
                        params.extend(__mutable_param_options)
                    elif method_fn.__name__ == "create":
                        params.extend(__mutable_param_options)

                    grp_commands.append(
                        click.Command(
                            name=method_name,
                            help=f"{klass.OBJECT_NAME}.{method_name}",
                            params=params,
                            callback=partial(cmd_callback, method_fn),
                        )
                    )
            groups.append(
                click.Group(
                    name=grp_name,
                    commands=grp_commands,
                    help=f"{klass.__name__} management",
                )
            )

        return groups
