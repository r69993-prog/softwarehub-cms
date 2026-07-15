from pathlib import Path

from .utils import category_slug, write_text


def build_categories(
    site: dict,
    software: list,
    template,
    site_dir: Path,
) -> list[str]:
    """
    Generate category pages.
    Returns list of generated filenames.
    """

    urls = []

    categories = sorted({
        item["category"]
        for item in software
    })

    for category in categories:

        items = [
            s for s in software
            if s["category"] == category
        ]

        filename = f"{category_slug(category)}.html"

        html = template.render(
            title=category,
            site=site,
            category=category,
            software=items,
        )

        write_text(site_dir / filename, html)

        urls.append(filename)

    return urls