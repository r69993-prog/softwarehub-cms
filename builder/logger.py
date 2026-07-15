from datetime import datetime
from pathlib import Path


class BuildLogger:

    def __init__(self, log_dir: Path):

        self.log_dir = log_dir
        self.log_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.file = (
            self.log_dir /
            "build.log"
        )

    def write(
        self,
        report,
    ):

        now = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        sec = report.finish()

        text = f"""
========================================
{now}

Home Pages     : {report.home}
Category Pages : {report.category}
Article Pages  : {report.article}
Static Pages   : {report.static}

RSS            : {report.rss}
Sitemap        : {report.sitemap}
Robots         : {report.robots}
Assets         : {report.assets}

Total Pages    : {report.total}

Build Time     : {sec:.2f} sec

SUCCESS
========================================

"""

        with open(
            self.file,
            "a",
            encoding="utf-8"
        ) as f:

            f.write(text)