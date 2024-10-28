# savol = "mahsulotlar nomini kiriting:"
# n = 1
# mahsulotlar = []

# while True:
#     q = input(f"Iltimos, {n} - {savol} ")
#     mahsulotlar.append(q)
#     again = input("Yana mahsulot kiritishni xohlaysizmi? ha/yo'q ")
#     n += 1
#     if again != "ha":
#         break
# print("Rahmat!")
# print(mahsulotlar)

# print("e-bozor uchun mahsulotlar va ularning narhlari")
# products = {}

# while True:
#     name = input("Iltimos, mahsulot nomini kiriting: ")
#     price = input("Iltimos, mahsulot narxini kiriting: ")
#     products[name] = int(price)
#     again = input("Yana mahsulot kiritishni xohlaysizmi? ha/yo'q ")
#     if again != 'ha':
#         break
    
# for k, q in products.items():
#     print(f"{k} - {q} so'm")

buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")
    