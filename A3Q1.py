import psycopg2
import datetime

connection = "host = 'localhost' \
dbname = '3005A3' user = 'postgres' \
password = 'password'"

connect = psycopg2.connect(connection)

# This line is so that you can still use other queries after a failed query
connect.autocommit = True
cursor = connect.cursor()

# Gets all students, printing them each on a seperate line
def getAllStudents():
    sql = 'SELECT * FROM students'
    print (sql)
    cursor.execute(sql)
    students = cursor.fetchall()
    for student in students:
        print(student)

# Add student with following parameters
def addStudent(first_name, last_name, email, enrollment_date):
    sql = ''' INSERT INTO students(first_name, last_name, email, enrollment_date) 
    VALUES (%s, %s, %s, %s)'''
    record = (first_name, last_name, email, enrollment_date)
    cursor.execute(sql, record)
    print (sql)

# Update student email for student with id student_id
def updateStudentEmail(student_id, new_email):
    sql = ''' UPDATE students 
    SET email = %s
    WHERE student_id = %s'''
    record = (new_email, student_id)

    cursor.execute(sql, record)
    print (sql, record)
    
# Delete student with id student_id
def deleteStudent(student_id):
    sql = ''' DELETE FROM students WHERE student_id = %s'''

    cursor.execute(sql, student_id)
    print (sql, student_id)
    

def main():

    # Initially printing all options
    print("Options: ")
    print("1) Get all students")
    print("2) Add student")
    print("3) Update student email")
    print("4) Delete student")
    ans = input("Enter the option you would like to select (-1 to exit): ")

    # Loops until user does not want to continue
    while (ans != "-1"):

        # Choosing get all students
        if (ans == "1"):
            try:
                getAllStudents()
            except psycopg2.Error as error:
                print(error)
        
        # Choosing to add a student and the user inputs the requested parameters
        elif (ans == "2"):
            fName = input("Enter the first name of the new student: ")
            lName = input("Enter the last name of the new student: ")
            email = input("Enter the email of the new student: ")
            enrollmentDate = input("Enter the enrollment date of the new student (YYYY-MM-DD): ")
            try:
                addStudent(fName, lName, email, enrollmentDate)
            except psycopg2.Error as error:
                print(error)
        
        # Updating the email for a student with the given id
        elif (ans == "3"):
            student_id = input("Enter the id of the student whose email you would like to update: ")
            email = input("Enter the new email for the student whose email you would like to update: ")
            try:
                updateStudentEmail(student_id, email)
            except psycopg2.Error as error:
                print(error)
        
        # Deleting the student with the given id
        elif (ans == "4"):
            student_id = input("Enter the id of the student you would like to delete: ")
            try:
                deleteStudent(student_id)
            except psycopg2.Error as error:
                print(error)
        
        print()

        print("Options: ")
        print("1) Get all students")
        print("2) Add student")
        print("3) Update student email")
        print("4) Delete student")
        ans = input("Enter the option you would like to select (-1 to exit): ")

    


if __name__ == "__main__":
    main()


