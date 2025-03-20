dict = {
    "Alice": 85,
    "Sam": 79,
    "Dean": 98
}
name = input("Enter the student's name: ")
if dict.keys().__contains__(name) :
    print(name + "'s marks:" , dict[name])
else:
    print("Student not found.")