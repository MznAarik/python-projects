import mysql.connector

# Establish connection to the database
dbconnector = mysql.connector.connect(host="localhost", user="root", password="mysql", db="pycrud")
mysqlcursor = dbconnector.cursor()
# mysqlcursor.execute("Create table studentrecord(rollno INT, name VARCHAR(30), marks INT)")

# Function to create a new record
def create_record():
    try:
        rollno = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        marks = int(input("Enter Marks: "))
        mysqlcursor.execute("INSERT INTO studentrecord (rollno, name, marks) VALUES (%s, %s, %s)", (rollno, name, marks))
        dbconnector.commit()
        print("Record inserted successfully!")
    except Exception as e:
        print(f"Error: {e}")
        dbconnector.rollback()
    
# Function to read records
def read_records():
    try:
        mysqlcursor.execute("SELECT * FROM studentrecord")
        result = mysqlcursor.fetchall()
        for row in result:
            roll, name, marks = row
            print(f"Roll No: {roll}, Name: {name}, Marks: {marks}")
    except Exception as e:
        print(f"Error: {e}")

# Updating records
def update_record():
    try:
        rollno = int(input("Enter Roll Number of the record to update: "))
        name = input("Enter new Name: ")
        marks = int(input("Enter new Marks: "))
        mysqlcursor.execute("UPDATE studentrecord SET name=%s, marks=%s WHERE rollno=%s", (name, marks, rollno))
        dbconnector.commit()
        print("Record updated successfully!")
    except Exception as e:
        print(f"Error: {e}")
        dbconnector.rollback()
    
# Delete record
def delete_record():
    try:
        rollno = int(input("Enter the roll number of the student to delete: "))
        mysqlcursor.execute("DELETE FROM studentrecord WHERE rollno=%s", (rollno,))
        dbconnector.commit()
        print("Record deleted successfully!")
    except Exception as e:
        print(f"Error: {e}")
        dbconnector.rollback()

while True:
    print("\nChoose an option:")
    print("1: Create")
    print("2: Read")
    print("3: Update")
    print("4: Delete")
    print("5: Exit")
    
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        create_record()
    elif choice == 2:
        read_records()
    elif choice == 3:
        update_record()
    elif choice == 4:
        delete_record()
    elif choice == 5:
        break
    else:
        print("INVALID! Select a valid option.")

mysqlcursor.close()
dbconnector.close()
