import csv
from pathlib import Path


def load_software(csv_file: Path):
    """
    อ่านไฟล์ software.csv
    คืนค่าเป็น list ของ dictionary
    """

    items = []

    with csv_file.open(
        encoding="utf-8",
        newline=""
    ) as f:

        reader = csv.DictReader(f)

        for row in reader:

            row["rating"] = float(
                row.get("rating", 0)
            )

            items.append(row)

    return items