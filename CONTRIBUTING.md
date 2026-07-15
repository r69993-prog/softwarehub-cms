# CONTRIBUTING

## Development Rules

- ตอบเฉพาะที่ผู้ใช้ถาม
- ทำทีละขั้น
- ห้ามข้ามขั้น
- แก้เฉพาะจุดที่มีปัญหา
- ถ้ายังไม่ผ่าน ห้ามไปต่อ

---

## File Rules

แก้ไขเฉพาะ

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

## Build

ทุกครั้งหลังแก้ไข

```bash
python3 scripts/build.py
```

ต้อง Build และตรวจผลก่อนถือว่างานเสร็จ

---

## Documentation

เมื่อทำ Feature เสร็จ

อัปเดต

- docs/SESSION.md
- docs/TODO.md
- docs/CHANGELOG.md

หากมีการเปลี่ยนแนวทางของระบบ

ให้อัปเดต

- docs/DECISIONS.md

---

## Before Working

อ่านเอกสารตามลำดับ

1. docs/AI_HANDOVER.md
2. docs/PROJECT_CONTEXT.md
3. docs/SESSION.md
4. docs/TODO.md

แล้วจึงเริ่มทำงาน

---

## Branch Rule

ทำงานบน Branch ปัจจุบัน

Commit เมื่อทำงานเสร็จแต่ละ Feature

---

## Goal

พัฒนา SoftwareHub CMS

ให้เป็น Static CMS ที่รองรับ

- SEO
- Automation
- AI
- Easy Maintenance