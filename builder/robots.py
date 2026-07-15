from pathlib import Path


def build_robots(site: dict, site_dir: Path) -> None:
    """
    Generate robots.txt
    """

    robots = f"""User-agent: *
Allow: /

Sitemap: {site["site"]["url"].rstrip("/")}/sitemap.xml
"""

    (site_dir / "robots.txt").write_text(
        robots,
        encoding="utf-8"
    )