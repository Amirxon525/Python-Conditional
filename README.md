# Python Mashqlar (if, if-else, elif)

## if Operatori

### 🔹 **1. Absolyut qiymat**
**Vazifa:** Foydalanuvchidan butun son kiritsini so'rang. Agar son manfiy bo'lsa, uni musbatga o'zgartirib chiqaring. Faqat `if` dan foydalaning.

**Misol:**
```
Kirish: -5
Chiqish: 5
```

---

### 🔹 **2. Ism tekshiruvi**
**Vazifa:** Foydalanuvchidan ismini so'rang. Agar foydalanuvchi hech narsa kiritmasa (bo'sh string `""`), `"Ism kiritilmadi"` deb chiqaring. Faqat `if` ishlating.

**Misol:**
```
Kirish: (bo'sh)
Chiqish: Ism kiritilmadi
```

---

### 🔹 **3. Bo'linuvchanlikni tekshirish**
**Vazifa:** Foydalanuvchidan son kiritsini so'rang. Shu son:
- 2 ga bo'linishini
- 3 ga bo'linishini  
- 5 ga bo'linishini

alohida `if` lar bilan tekshiring va har bir holat uchun alohida xabar chiqaring.

**Misol:**
```
Kirish: 30
Chiqish: tasnif**
**Vazifa:** Foydalanuvchidan vazn (kg) va bo'y (m) so'rang. BMI ni hisoblang va tasniflang:
- BMI < 18.5: "Kam vazn"
- 18.5 ≤ BMI < 25: "Normal vazn"
- 25 ≤ BMI < 30: "Ortiqcha vazn"  
- BMI ≥ 30: "Semizlik"

**Formula:** BMI = vazn / (bo'y)²

**Qo'shimcha tekshiruvlar:**
- Vazn va bo'y musbat bo'lishi kerak
- Bo'y 0.5-3.0 m oralig'ida bo'lishi kerak
- Vazn 1-500 kg oralig'ida bo'lishi kerak

**Misol:**
```
Vazn: 70
Bo'y: 1.75
BMI: 22.86
Tasnif: Normal vazn
```

30 soni 2 ga bo'linadi
30 soni 3 ga bo'linadi
30 soni 5 ga bo'linadi
```

---

### 🔹 **4. Yoshga bog'liq chegirma**
**Vazifa:** 
Chipta narxi 100 so'm. Foydalanuvchidan yoshini so'rang va chegirmani qo'llang:
- 7 yoshgacha (0-6): 50% chegirma
- 7-17 yosh: 20% chegirma  
- 60 yoshdan katta: 30% chegirma

Yakuniy narxni chiqaring. Faqat `if` ishlating (bir nechta `if` dan foydalanish mumkin).

**Misol:**
```
Kirish: 5
Chiqish: Yakuniy narx: 50 so'm (50% chegirma qo'llanildi)
```

---

### 🔹 **5. Haroratga mos maslahat**
**Vazifa:** Foydalanuvchidan haroratni (°C) so'rang va maslahat bering:
- 0°C dan past: `"Juda sovuq! Issiq kiyim kiying."`
- 0-14°C orasida: `"Sovuq. Kurtka kiying."`  
- 15°C va undan yuqori: `"Ob-havo yaxshi."`

Har bir shartni alohida `if` bilan tekshiring.

---

## if-else Operatori

### 🔹 **1. Kirish ruxsati**
**Vazifa:** Foydalanuvchidan yoshini so'rang. Agar 18 yoshdan katta yoki teng bo'lsa, `"Kirishga ruxsat berildi."`, aks holda `"Kirish rad etildi. Yosh 18 dan kichik."` deb chiqaring.

---

### 🔹 **2. Parol tekshiruvi**
**Vazifa:** Foydalanuvchidan parol kiritsini so'rang. Parol quyidagi shartlarni bajarishi kerak:
- Kamida 8 belgidan iborat bo'lishi
- Kamida 1 harf va 1 raqam bo'lishi kerak

Agar parol to'g'ri bo'lsa, `"Parol qabul qilindi."`, aks holda `"Parol noto'g'ri. Kamida 8 belgi, 1 harf va 1 raqam bo'lishi kerak."` deb chiqaring.

**Maslahat:** `isalpha()`, `isdigit()`, `len()` funksiyalaridan foydalaning.

---

### 🔹 **3. Fayl mavjudligini tekshirish**
**Vazifa:** Foydalanuvchidan fayl nomini so'rang. Agar fayl mavjud bo'lsa, `"Fayl '<fayl nomi>' mavjud."`, aks holda `"Fayl '<fayl nomi>' topilmadi."` deb chiqaring. 

**Maslahat:** `os.path.exists()` funksiyasidan foydalaning.

```python
import os
```

---

### 🔹 **4. Bank hisobini tekshirish**
**Vazifa:** 
Hisobingizda 5000 so'm bor. Foydalanuvchidan yechmoqchi bo'lgan summani so'rang.
- Agar mablag' yetarli bo'lsa: `"Pul yechildi. Qolgan balans: X so'm"`
- Yetarli bo'lmasa: `"Mablag' yetarli emas. Sizning balansingiz: 5000 so'm"`

**Qo'shimcha:** Manfiy son kiritilsa, `"Manfiy summa kiritib bo'lmaydi."` deb chiqaring.

---

### 🔹 **5. Email manzilini tekshirish**
**Vazifa:** Foydalanuvchidan email manzilini so'rang. Email quyidagi shartlarni bajarishi kerak:
- `@` belgisini o'z ichiga olishi
- `.com`, `.uz`, `.net` yoki `.org` bilan tugashi

Agar to'g'ri bo'lsa, `"Email qabul qilindi."`, aks holda `"Email noto'g'ri formatda."` deb chiqaring.

---

## elif Operatori

### 🔹 **1. Baholash tizimi**
**Vazifa:** Foydalanuvchidan ball (0-100) so'rang va bahoni chiqaring:
- 90-100: "A (A'lo)"
- 80-89: "B (Yaxshi)"  
- 70-79: "C (Qoniqarli)"
- 60-69: "D (Qoniqarsiz)"
- 0-59: "F (Rad)"

Agar 0-100 oralig'idan tashqari son kiritilsa, `"Ball 0-100 oralig'ida bo'lishi kerak!"` deb chiqaring.

---

### 🔹 **2. Sodda kalkulyator**
**Vazifa:** Foydalanuvchidan ikkita son va amalni (+, -, *, /) so'rang. Hisoblashni bajaring. 
- Agar bo'lishda ikkinchi son 0 bo'lsa: `"Nolga bo'lish mumkin emas!"`
- Noto'g'ri amal kiritilsa: `"Noto'g'ri amal. Faqat +, -, *, / ishlatiladi."`

**Misol:**
```
1-son: 10
2-son: 3  
Amal: +
Natija: 10 + 3 = 13
```

---

### 🔹 **3. Kun davomidagi vaqt**
**Vazifa:** Soatni (0-23) so'rang va vaqt oralig'ini aniqlang:
- 5-11: "Ertalab"
- 12-17: "Kunduzi"  
- 18-21: "Kechqurun"
- 22-4: "Tun"

Agar 0-23 oralig'idan tashqari son kiritilsa, `"Soat 0-23 oralig'ida bo'lishi kerak!"` deb chiqaring.

---

### 🔹 **4. Transport tanlash**
**Vazifa:** Masofani (km) so'rang va transportni tavsiya qiling:
- 0-1 km: "Piyoda yuring"
- 1-5 km: "Velosiped yoki elektr skuter"
- 5-50 km: "Avtobus yoki mashina"  
- 50+ km: "Poyezd yoki samolyot"

Manfiy masofa kiritilsa, `"Masofa manfiy bo'la olmaydi!"` deb chiqaring.

---

### 🔹 **5. BMI hisoblash va 