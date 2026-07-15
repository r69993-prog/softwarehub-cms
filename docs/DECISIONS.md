# DECISIONS

Last Update

2026-07-14

---

# Purpose

ไฟล์นี้ใช้บันทึกเหตุผลในการตัดสินใจออกแบบระบบ

เพื่อให้ผู้พัฒนาและ AI ในอนาคตเข้าใจว่า

"ทำไมจึงเลือกแนวทางนี้"

ห้ามเปลี่ยนแนวทางที่ระบุไว้

โดยไม่มีเหตุผลที่ดีกว่า

---

# Decision 001

Title

ใช้ Static Website

Status

Approved

Reason

- โหลดเร็ว
- Deploy ง่าย
- ค่าใช้จ่ายต่ำ
- SEO ดี
- Security สูง
- ไม่ต้องดูแล Server

Alternative

Dynamic Website

Result

Rejected

---

# Decision 002

Title

ใช้ CSV เป็นแหล่งข้อมูลหลัก

Status

Approved

Reason

- อ่านง่าย
- แก้ไขง่าย
- ใช้ Git ได้ดี
- AI สร้างข้อมูลได้ง่าย
- Export / Import ง่าย

Alternative

Database

Result

Deferred

จะพิจารณาอีกครั้ง

เมื่อโปรเจกต์มีความจำเป็นจริง

---

# Decision 003

Title

ใช้ Python

Status

Approved

Reason

- Build Script เขียนง่าย
- Library เยอะ
- AI เข้าใจโค้ดได้ดี
- ดูแลรักษาง่าย

Alternative

Node.js

PHP

Result

Rejected

---

# Decision 004

Title

ใช้ Jinja2

Status

Approved

Reason

- Template อ่านง่าย
- แยก HTML ออกจาก Logic
- ดูแลระยะยาวง่าย

Alternative

เขียน HTML ด้วย Python

Result

Rejected

---

# Decision 005

Title

แยก Template และ Static Assets

Status

Approved

Reason

แก้ไข Layout ได้โดยไม่ต้องแก้ Build Script

---

# Decision 006

Title

ห้ามแก้ไขโฟลเดอร์ site/

Status

Approved

Reason

site/

เป็นผลลัพธ์จากการ Build

หากแก้ไขโดยตรง

ข้อมูลจะหาย

ทุกการแก้ไข

ต้องแก้จาก

templates/

หรือ

static/

แล้ว Build ใหม่

---

# Decision 007

Title

Documentation First

Status

Approved

Reason

โปรเจกต์ต้องสามารถส่งต่อให้

AI

หรือ

Developer

คนใหม่

ได้โดยไม่ต้องอาศัยประวัติ Chat

---

# Decision 008

Title

Automation First

Status

Approved

Reason

เป้าหมายสุดท้าย

คือ

เพิ่มข้อมูลเพียงครั้งเดียว

ระบบสร้างเว็บไซต์ทั้งหมด

อัตโนมัติ

---

# Decision 009

Title

Deploy ด้วย Cloudflare Pages

Status

Current Plan

Reason

- ฟรี
- CDN
- SSL
- Deploy อัตโนมัติ
- รองรับ Domain
- เหมาะกับ Static Site

สามารถเปลี่ยนได้ในอนาคต

หากมีเหตุผลรองรับ

---

# Decision 010

Title

AI Friendly Project

Status

Approved

Reason

ทุกส่วนของโปรเจกต์

ต้องออกแบบให้ AI

สามารถเข้าใจ

แก้ไข

และต่อยอด

ได้ง่าย

---

# Project Principles

- Static First
- CSV First
- Documentation First
- SEO First
- Simple
- Fast
- Reusable
- Automation
- AI Friendly
- Easy Maintenance

---

# Rules

หากมีการตัดสินใจสำคัญใหม่

ให้เพิ่มเป็น

Decision 011

Decision 012

Decision 013

...

ห้ามแก้ไข Decision เก่า

ให้เพิ่มรายการใหม่แทน

เพื่อเก็บประวัติการออกแบบของโปรเจกต์