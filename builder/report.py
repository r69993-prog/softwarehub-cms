from datetime import datetime
from pathlib import Path


class BuildReport:

    def __init__(self):

        self.start = datetime.now()

        self.home = 0
        self.category = 0
        self.article = 0
        self.static = 0

        self.rss = False
        self.sitemap = False
        self.robots = False
        self.assets = False

    @property
    def total(self):

        return (
            self.home
            + self.category
            + self.article
            + self.static
        )

    def finish(self):

        end = datetime.now()

        return (end - self.start).total_seconds()

    def print(self):

        sec = self.finish()

        print("=" * 45)
        print("SoftwareHub CMS Pro v2.1")
        print("=" * 45)

        print(f"Home Pages     : {self.home}")
        print(f"Category Pages : {self.category}")
        print(f"Article Pages  : {self.article}")
        print(f"Static Pages   : {self.static}")

        print()

        print(f"RSS            : {'OK' if self.rss else '-'}")
        print(f"Sitemap        : {'OK' if self.sitemap else '-'}")
        print(f"Robots         : {'OK' if self.robots else '-'}")
        print(f"Assets         : {'OK' if self.assets else '-'}")

        print()

        print(f"Total Pages    : {self.total}")

        print(f"Build Time     : {sec:.2f} sec")

        print()

        print("Build Success")

        print("=" * 45)