# SoftwareHub CMS v2
# Coding Standard

Version: 1.0

---

# Purpose

เอกสารนี้กำหนดมาตรฐานการเขียนโค้ดของ SoftwareHub CMS

Developer และ AI ทุกตัวต้องปฏิบัติตาม

---

# General Principles

โค้ดต้อง

- อ่านง่าย
- แก้ง่าย
- แยกหน้าที่
- ใช้ซ้ำได้
- ทดสอบได้

---

# Project Structure

scripts/

เป็น Entry Point

builder/

Business Logic

templates/

Presentation

content/

Content Source

config/

Configuration

docs/

Documentation

site/

Generated Output

---

# File Responsibilities

หนึ่งไฟล์

หนึ่งหน้าที่

ห้ามรวมหลายระบบไว้ในไฟล์เดียว

---

# Function Rules

- Function ควรสั้น
- ทำงานเพียงเรื่องเดียว
- ตั้งชื่อให้สื่อความหมาย
- ลดการซ้อน if

---

# Import Rules

ใช้

from pathlib import Path

หลีกเลี่ยง

os.path

Import ต้องอยู่บนสุดของไฟล์

---

# Naming Convention

Variables

snake_case

Functions

snake_case

Classes

PascalCase

Constants

UPPER_CASE

Modules

snake_case.py

---

# Build Rules

scripts/build.py

ทำหน้าที่

Orchestrator เท่านั้น

Business Logic

ต้องอยู่ใน builder/

---

# Template Rules

Template

ไม่มี Business Logic

ใช้แสดงผลเท่านั้น

---

# Error Handling

Catch Error เฉพาะจุดที่จำเป็น

Error ต้องมีข้อความที่เข้าใจง่าย

---

# Documentation

ทุก Function สำคัญ

ควรมี Docstring

ทุก Module

ควรมีคำอธิบายหน้าที่

---

# Git Rules

ก่อน Commit

ต้อง

- Build ผ่าน
- ไม่มี Syntax Error
- ไม่มี Import Error

---

# Performance

หลีกเลี่ยง Loop ซ้อน

ใช้ Pathlib

ลดการสร้าง Object ซ้ำ

---

# AI Coding Rules

AI ต้อง

- รักษา Architecture
- ไม่เขียนโค้ดซ้ำ
- ใช้ Builder เดิม
- ไม่รวม Module
- ไม่เปลี่ยน API โดยไม่จำเป็น

---

END OF DOCUMENT