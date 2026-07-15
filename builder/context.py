import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from content import load_software


class BuildContext:

    def __init__(self, base_dir: Path):

        self.base_dir = base_dir

        self.config_file = base_dir / "config" / "site.json"
        self.software_file = base_dir / "content" / "software.csv"

        self.template_dir = base_dir / "templates"
        self.static_dir = base_dir / "static"
        self.site_dir = base_dir / "site"

        self.site_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.site = json.loads(
            self.config_file.read_text(
                encoding="utf-8"
            )
        )

        self.software = load_software(
            self.software_file
        )

        self.env = Environment(
            loader=FileSystemLoader(
                self.template_dir
            ),
            autoescape=True
        )

    def template(self, name: str):
        return self.env.get_template(name)