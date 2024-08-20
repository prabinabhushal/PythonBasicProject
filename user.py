import sqlite3
import csv

#git config --global user.name "Prabina Bhushal"
 #git config --global user.email "bhushalprabina@gmail.com"
 #create acc in github
 #git init
 #git status
 #git add .
 #git status
 #git commit -m "Add python project"
 #git status

 ##copy paste from github 3 line
 #git remote add origin https://github.com/prabinabhushal/PythonBasicProject.git
#git branch -M main
#git push -u origin main

###after changing any file
#git status # checks what happened in the file
#git add .
#git commit -m "Your commit message"
#git push origin 

def create_connection():
    try:
        conn = sqlite3.connect("users.sqlite")
        return conn
    except Exception as e:
        print(f"Error:,{e}")

INPUT_STRING = """
Enter the option:
    1. Create the TABLE
    2. DUMP users from csv INTO users TABLE
    3. ADD new user into users TABLE
    4. QUERY all users from TABLE
    5. QUERY user by id from TABLE
    6. QUERY specified no. of records from TABLE
    7. DELETE all users
    8. DELETE user by id
    9. UPDATE user
    10.Press any key to EXIT 
"""


def create_tables(conn):
    CREATE_USER_TABLES_QUERY = """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name CHAR(255) NOT NULL,
            last_name CHAR(255) NOT NULL,                   
            company_name CHAR(255) NOT NULL,
            address CHAR(255) NOT NULL,           
            city CHAR(255) NOT NULL,
            county CHAR(255) NOT NULL,
            state CHAR(255) NOT NULL,
            zip REAL NOT NULL,
            phone1 CHAR(255) NOT NULL,
            phone2 CHAR(255) NOT NULL,
            email CHAR(255) NOT NULL,
            web text
        );

    """
    cur = conn.cursor()
    cur.execute(CREATE_USER_TABLES_QUERY)
    print("user table was created successfully.")

def read_csv():  #csv bata read gaarera sabai name data lyani 
    users=[]  #list ma xa tuple ma rakhni
    with open("sample_users.csv","r")as f:
        data = csv.reader(f)
        for user in data:
            users.append(tuple(user))
    #print(users)
    return users[1:]
            
def insert_users(con,users):
    user_add_query = """
        INSERT INTO users(
            first_name,
            last_name,
            company_name,
            address,
            city,
            county,
            state,
            zip,
            phone1,
            phone2,
            email,
            web
            
        )
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
    """
    cur=con.cursor()
    cur.executemany(user_add_query, users)

    con.commit()
    print(f"{len(users)} users were imported successfully.")

#4 ko query 
def select_users(con):  #main bata connection gareko
    cur = con.cursor()
    users = cur.execute("SELECT * FROM users")  #query execute garna
    for user in users:  #loop lagaudai value herna milxa
        print(user)

#5
def select_user_by_id(con,user_id):
    cur = con.cursor()
    users = cur.execute("SELECT * FROM users where id=?;",(user_id,))  #query execute garna
    for user in users:  #loop lagaudai value herna milxa
        print(user)


#6
def select_users(con,no_of_users=0):  
    cur = con.cursor()
    if no_of_users:
        users = cur.execute("SELECT * FROM users LIMIT ?;",(no_of_users,))  
    else:
        users = cur.execute("SELECT * FROM users")
    for user in users:  
        print(user)


#7
def delete_users(con):
    cur=con.cursor()
    cur.execute("DELETE FROM USERS ;")
    con.commit()
    print("All users were delected successfully")


#8
def delete_user_by_id(con, user_id):
    cur=con.cursor()
    cur.execute("DELETE FROM USERS where id =?",(user_id,))
    con.commit()
    print(f"User with id[{user_id}] was successfully deleted.")


#3
COLUMNS=(
    "first_name",
    "last_name",
    "company_name",
    "address",
    "city",
    "county",
    "state",
    "zip",
    "phone1",
    "phone2",
    "email",
    "web",  #comma opitional yesma matra

)

#9
def update_user_by_id(con,user_id,column_name,column_value):
    update_query=f"UPDATE users set {column_name}=? where id=?;"
    cur=con.cursor()
    cur.execute(update_query,(column_value,user_id))
    con.commit()
    print(f"[{column_name}] was updated with value[{column_value}] of user with id [{user_id}]")


def main():
    con = create_connection()
    user_input = input(INPUT_STRING)
    if user_input == "1":
        create_tables(con)
    elif user_input=="2":
        users = read_csv()
        insert_users(con,users)

    elif user_input=="3":
        data=[]
        for column in COLUMNS:
            column_value=input(f"Enter the value of {column}:")
            data.append(column_value)
        insert_users(con,[tuple(data)])
       
    elif user_input=="4":
        select_users(con)
    elif user_input=="5":
        user_id=input("Enter user id:")
        if user_id.isnumeric():
            select_user_by_id(con,user_id)

    elif user_input=="6":
        no_of_users =input("Enter the no of users to fetch:")
        if no_of_users.isnumeric() and int(no_of_users)>0:
            select_users(con,no_of_users=int(no_of_users))

        
    elif user_input=="7":
        confirm = input("Are you sure u want to delete all users?(y/n):")
        if confirm=="y":
            delete_users(con)


    elif user_input=="8":
        user_id = input("Enter the user id")
        if user_id.isnumeric():
            delete_user_by_id(con,user_id)


    elif user_input=="9":
        user_id =input("Enter id of users:")
        if user_id.isnumeric():
            column_name= input(
                f"Enter the column you want to edit.Please make sure column is with in {COLOMNS}"
            )
            if column_name in COLOMNS:
                column_value=input(f"Enter the value of{column_name}:")
                update_user_by_id(con,user_id,column_name,column_value)
        else:
            exit()
            
        

    elif user_input=="10":
        pass



main()










