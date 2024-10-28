#ismlar = ['Ali', 'Vali', 'Gani', 'Nodir', 'Sardor']
#for ism in ismlar:
    #print("Assalomu alaykum", ism)
#print("Kod", len(ismlar), "marta takrorlandi" )

#sonlar = list(range(11, 100, 2))
#for son in sonlar:
#    print(son**3)

kinolar = []
print("O'zingiz yoqtirgan 5 ta kinoni yozing")
for n in range(5):
    kinolar.append(input(f"Iltimos, {n+1} - kinoni yozing: ").capitalize())
print(kinolar)