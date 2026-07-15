from pathlib import Path


def slugify(name: str) -> str:
    """Convert software name to URL slug."""
    return (
        name.lower()
        .replace(" ", "")
        .replace("+", "plus")
        .replace("-", "")
    )


def category_slug(category: str) -> str:
    """Convert category name to filename."""
    return category.lower().replace(" ", "")


def ensure_dir(path: Path) -> None:
    """Create directory if it does not exist."""
    path.mkdir(parents=True, exist_ok=True)


def write_text(path: Path, content: str) -> None:
    """Write UTF-8 text file."""
    path.write_text(content, encoding="utf-8")