import math
from pathlib import Path

from .utils import write_text


def build_home_pages(
    site: dict,
    software: list,
    template,
    site_dir: Path,
) -> list[str]:
    """
    Generate paginated home pages.
    Returns list of generated filenames.
    """

    per_page = site["build"]["items_per_page"]
    total_pages = math.ceil(len(software) / per_page)

    urls = []

    for page in range(1, total_pages + 1):

        start = (page - 1) * per_page
        end = start + per_page

        items = software[start:end]

        filename = (
            "index.html"
            if page == 1
            else f"page{page}.html"
        )

        html = template.render(
            title=site["seo"]["title"],
            site=site,
            software=items,
            page=page,
            total_pages=total_pages,
        )

        write_text(site_dir / filename, html)

        urls.append(filename)

    return urls