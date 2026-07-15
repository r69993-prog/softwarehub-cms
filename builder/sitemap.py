from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, ElementTree


def build_sitemap(site: dict, urls: list[str], site_dir: Path) -> None:
    """
    Generate sitemap.xml
    """

    root = Element("urlset")
    root.set(
        "xmlns",
        "http://www.sitemaps.org/schemas/sitemap/0.9"
    )

    base_url = site["site"]["url"].rstrip("/")

    for url in urls:
        node = SubElement(root, "url")
        SubElement(node, "loc").text = f"{base_url}/{url}"

    ElementTree(root).write(
        site_dir / "sitemap.xml",
        encoding="utf-8",
        xml_declaration=True
    )