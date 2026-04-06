# import json

# kitob = {"sarlavha": "Algoritmlar", "muallif": "Knuth", "yil": 1968, "bor": True}

# json_res = json.dumps(kitob, indent=4, ensure_ascii=False)
# print(json_res)



# import json

# self = '{"ism": "Dilnoza", "yosh": 27, "manzil": {"shahar": "Samarqand", "ko\'cha": "Registon"}}'

# json_res = json.loads(self)
# print(json_res)

# print(type(json_res))
# print(json_res['manzil']['shahar'])



# import json

# students = [
#     {"ism": "Ali", "yosh": 22, "baho": 57},
#     {"ism": "Aziz", "yosh": 23, "baho": 84},
#     {"ism": "Bobur", "yosh": 24, "baho": 73},
#     {"ism": "Sardor", "yosh": 25, "baho": 92},
#     {"ism": "Olim", "yosh": 26, "baho": 81}
# ]

# with open("students.json", "w", encoding="utf-8") as fayl:
#     json.dump(students, fayl, indent=4, ensure_ascii=False)


# with open("students.json", "r", encoding="utf-8") as fayl:
#     top_students = [
#         student for student in json.load(fayl) if student["baho"] >= 80
#     ]

# print(top_students)
# print(type(top_students))



# import json

# json_str = '{"mahsulot": "qalam", "narx": 2000}'
# to_py = json.loads(json_str)
# print(type(to_py))

# miqdor = to_py.get("miqdor", "Nomalum")
# print(miqdor)

# kategoriya = to_py.get("kategoriya", "Nomalum")
# print(kategoriya)



# import json
# json_str = '''
# {
#   "users": [
#     {"id": 1, "ism": "Akbar", "faol": true},
#     {"id": 2, "ism": "Barno", "faol": false},
#     {"id": 3, "ism": "Camila", "faol": true},
#     {"id": 4, "ism": "Davron", "faol": false},
#     {"id": 5, "ism": "Ezgulik", "faol": true}
#   ]
# }     '''

# res = [user.get("ism") for user in json.loads(json_str).get("users") if user["faol"]]
# print(res)



# import json 

# user = {"ism": input("ism: "), 
#         "yosh": input("yosh:"),
#         "shahar": input("shahar: ") 
#         }

# with open("user.json", "w", encoding="utf-8") as fayl:
#     json.dump(user, fayl, indent=4, ensure_ascii=False)



# import json

# mahsulotlar = [
#     {"id": 1, "nom": "qalam", "narx": 2000},
#     {"id": 2, "nom": "daftar", "narx": 5000},
#     {"id": 3, "nom": "ruchka", "narx": 3000},
#     {"id": 4, "nom": "o'yinqaroq", "narx": 15000},
#     {"id": 5, "nom": "kompyuter", "narx": 500000}
# ]

# with open("mahsulotlar.json", "w", encoding="utf-8") as file:
#     json.dump(mahsulotlar, file, indent=4, ensure_ascii=False)

# with open("mahsulotlar.json", "r", encoding="utf-8") as file:
#     print(sorted(json.load(file), key=lambda x: x["narx"], reverse=True)[:3])



# import json

# with open("info_std.json", "r", encoding="utf-8") as file:
#     students = json.load(file)

# for student in students["talabalar"]:
#     average = sum(student["baholar"].values()) / len(student["baholar"])
#     print(f"{student['ism']}ning o'rtacha bahosi: {average:.2f}")


import json

class Mahsulot:
    def __init__(self, nomi, narx, miqdor):
        self.nomi = nomi
        self.narx = narx
        self.miqdor = miqdor
    
    def dict(self):
        return {"nomi": self.nomi, "narx": self.narx, "miqdor": self.miqdor}

m1 = Mahsulot("qalam", 2000, 100)
m2 = Mahsulot("daftar", 5000, 200)
m3 = Mahsulot("ruchka", 3000, 150)
m4 = Mahsulot("o'yinqaroq", 15000, 50)
m5 = Mahsulot("kompyuter", 500000, 10)

mahsulotlar = [m1.dict(), m2.dict(), m3.dict(), m4.dict(), m5.dict()]

with open("mahsulotlar2.json", "w", encoding="utf-8") as file:
    json.dump(mahsulotlar, file, indent=4, ensure_ascii=False)

with open("mahsulotlar2.json", "r", encoding="utf-8") as file:
    copy = [mahsulot for mahsulot in json.load(file)]
    print(copy)