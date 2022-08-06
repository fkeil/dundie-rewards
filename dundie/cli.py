import pkg_resources
import rich_click as click
from rich.console import Console
from rich.table import Table

from dundie import core

click.rich_click.USE_RICH_MARKUP = True
click.rich_click.USE_MARKDOWN = True
click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True
click.rich_click.SHOW_METAVARS_COLUMN = False
click.rich_click.APPEND_METAVARS_HELP = True


@click.group()
@click.version_option(pkg_resources.get_distribution("dundie").version)
def main():
    """Dunder Mifflin Rewars system.

    This CLI application controls DM rewars.
    """


@main.command()
@click.argument("filepath", type=click.Path(exists=True))
def load(filepath):
    """Loads the file to the database

    ## Features

    - Validates data
    - Parses the dile
    - Loads to database
    """

    table = Table(
        title="Dunder Mifflin Associates", title_style="yellow", highlight=True
    )
    headers = ["Name", "Department", "Role", "e-mail", "Created"]
    for header in headers:
        table.add_column(
            header, header_style="blue", style="magenta", justify="center"
        )

    result = core.load(filepath)
    for person in result:
        table.add_row(*[str(value) for value in person.values()])

    console = Console()
    console.print(table)
