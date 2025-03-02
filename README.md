# 🛍 Cafe Shop Telegram Web3 Bot

Bu **Web3 Shop Telegram Bot** mahsulotlarni qo‘shish, ularni foydalanuvchilarga ko‘rsatish va savatchaga qo‘shish imkonini beradi. Bot Web3 HTML bilan bog‘langan bo‘lib, foydalanuvchilar mahsulotlarni bot orqali tanlashi va to‘lovni amalga oshirishi mumkin.

## 🚀 Xususiyatlar
- 🔹 **Admin paneli** — admin mahsulot qo‘shishi, o‘chirish va tahrirlashi mumkin
- 🛍 **Mahsulotlar ko‘rinishi** — foydalanuvchilar mahsulotlarni ko‘rishi va savatchaga qo‘shishi mumkin
- 🛒 **Savatcha** — foydalanuvchi savatchasini boshqarish imkoniyati
- 💳 **To‘lov tizimi** — RHMT.uz orqali to‘lov
- 📩 **Taklif va shikoyatlar** — foydalanuvchilar fikr qoldirishi va bu adminlarga yuboriladi

---

## ⚙️ Texnologiyalar
- **Aiogram 3.x** — Asinxron Telegram bot framework
- **SQLite** — Mahsulotlar va buyurtmalar uchun ma’lumotlar bazasi
- **Tortoise-ORM** — ORM ma’lumotlar bazasi bilan ishlash uchun
- **Web3 HTML, CSS, JavaScript** — Do‘kon interfeysi
- flask
---

## 🔧 O‘rnatish

### 1️⃣ Botni klonlash
```bash
git clone https://github.com/username/web3-shop-bot.git
cd web3-shop-bot
```

### 2️⃣ Virtual muhit yaratish
```bash
python -m venv venv
source venv/bin/activate  # Linux & macOS
env\Scripts\activate  # Windows
```

### 3️⃣ Kerakli kutubxonalarni o‘rnatish
```bash
pip install -r requirements.txt
```

### 4️⃣ `config.py` faylini yaratish va to‘ldirish
Bot uchun token va ma’lumotlar bazasi sozlamalarini o‘rnatish kerak:
```python
BOT_TOKEN = "YOUR_BOT_TOKEN"
ADMIN_ID = [123456789]  # Admin Telegram ID
DATABASE_URL = "sqlite://db.sqlite3"
WEB3_SHOP_URL = "https://your-web3-shop.com"
```

### 5️⃣ Botni ishga tushirish
```bash
python bot.py
```

---

## 🛠 Buyruqlar
| Buyruq | Tavsif |
|--------|---------|
| `/start` | Botni ishga tushirish |
| `/admin` | Admin paneliga kirish |
---

## 📬 Aloqa
Agar biror muammo yoki taklif bo‘lsa, quyidagi kanallar orqali bog‘laning:
- **Telegram:** [@None_oo8)
- **GitHub Issues** bo‘limida yangi xabar qoldiring.

✅ **Dasturdan zavqlaning!** 🎉

