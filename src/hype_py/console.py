import textwrap

import click
import requests

from . import __version__


# API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
API_URL = 'https://en.wikipedia.org/api/rest_v1/page/summary/'


@click.command()
@click.option('--query', prompt=True)
@click.version_option(version=__version__)
def main(query):
    # click.echo(f'Hello {name}!')
    """The hypermodern Python project."""
    try:
      with requests.get(f'{API_URL}{query}') as response:
          response.raise_for_status()
          data = response.json()

      title = data["title"]
      extract = data["extract"]

      click.secho(title, fg="green")
      click.echo(textwrap.fill(extract))
    except:
      click.echo("Something went wrong")