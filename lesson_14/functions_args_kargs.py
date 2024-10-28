# =============================================================================
# def kopaytir(*sonlar):
#     kopaytma = 1
#     for son in sonlar:
#         kopaytma *= son
#     return kopaytma
# 
# print(kopaytir(2,4))    
# =============================================================================

def talaba_info(ismi, familiyasi, **malumotlar):
    
    malumotlar['ism'] = ismi
    malumotlar['familiya'] = familiyasi
    return malumotlar

talaba = talaba_info("Nodir", "Komilov", yosh = 36, joy = "Namangan")
print(talaba)