#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# =============================================================================
# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#     else:
#         print(car.capitalize())
# =============================================================================

# =============================================================================
# foydalanuvchi_ismi = input("Iltimos, login kiriting: ")
# if foydalanuvchi_ismi.lower() == 'admin':
#     print("Hush kelibsiz, Admin! Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Hush kelibsiz!, {foydalanuvchi_ismi}")
# =============================================================================
  
# =============================================================================
# x = float(input("Iltimos, 1 - sonni kiriting: "))
# y = float(input("Iltimos, 2 - sonni kiriting: "))
# if x == y:
#     print(f"sonlar teng ekan, {x} = {y}")
# else:
#     print("Rahmat!")
# =============================================================================

# =============================================================================
# son = float(input("Iltimos, istalgan sonni kiriting: "))
# if son < 0:
#     print("Bu manfiy son")
# else:
#     print("Bu musbat son")
# =============================================================================

son = float(input("Iltimos, istalgan sonni kiriting: "))
if son >= 0:
    print(son**(1/2))
else:
    print("Iltimos, musbat son kiriting!")
    