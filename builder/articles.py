from pathlib import Path

from .utils import slugify, write_text


def build_articles(
    site: dict,
    software: list,
    template,
    site_dir: Path,
) -> list[str]:
    """
    Generate article pages.
    Returns list of generated filenames.
    """

    urls = []

    for item in software:

        filename = f"{slugify(item['name'])}.html"

        related = [
            s for s in software
            if s["name"] != item["name"]
        ][:3]

        html = template.render(
            title=item["name"],
            site=site,
            software=item,
            related=related,
        )

        write_text(site_dir / filename, html)

        urls.append(filename)

    return urls