# SoftwareHub CMS

## Project Overview

SoftwareHub CMS เป็นระบบ Static CMS สำหรับสร้างเว็บไซต์รวมโปรแกรมโดยใช้ Python + Jinja2

ข้อมูลทั้งหมดถูกเก็บไว้ในไฟล์ CSV

เมื่อ Build ระบบจะสร้างเว็บไซต์ HTML ทั้งหมดโดยอัตโนมัติ

จุดประสงค์ของโปรเจกต์

- สร้างเว็บไซต์ได้จากข้อมูลเพียงชุดเดียว
- ไม่มี Database
- SEO Friendly
- โหลดเร็ว
- Deploy ง่าย
- รองรับ AI Automation ในอนาคต

---

# Current Version

SoftwareHub CMS v2

---

# Project Status

กำลังพัฒนา

Progress โดยประมาณ

CMS Core

65%

Project ทั้งหมด

25%

---

# Technology Stack

Python 3

Jinja2

CSV

HTML5

CSS3

Git

GitHub

GitHub Codespaces

---

# Project Structure

config/

content/

docs/

scripts/

static/

templates/

site/

---

# Folder Responsibilities

config/

เก็บค่าต่าง ๆ ของเว็บไซต์

เช่น

ชื่อเว็บ

SEO

ภาษา

---

content/

เก็บข้อมูลโปรแกรมทั้งหมด

ปัจจุบันใช้

software.csv

---

scripts/

Build Engine

เช่น

content.py

build.py

---

templates/

Jinja2 Templates

base.html

home.html

article.html

---

static/

CSS

Images

Assets

---

site/

ผลลัพธ์หลัง Build

HTML

CSS

Images

พร้อม Deploy

---

docs/

เอกสารทั้งหมดของโปรเจกต์

---

# Current Build Flow

software.csv

↓

content.py

↓

build.py

↓

Jinja2

↓

site/

↓

Deploy

---

# Build Command

python3 scripts/build.py

---

# Current Features

✔ Load Config

✔ Load CSV

✔ Build Home Page

✔ Build Article Page

✔ Copy CSS

✔ Copy Images

✔ Static HTML Generation

✔ Responsive Layout (กำลังปรับปรุง)

✔ Search Box UI

---

# Features In Progress

Home UI

Article UI

Responsive Design

SEO Layout


---

# Features Planned

Search

Category

Tag

Pagination

Breadcrumb

Sitemap.xml

robots.txt

RSS Feed

Open Graph

Schema.org

Dark Mode

Search Index

Admin Panel

Import URL

Crawler

AI Import

AI Rewrite

GitHub Actions

Cloudflare Pages Deploy

Auto Update

---

# Coding Rules

ตอบเฉพาะที่ผู้ใช้ถาม

ตอบสั้น

ทำทีละขั้น

ห้ามข้ามขั้น

ห้ามเดา

ห้ามสมมุติ

ถ้ายังไม่ได้ตรวจ

ห้ามบอกว่าเสร็จ

แก้เฉพาะจุดที่มีปัญหา

เมื่อแก้ไฟล์

ให้แก้ทั้งไฟล์

ถ้าไฟล์ยาวเกิน

แบ่งเป็น

Part 1

Part 2

Part 3

จนจบไฟล์

ทุกครั้งหลังแก้

ต้อง Build

และตรวจผล

หากไม่ผ่าน

ห้ามไป Feature ถัดไป

---

# Development Principles

Static First

CSV First

Simple

Fast

SEO Friendly

AI Friendly

Easy Maintenance

Easy Deployment

No Database

---

# Architecture

CSV

↓

Python

↓

Jinja2

↓

Static HTML

↓

Deploy

---

# Deployment Plan

Development

↓

GitHub Codespaces

↓

GitHub Repository

↓

Cloudflare Pages

↓

Custom Domain

↓

Automation

---

# Current UI Status

Home Page

ใช้งานได้

อยู่ระหว่างปรับปรุง Layout

Article Page

ใช้งานได้

อยู่ระหว่างออกแบบใหม่

Search

มีเฉพาะ UI

ยังไม่มีระบบค้นหา

Category

ยังไม่เริ่ม

SEO

ยังไม่เริ่ม

Automation

ยังไม่เริ่ม

AI

ยังไม่เริ่ม

---

# Long Term Goal

ผู้ดูแลเว็บไซต์

เพิ่มโปรแกรมเพียงครั้งเดียว

ระบบทำงานอัตโนมัติทั้งหมด

ในอนาคต

กรอกชื่อโปรแกรม

↓

AI ค้นหาข้อมูล

↓

AI ตรวจสอบ

↓

AI ดาวน์โหลดรูป

↓

AI สร้างบทความ

↓

Build Website

↓

Deploy Website

ทั้งหมดอัตโนมัติ


---

# Roadmap

Phase 1

Foundation

Status

Completed

---

Phase 2

CMS Core

Status

In Progress

---

Phase 3

UI / UX

Status

In Progress

---

Phase 4

SEO

Status

Not Started

---

Phase 5

Automation

Status

Not Started

---

Phase 6

AI Integration

Status

Not Started

---

Phase 7

Production

Status

Not Started

---

# Current Priority

1.

ปรับ Home Page UI

2.

ปรับ Article Page UI

3.

Category

4.

Search System

5.

SEO

6.

Sitemap

7.

RSS Feed

8.

robots.txt

9.

Deploy

10.

Automation

11.

AI Import

12.

Admin Panel

---

# Important Notes For Next AI

ก่อนเริ่มทำงาน

ให้อ่านไฟล์ต่อไปนี้ตามลำดับ

1.

docs/PROJECT_CONTEXT.md

2.

docs/SESSION.md

3.

docs/TODO.md

4.

docs/ROADMAP.md

5.

docs/ARCHITECTURE.md

6.

docs/CHANGELOG.md

หลังจากอ่านครบ

ให้สรุปความเข้าใจของโปรเจกต์ก่อน

จากนั้นตรวจโครงสร้างโปรเจกต์จริง

ตรวจไฟล์ที่เกี่ยวข้อง

และทำงานต่อจาก Current Task

ห้ามสร้างระบบใหม่ที่ซ้ำกับของเดิม

ห้ามเปลี่ยน Architecture

ห้ามเปลี่ยนโครงสร้างโฟลเดอร์

ห้ามเปลี่ยน Coding Rules

ยกเว้นผู้ใช้สั่งโดยตรง

หากพบ Bug

ให้แก้ Bug นั้นจนผ่านก่อน

จึงเริ่มงานถัดไป

---

# Vision

SoftwareHub CMS จะพัฒนาเป็น Static CMS Engine

ที่สามารถสร้างเว็บไซต์หลายประเภทจาก Engine เดียว

เช่น

Software

Games

Movies

Books

Courses

Fonts

Icons

Templates

AI Tools

News

และ Content ประเภทอื่น

โดยใช้ Workflow เดียวกัน

คือ

Data

↓

Build

↓

Static Site

↓

Deploy

↓

Automation

↓

AI


