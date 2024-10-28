import re

example = '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'

while True:
    phone = input("Iltimos telefon raqamingizni kiriting: ")
    if re.match(example, phone):
        print("Rahmat! Tez orada siz bilan bog'lanamiz!")
        break
    else:
        print("Iltimos telefon raqam kirgissangiz!")