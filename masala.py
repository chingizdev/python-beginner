# python-beginner
#my basic programs

#1-sonning kvadrati va kubini topish

son = input("Istalgan sonni kiriting\n->")
son = int(son)
print(f"{son} ning kvadrati {son**2} ga teng")
print(f"{son} ning kubi {son**3} ga teng")

#2-yoshga qarab tug'ilgan yilni aniqlash

yosh = input("Yoshingizni kiriting\->")
yosh = int(yosh)
yil = 2021-yosh
print(f"Siz {yil} da tug'ilgansiz!")

#3-Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur

son1 = input('Birinchi sonni kiriting\n->')
son2 = input('Ikkinchi sonni kiriting\n->')
son1 = float(son1)
son2 = float(son2)
print(f"{son1} + {son2} = {son1+son2}")
print(f"{son1} - {son2} = {son1-son2}")
print(f"{son1} * {son2} = {son1*son2}")
print(f"{son1} / {son2} = {son1/son2}")
