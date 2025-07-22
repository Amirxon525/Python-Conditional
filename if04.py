yosh = int(input("Yoshingizni kiriting: "))
narx = 100

if yosh >= 0 and yosh <= 6:
    narx = narx * 0.5
if yosh >= 7 and yosh <= 17:
    narx = narx * 0.8
if yosh > 60:
    narx = narx * 0.7

if yosh < 0 or yosh > 120:  
    print("Xato: not‘gri yosh kiritdingiz.")
else:
    print("Siz to'lashingiz kerak bo'lgan summa:", narx, "so'm")


