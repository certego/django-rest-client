#!/usr/bin/env python3
import click
import click_creds

from django_rest_client.cli_maker import make_groups_for_api_resources

from .client import ExampleClient


class ClickContext(click.Context):
    obj: ExampleClient


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
@click_creds.use_netrcstore(
    name="django_rest_client_example",
    mapping={"login": "certificate", "password": "token", "account": "instance_url"},
)
@click.pass_context
def cli(ctx: ClickContext):
    host = click_creds.get_netrc_object_from_ctx(ctx).host.copy()
    token, url = host["password"], host["account"]
    if (not token or not url) and ctx.invoked_subcommand != "config":
        click.echo("Hint: Use `config set` to set config variables!")
        exit()
    else:
        # store instance as ``click.Context.obj```
        ctx.obj = ExampleClient(token=token)
        ctx.obj._server_url = url


# Compile all groups and commands
apiresource_groups = make_groups_for_api_resources(api_client_class=ExampleClient)
for c in [click_creds.config_group, *apiresource_groups]:
    cli.add_command(c)

# Entrypoint/executor
if __name__ == "__main__":
    cli()
