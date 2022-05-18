import typer
from ssg import site


def main(source="content", dest="dist"):
    config = {
            "source": source,
            "dest": dest
            }

    new_site = site.Site(**config).build()


typer.run(main)
