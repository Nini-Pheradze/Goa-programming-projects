#Dictionary მოსწავლეთა სახელებისა და მათი ქულების შესანახად
students = {
    "ნიკა ჯავახიშვილი": "95",
    "მარიამ გოგოლაძე" : "88",
    "გიორგი ჯუღელი" : "76",
    "ელენე თათარიძე" : "92",
    "საბა დოლიძე" : "81",
    "თამარ შაინიძე" : "89",
    "ალექსანდრე ქავთარაძე" : "85",
    "სალომე ლობჟანიძე" : "93",
    "დავით აბრამიშვილი" : "78",
    "ანი სიდამონიძე" : "84"
}

#ფუნქცია სტუდენტის დამატებისთვის
def add_student(name, grade):
    students[name] = grade  # ვამატებთ სტუდენტის სახელს და ქულას
    print(f"სტუდენტი {name} წარმატებით დაემატა!")


#ფუნქცია ყველა სტუდენტის ჩვენებისთვის
def display_students():
    if not students:
        print("სტუდენტთა სია ცარიელია.")
        return
    print("სტუდენტთა სია:")
    for name, grade in students.items():
        print(f"{name}: {grade}")

#ფუნქცია უმაღლესი და დაბალი ქულის საპოვნელად
def find_highest_lowest():
    if not students:
        print("სტუდენტთა სია ცარიელია.")
        return
highest = max(students.values())
lowest = min(students.values())
high_students = [name for name, grade in students.items() if grade == highest]
low_students = [name for name, grade in students.items() if grade == lowest]


print(f"უმაღლესი ქულა ({highest}) მიეკუთვნება: {', '.join(high_students)}")
print(f"დაბალი ქულა ({lowest}) მიეკუთვნება: {', '.join(low_students)}")


# პროგრამის მთავარი ციკლი
while True:
    print("1. დაამატე სტუდენტი")
    print("2. სტუდენტთა სიის ჩვენება")
    print("3. უმაღლესი და დაბალი ქულების ჩვენება")
    print("4. გამოსვლა")

    choice = input("აირჩიეთ ოფცია (1-6): ")

    if choice == '1':
        name = input("შეიყვანეთ სტუდენტის სახელი: ")
        try:
            grade = float(input("შეიყვანეთ სტუდენტის ქულა (0-100): "))
            if 0 <= grade <= 100:
                add_student(name, grade)
            else:
                print("შეიყვანეთ ქულა 0-დან 100-ის ფარგლებში.")
        except ValueError:
            print("გთხოვთ, შეიყვანოთ სწორი რიცხვი.")

    elif choice == '2':
        display_students()

    elif choice == '3':
        find_highest_lowest()

    elif choice == '4':
        print("პროგრამა დასრულდა.")
        break

    else:
        print("არასწორი არჩევანი, სცადეთ კიდევ ერთხელ.")