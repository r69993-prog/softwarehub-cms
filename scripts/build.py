import json
import math
import shutil
from pathlib import Path


import sys

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))



from xml.etree.ElementTree import Element, SubElement, ElementTree

from jinja2 import Environment, FileSystemLoader

from content import load_software


from builder.pages import build_home_pages
from builder.categories import build_categories
from builder.articles import build_articles
from builder.rss import build_rss
from builder.sitemap import build_sitemap
from builder.robots import build_robots
from builder.assets import copy_assets



BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG_FILE = BASE_DIR / "config" / "site.json"
SOFTWARE_FILE = BASE_DIR / "content" / "software.csv"

TEMPLATE_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"
SITE_DIR = BASE_DIR / "site"

SITE_DIR.mkdir(exist_ok=True)

site = json.loads(
    CONFIG_FILE.read_text(encoding="utf-8")
)

software = load_software(SOFTWARE_FILE)

categories = sorted({
    item["category"]
    for item in software
})

env = Environment(
    loader=FileSystemLoader(TEMPLATE_DIR),
    autoescape=True
)

home_template = env.get_template("home.html")
article_template = env.get_template("article.html")
category_template = env.get_template("category.html")
notfound_template = env.get_template("404.html")
privacy_template = env.get_template("privacy.html")
terms_template = env.get_template("terms.html")
disclaimer_template = env.get_template("disclaimer.html")
contact_template = env.get_template("contact.html")

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

    html = home_template.render(
        title=site["seo"]["title"],
        site=site,
        software=items,
        page=page,
        total_pages=total_pages
    )

    (SITE_DIR / filename).write_text(
        html,
        encoding="utf-8"
    )

    urls.append(filename)

for category in categories:

    slug = category.lower().replace(" ", "")

    items = [
        s for s in software
        if s["category"] == category
    ]

    html = category_template.render(
        title=category,
        site=site,
        category=category,
        software=items
    )

    (SITE_DIR / f"{slug}.html").write_text(
        html,
        encoding="utf-8"
    )

    urls.append(f"{slug}.html")

for item in software:

    slug = (
        item["name"]
        .lower()
        .replace(" ", "")
        .replace("+", "plus")
        .replace("-", "")
    )

    related = [
        s for s in software
        if s["name"] != item["name"]
    ][:3]

    html = article_template.render(
        title=item["name"],
        site=site,
        software=item,
        related=related
    )

    (SITE_DIR / f"{slug}.html").write_text(
        html,
        encoding="utf-8"
    )

    urls.append(f"{slug}.html")

(SITE_DIR / "404.html").write_text(
    notfound_template.render(title="404", site=site),
    encoding="utf-8"
)

(SITE_DIR / "privacy.html").write_text(
    privacy_template.render(title="Privacy Policy", site=site),
    encoding="utf-8"
)

(SITE_DIR / "terms.html").write_text(
    terms_template.render(title="Terms of Use", site=site),
    encoding="utf-8"
)

(SITE_DIR / "disclaimer.html").write_text(
    disclaimer_template.render(title="Disclaimer", site=site),
    encoding="utf-8"
)

(SITE_DIR / "contact.html").write_text(
    contact_template.render(title="Contact Us", site=site),
    encoding="utf-8"
)


rss = Element("rss")
rss.set("version", "2.0")

channel = SubElement(rss, "channel")

SubElement(channel, "title").text = site["site"]["name"]
SubElement(channel, "link").text = site["site"]["url"]
SubElement(channel, "description").text = site["seo"]["description"]

for item in software:

    slug = (
        item["name"]
        .lower()
        .replace(" ", "")
        .replace("+", "plus")
        .replace("-", "")
    )

    post = SubElement(channel, "item")

    SubElement(post, "title").text = item["name"]
    SubElement(post, "link").text = (
        site["site"]["url"].rstrip("/")
        + "/"
        + slug
        + ".html"
    )
    SubElement(post, "description").text = item["description"]

ElementTree(rss).write(
    SITE_DIR / "feed.xml",
    encoding="utf-8",
    xml_declaration=True
)

root = Element("urlset")
root.set(
    "xmlns",
    "http://www.sitemaps.org/schemas/sitemap/0.9"
)

for url in urls:

    node = SubElement(root, "url")

    SubElement(node, "loc").text = (
        site["site"]["url"].rstrip("/")
        + "/"
        + url
    )

ElementTree(root).write(
    SITE_DIR / "sitemap.xml",
    encoding="utf-8",
    xml_declaration=True
)

(SITE_DIR / "robots.txt").write_text(
    f"""User-agent: *
Allow: /

Sitemap: {site["site"]["url"].rstrip("/")}/sitemap.xml
""",
    encoding="utf-8"
)

if (STATIC_DIR / "images").exists():
    shutil.copytree(
        STATIC_DIR / "images",
        SITE_DIR / "images",
        dirs_exist_ok=True
    )

if (STATIC_DIR / "css" / "style.css").exists():
    shutil.copy(
        STATIC_DIR / "css" / "style.css",
        SITE_DIR / "style.css"
    )

print("=" * 40)
print("SoftwareHub CMS Pro v3")
print("=" * 40)
print(f"Pages Built : {len(urls) + 5}")
print("Build Success")

