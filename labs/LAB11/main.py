import psycopg2
import csv


conn = psycopg2.connect(
    database = "LAB10",
    user = "postgres",
    password = "12345678",
    host = "localhost",
    port = "5432"
)

cur = conn.cursor()


def insert_from_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    print("📥 CSV деректері қосылды.")


def insert_from_input():
    name = input("Атыңызды енгізіңіз: ")
    phone = input("Телефон нөмірі: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))


    conn.commit()
    print("✅ Жаңа контакт қосылды.")


def update_contact():
    contact_id = input("Қай ID жаңартасың? ")
    new_name = input("Жаңа аты: ")
    new_phone = input("Жаңа телефон: ")
    cur.execute("UPDATE phonebook SET name = %s, phone = %s WHERE id = %s", (new_name, new_phone, contact_id))

    conn.commit()
    print("♻️ Контакт жаңартылды.")


def query_with_filter():
    keyword = input("Аты не номер бойынша ізде: ")
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s", (f'%{keyword}%', f'%{keyword}%'))
    rows = cur.fetchall()
    for row in rows:
        print(row)


def delete_contact():
    contact_id = input("қай ID өшіргің келеід? ")
    cur.execute("DELETE FROM phonebook WHERE id = %s", (contact_id))
    conn.commit()
    print("❌ Контакт өшірілді.")


def menu():
    run = True
    while run:
        print("\n PHONEBOOK MENU:")
        print("1 - insert from csv")
        print("2 - insert from input")
        print("3 - update contact")
        print("4 - query with filter")
        print("5 - delete contact")
        print("6 - quit")

        choice = input("Тандаңыз (1-6): ")

        if choice == '1':
            insert_from_csv("C:/Users/HUAWEI/Desktop/All labs/labs/LAB10/datas.csv") 

        elif choice == '2':
            insert_from_input()

        elif choice == '3':
            update_contact()
        elif choice == '4':
            query_with_filter()
        elif choice == '5':
            delete_contact()
        elif choice == "6":
            run = False
        else:
            print("❗ Қате таңдау.")
        
menu()
cur.close()
conn.close()