# DEPLOY

## Current Deployment

Development

GitHub Codespaces

---

## Build

```bash
python3 scripts/build.py
```

---

## Deploy Folder

อัปโหลดเฉพาะ

```text
site/
```

ไปยังผู้ให้บริการ Static Hosting

---

## Recommended Platform

- Cloudflare Pages
- GitHub Pages
- Netlify

---

## Future Deployment

GitHub

↓

GitHub Actions

↓

Build

↓

Cloudflare Pages

↓

Custom Domain

---

## Production Checklist

- Build ผ่าน
- ตรวจหน้า Home
- ตรวจหน้า Article
- ตรวจรูปภาพ
- ตรวจ CSS
- ตรวจลิงก์
- ตรวจ Sitemap
- ตรวจ robots.txt

---

## Deployment Rule

ห้าม Deploy

หาก Build ไม่ผ่าน

ทุกครั้งก่อน Deploy

ต้อง Build ใหม่เสมอ