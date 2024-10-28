import json

# =============================================================================
# # data = {"Model":"Malibu",
# #         "Color":"Black",
# #         "Year":2020,
# #         "Price":40000}
# 
# # data_json = json.dumps(data)
# # print(type(data_json))
# 
# # with open('data_json.json', 'w') as f:
# #     json.dump(data_json, f)
# =============================================================================


# =============================================================================
# talaba = {"ism":"Hasan",
#           "familiya":"Husanov",
#           "tyli":2000}
# 
# talaba_json = json.dumps(talaba)
# 
# talaba = json.loads(talaba_json)
# 
# print(f" {talaba['ism']} {talaba['familiya']}")
# 
# with open('talaba.json', 'w') as f:
#     json.dump(talaba, f)
# =============================================================================

filename = 'students.json'
with open(filename) as f:
    students = json.load(f)
    
name = students['student'][0]['name']
lastname = students['student'][0]['lastname'] 
course = students['student'][0]['year']
faculty = students['student'][0]['faculty']
    
print(f"{name} {lastname} {course}-kurs {faculty} fakulteti")    
    