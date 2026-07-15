# INSTALL

## Requirements

- Python 3.10+
- Git
- GitHub Codespaces หรือ Linux/macOS/Windows

---

## Clone

```bash
git clone <repository-url>
cd softwarehub-cms-v2
```

---

## Install

```bash
pip install -r requirements.txt
```

หากไม่มี `requirements.txt`

ติดตั้งเอง

```bash
pip install jinja2
```

---

## Build

```bash
python3 scripts/build.py
```

---

## Output

หลัง Build

เว็บไซต์จะถูกสร้างใน

```text
site/
```

---

## Development

แก้ไขไฟล์ใน

- config/
- content/
- scripts/
- templates/
- static/

ห้ามแก้ไข

```text
site/
```

โดยตรง

---

## Documentation

เริ่มอ่าน

```text
docs/AI_HANDOVER.md
```

ก่อนทำงาน