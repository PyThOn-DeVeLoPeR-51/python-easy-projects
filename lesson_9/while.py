# user = "Yaxshi ko'rgan kitoblaringizni kiriting!"
# user += "(Dasturni to'xtatish uchun 'stop' deb yozing): "
# while True:
#     k = input(user)
#     if k == 'stop':
#         break
# print("Dastur tugadi!")    

# user = "Iltimos, yoshingizni kiriting!"
# user += "(Dasturni to'xtatish uchun 'exit' yoki 'quit' deb yozing): "
# k = ''
# while k != 'exit' or 'quit':
#     k = input(user)
#     if k <= 7:
#         print(int("Sizga chipta narxi 2000 so'm"))
#     elif k > 7 and k <= 18:
#         print("Sizga chipta narxi 3000 so'm")
#     elif k > 18 and k <= 65:
#         print("Sizga chipta narxi 10000 so'm")
#     elif k > 65:
#         print("Sizga chipta narxi bepul")
# print("Rahmat!")
    
# user = "Iltimos, yoshingizni kiriting!"
# user += "(Dasturni to'xtatish uchun 'exit' yoki 'quit' deb yozing): "
# while True:
#     k = input(user)
#     if k == 'exit' or k == 'quit':
#         break
#     yosh = int(k)
    
#     if yosh <= 7:
#         narx = 2000
#     elif 7 < yosh <= 18:
#         narx = 3000
#     elif 18 < narx <= 65:
#         narx = 10000
#     else:
#         narx = 0
        
#     if narx == 0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Sizga {narx} so'm")
# print("Rahmat!")

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat == 0:
#         continue
#     son = float(qiymat)
    
#     if son=='Exit':
#         break
#     else:
#         ildiz = son**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")
   
while True:
    q = input(savol)
    if q == 'exit':
        break
    son = float(q)
    
    if son != 'exit':
        ildiz = son**(0.5)
        print(f"{son} ning ildizi {ildiz} ga teng")
print("Rahmat!")
   
        
        

