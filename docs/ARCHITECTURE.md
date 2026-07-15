# ARCHITECTURE

Last Update

2026-07-14

---

# System Overview

SoftwareHub CMS เป็น Static CMS

ไม่มี Database

ข้อมูลทั้งหมดถูกเก็บในไฟล์ CSV

เมื่อ Build ระบบจะสร้างเว็บไซต์ HTML ทั้งหมด

---

# High Level Architecture

User

↓

CSV Content

↓

Python

↓

Jinja2

↓

HTML

↓

site/

↓

Deploy

---

# Project Structure

config/

เก็บการตั้งค่าเว็บไซต์

เช่น

- ชื่อเว็บไซต์
- SEO
- ภาษา

---

content/

เก็บข้อมูลทั้งหมด

ปัจจุบัน

software.csv

อนาคต

article.csv

category.csv

tag.csv

---

scripts/

Business Logic

ประกอบด้วย

content.py

โหลดข้อมูล

build.py

สร้างเว็บไซต์

อนาคต

search.py

seo.py

deploy.py

import.py

---

templates/

Jinja2 Templates

base.html

Layout หลัก

home.html

หน้าแรก

article.html

หน้ารายละเอียด

อนาคต

category.html

search.html

404.html

rss.xml

sitemap.xml

---

static/

Static Assets

css/

images/

icons/

fonts/

javascript/

---

site/

ผลลัพธ์หลัง Build

ประกอบด้วย

HTML

CSS

Images

พร้อม Deploy

ห้ามแก้ไขไฟล์ในโฟลเดอร์นี้โดยตรง

เพราะจะถูก Build ใหม่ทุกครั้ง

---

docs/

เอกสารของโปรเจกต์

PROJECT_CONTEXT.md

SESSION.md

ROADMAP.md

TODO.md

CHANGELOG.md

ARCHITECTURE.md

---

# Build Flow

software.csv

↓

content.py

↓

Python Objects

↓

Jinja2 Templates

↓

HTML Files

↓

site/

---

# Build Command

python3 scripts/build.py

---

# Deployment Flow

Development

↓

GitHub

↓

GitHub Actions

↓

Cloudflare Pages

↓

Custom Domain

---

# Design Principles

Static First

CSV First

No Database

SEO Friendly

Fast

Simple

Reusable

AI Friendly

Easy Deployment

Easy Maintenance

---

# Future Architecture

Admin Panel

↓

CSV Generator

↓

AI Import

↓

Build

↓

GitHub Actions

↓

Deploy

↓

Cloudflare Pages

---

# Development Rules

ห้ามแก้ไขไฟล์ใน

site/

โดยตรง

ให้แก้เฉพาะ

templates/

static/

scripts/

content/

config/

จากนั้น Build ใหม่ทุกครั้ง

---

# AI Rules

AI ทุกตัวต้อง

1.

อ่าน PROJECT_CONTEXT.md

2.

อ่าน SESSION.md

3.

อ่าน TODO.md

4.

ตรวจโครงสร้างโปรเจกต์

5.

ทำงานต่อจาก Current Task

ห้ามเปลี่ยน Architecture

ห้ามเปลี่ยนโครงสร้างโฟลเดอร์

ห้ามเพิ่ม Framework ใหม่

ยกเว้นผู้ใช้สั่งโดยตรง