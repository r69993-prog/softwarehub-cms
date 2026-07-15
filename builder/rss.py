from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, ElementTree

from .utils import slugify


def build_rss(site: dict, software: list, site_dir: Path) -> None:
    """
    Generate RSS feed.
    """

    rss = Element("rss")
    rss.set("version", "2.0")

    channel = SubElement(rss, "channel")

    SubElement(channel, "title").text = site["site"]["name"]
    SubElement(channel, "link").text = site["site"]["url"]
    SubElement(channel, "description").text = site["seo"]["description"]

    for item in software:

        post = SubElement(channel, "item")

        SubElement(post, "title").text = item["name"]

        SubElement(post, "link").text = (
            site["site"]["url"].rstrip("/")
            + "/"
            + slugify(item["name"])
            + ".html"
        )

        SubElement(post, "description").text = item["description"]

    ElementTree(rss).write(
        site_dir / "feed.xml",
        encoding="utf-8",
        xml_declaration=True
    )