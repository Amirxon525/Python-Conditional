harorat = int(input("Haroratni kiriting: "))

if harorat < 0:
    print("Juda sovuq! Issiq kiyim kiying.")
if harorat >= 0 and harorat <= 14:
    print("Sovuq. Kurtka kiying.")
if harorat >= 15:
    print("Ob-havo yaxshi.")

print(harorat)

