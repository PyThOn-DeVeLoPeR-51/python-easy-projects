# =============================================================================
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# 
# def katta_harf(matnlar):
#     for n in range(len(matnlar)):
#         matnlar[n] = matnlar[n].title()
#     
# katta_harf(ismlar)
# print(ismlar)
# 
# =============================================================================


# =============================================================================
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# 
# def katta_harf(matnlar):
#     matnlar = matnlar[:]
#     for n in range(len(matnlar)):
#         matnlar[n] = matnlar[n].title()
#     return matnlar
#     
# yangi_ismlar = katta_harf(ismlar)
# print(yangi_ismlar)
# =============================================================================
        

ismlar = ['ali', 'vali', 'hasan', 'husan']

def bahola(ismlar):
    talabalar = {}
    for ism in ismlar:
        baho = int(input(f"Talaba {ism.title()}ning bahosni kiriting: "))
        talabalar[ism] = baho
    return talabalar

talabalar = bahola(ismlar)
print(talabalar)
print(ismlar)

        