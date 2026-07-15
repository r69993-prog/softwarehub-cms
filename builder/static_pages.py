from pathlib import Path

from .utils import write_text


def build_static_pages(
    site: dict,
    templates: dict,
    site_dir: Path,
) -> int:
    """
    Generate static pages.
    Returns number of generated pages.
    """

    pages = {
        "404.html": (
            templates["404"],
            "404",
        ),
        "privacy.html": (
            templates["privacy"],
            "Privacy Policy",
        ),
        "terms.html": (
            templates["terms"],
            "Terms of Use",
        ),
        "disclaimer.html": (
            templates["disclaimer"],
            "Disclaimer",
        ),
        "contact.html": (
            templates["contact"],
            "Contact Us",
        ),
    }

    count = 0

    for filename, (template, title) in pages.items():

        html = template.render(
            title=title,
            site=site,
        )

        write_text(
            site_dir / filename,
            html,
        )

        count += 1

    return count