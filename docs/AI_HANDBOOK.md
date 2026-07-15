# SoftwareHub CMS v2
# AI Handbook

Version: 1.0
Status: Active
Repository: https://github.com/r69993-prog/softwarehub-cms

---

# 1. Project Mission

SoftwareHub CMS คือ Static CMS สำหรับสร้างเว็บไซต์แนะนำซอฟต์แวร์ที่มีคุณภาพสูง เน้น

- ความเร็ว
- SEO
- Static Website
- Build ง่าย
- ดูแลรักษาง่าย
- พร้อมขยายเป็น Full CMS ในอนาคต

---

# 2. Long-Term Vision

Roadmap

v2.x

Static CMS

↓

v3.x

Database CMS

↓

v4.x

Plugin + Theme

↓

v5.x

AI Powered CMS

---

# 3. Current Status

Current Version

SoftwareHub CMS v2

Current Release

Development

Build

Working

GitHub

Connected

Codespaces

Connected

---

# 4. Technology Stack

Language

- Python 3

Template Engine

- Jinja2

Frontend

- HTML5
- CSS3

Content

- CSV

Output

- Static HTML

Deployment

- Static Hosting

---

# 5. Folder Structure

builder/
config/
content/
docs/
scripts/
static/
templates/
site/

---

# 6. Builder Responsibilities

pages.py

Build Home

articles.py

Build Articles

categories.py

Build Categories

static_pages.py

Privacy
Terms
Disclaimer
Contact

rss.py

RSS Feed

sitemap.py

Sitemap

robots.py

robots.txt

assets.py

Copy Assets

context.py

Shared Context

logger.py

Build Logger

report.py

Build Report

seo.py

SEO Utilities

utils.py

Shared Utilities

navigation.py

Navigation Builder

---

# 7. Build Pipeline

software.csv

↓

content.py

↓

builder modules

↓

templates

↓

site/

---

# 8. Coding Standard

General Rules

- Function ต้องสั้น
- Module มีหน้าที่เดียว
- ห้ามเขียน Logic ซ้ำ
- ใช้ pathlib
- ห้าม Hardcode Path
- ใช้ UTF-8

Naming

snake_case

Classes

PascalCase

Constants

UPPER_CASE

---

# 9. Build Rules

ทุกครั้งก่อน Commit

ต้อง Build ผ่าน

คำสั่ง

python scripts/build.py

Build ต้อง

- ไม่มี Error
- Output ถูกต้อง
- Site ถูกสร้างครบ

---

# 10. Git Workflow

ก่อนเริ่มงาน

git pull

หลังทำงาน

git add .

git commit -m "Description"

git push

ห้าม Push ถ้า Build ไม่ผ่าน

---

# 11. Documentation Rules

ทุก Feature

ต้อง Update

CHANGELOG.md

TODO.md

ROADMAP.md

ถ้ามีการเปลี่ยน Architecture

Update

ARCHITECTURE.md

---

# 12. AI Workflow

AI ทุกตัว

ต้องอ่าน

1. AI_HANDBOOK.md
2. PROJECT_CONTEXT.md
3. ROADMAP.md
4. TODO.md
5. CHANGELOG.md

ก่อนเริ่มงาน

---

# 13. AI Restrictions

AI ห้าม

- เปลี่ยนโครงสร้าง Project โดยไม่มีเหตุผล
- ลบ Builder
- รวมหลาย Module ที่แยกหน้าที่แล้ว
- เปลี่ยน API โดยไม่รักษา Backward Compatibility
- Push โค้ดที่ Build ไม่ผ่าน

---

# 14. Architecture Principles

build.py

มีหน้าที่เป็น Orchestrator เท่านั้น

Business Logic

ต้องอยู่ใน

builder/

Template

ไม่มี Business Logic

Config

อยู่ใน config/

Content

อยู่ใน content/

---

# 15. Release Policy

ทุก Release

Build

↓

Test

↓

Commit

↓

Push

↓

Release

---

# 16. Roadmap

Release v2.1

Refactor Build System

Release v2.2

SQLite

Release v2.3

Dashboard

Release v2.4

SEO Engine

Release v3.0

Plugin System

Theme System

Media Library

AI Assistant

---

# 17. Definition of Done

Feature ถือว่าเสร็จเมื่อ

- Build ผ่าน
- ไม่มี Error
- ไม่มี Import Error
- Documentation Update
- Commit แล้ว
- Push แล้ว

---

# 18. AI Collaboration Policy

AI ทุกตัวต้อง

- เคารพ Architecture เดิม
- ใช้รูปแบบ Coding เดิม
- เพิ่ม Feature แบบ Modular
- ไม่เขียนโค้ดซ้ำ
- ลด Complexity
- รักษา Readability

---

# 19. Project Philosophy

SoftwareHub CMS เน้น

Simple

Maintainable

Modular

Scalable

Readable

Stable

ก่อนเพิ่ม Feature ใหม่

ต้องรักษาคุณภาพของระบบเดิม

---

END OF DOCUMENT