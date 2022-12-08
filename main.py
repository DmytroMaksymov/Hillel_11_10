import sqlite3
from faker import Faker

fake = Faker()

con = sqlite3.connect('hw2.db')
cur = con.cursor()
sql_command = '''CREATE TABLE IF NOT EXISTS person(
personid INTEGER PRIMARY KEY AUTOINCREMENT,
first_name VARCHAR(128),
last_name VARCHAR(128),
address VARCHAR(1024) ,
job VARCHAR(128),
age INTEGER)'''
cur.execute(sql_command)


def insert_data():
    for i in range(15):
        fake_fn = fake.first_name()
        fake_ln = fake.last_name()
        fake_adr = fake.address()
        fake_work = fake.job()
        fake_age = fake.pyint(1, 99)

        sql = f'''INSERT INTO person (first_name, last_name, address, job, age) 
        VALUES ('{fake_fn}','{fake_ln}', '{fake_adr}', '{fake_work}', '{fake_age}')'''
        cur.execute(sql)
        con.commit()


def select_data():
    sql = '''SELECT * FROM person'''
    rows = cur.execute(sql)
    for row in rows:
        print(row)


def update_data():
    numbers = '''SELECT personid FROM person'''
    user_choice = input('Select id to update - ')

    if user_choice in numbers:
        name = input('Input new name - ')
        surname = input('Input new surname - ')
        address = input('Input new address - ')
        job = input('Input new job - ')
        age = input('Input new age - ')

        cur.execute(
                f"UPDATE person SET first_name = ?, last_name = ?,"
                f"address = ?, job = ?, age =?"
                f"WHERE personid = ?",
                (name, surname, address, job, age,
                 user_choice))
        print('Successful updated!')
    else:
        print('Wrong id!')

    con.commit()


def delete_data():

    user_choice = int(input('Select id to delete - '))
    cur.execute(f"DELETE FROM person WHERE personid = '{user_choice}'")
    print('Successful deleted!')

    con.commit()


if __name__ == 'main':
    insert_data()
    select_data()
    update_data()
    select_data()
    delete_data()
    select_data()
