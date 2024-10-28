import pickle

# kitobxon = 'kitobxon.txt'

# while True:
#     book = input("Sevgan kitobingizni kiriting!To'xtatish uchun shunchaki 'Enter' ni bosing: ")
#     if not book: break
#     with open(kitobxon, 'a') as file:
#         file.write(book+'\n')
            

# with open(kitobxon) as file:
#     kitobxon = file.read()
    
# kitobxon = kitobxon.strip()

# kitobxon = kitobxon.replace('\n', ', ')    

# print(kitobxon)
        
# with open('kitobxon_info', 'wb') as file:
#     pickle.dump(kitobxon, file)


with open('kitobxon_info', 'rb') as file:
    kitobxon_info = pickle.load(file)
    
print(kitobxon_info)