try:
    import click
except ImportError:
    click = None
import json
from typing import List, Callable
from functools import partial

from .api_client import APIClient
from .exceptions import APIClientException

method_names = ["get", "retrieve", "list", "create", "update", "delete"]
param_options = [
    click.Option(
        ("--fields", "fields"),
        required=False,
        type=click.STRING,
    ),
    click.Option(
        ("--omit", "omit"),
        required=False,
        type=click.STRING,
    ),
    click.Option(
        ("--expand", "expand"),
        required=False,
        type=click.STRING,
    ),
    click.Option(
        ("--ordering", "ordering"),
        required=False,
        type=click.STRING,
    ),
    click.Option(
        ("--page", "page"),
        required=False,
        type=click.INT,
    ),
    click.Option(
        ("--page_size", "page_size"),
        required=False,
        type=click.INT,
    ),
]

if click:

    @click.pass_context
    def cmd_callback(
        ctx: click.Context,
        apiresource_method: Callable,
        object_id: str = None,
        json_data: str = None,
        **kwargs,
    ):
        try:
            params = kwargs  # FIXME: needs proper parsing
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
            ctx.obj._logger.info(resp.data)
        except APIClientException as exc:
            ctx.obj._logger.error(str(exc))

    def make_groups_for_api_resources(api_client_class: APIClient) -> List[click.Group]:
        groups = []
        resources_map = api_client_class._get_resources_map()
        # one group for each APIResource class
        for attrkey, klass in resources_map.items():
            grp_name = attrkey.lower()
            grp_commands = []
            # make commands
            for method_name in method_names:
                method_fn = getattr(klass, method_name, None)
                if method_fn is not None:
                    params = param_options.copy()
                    if "object_id" in method_fn.__annotations__:
                        params.append(
                            click.Argument(
                                ("object_id",), required=True, type=click.STRING
                            )
                        )
                    if "data" in method_fn.__annotations__:
                        params.append(
                            click.Argument(
                                ("json_data",), required=True, type=click.STRING
                            )
                        )
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
