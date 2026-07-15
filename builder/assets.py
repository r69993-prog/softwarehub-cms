import shutil
from pathlib import Path


def copy_assets(static_dir: Path, site_dir: Path) -> None:
    """
    Copy static assets (CSS, JS, Images) to output directory.
    """

    images = static_dir / "images"
    css = static_dir / "css" / "style.css"
    js = static_dir / "js"

    if images.exists():
        shutil.copytree(
            images,
            site_dir / "images",
            dirs_exist_ok=True
        )

    if css.exists():
        shutil.copy(
            css,
            site_dir / "style.css"
        )

    if js.exists():
        shutil.copytree(
            js,
            site_dir / "js",
            dirs_exist_ok=True
        )