import os
import getpass
from datetime import date

# Set up access to PostgreSQL libraries on Windows
pg_dll_directory = None

if os.name == "nt":
    pg_bin = r"C:\Program Files\PostgreSQL\18\bin"
    if os.path.isdir(pg_bin):
        pg_dll_directory = os.add_dll_directory(pg_bin)

import psycopg


# database connection information
DB_NAME = "COMP3005_A3"
DB_USER = "postgres"
DB_HOST = "localhost"
DB_PORT = 5432

db_password = None


# Connect to the PostgreSQL database
def get_connection():
    return psycopg.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=db_password,
        host=DB_HOST,
        port=DB_PORT
    )


# Retrieve and display all student records
def getAllStudents():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM students ORDER BY student_id;"
            )
            students = cur.fetchall()

            print("\nAll Students:")
            for student in students:
                print(student)

# Add a new student
def addStudent(first_name, last_name, email, enrollment_date):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO students
                (first_name, last_name, email, enrollment_date)
                VALUES (%s, %s, %s, %s)
                RETURNING student_id;
                """,
                (first_name, last_name, email, enrollment_date)
            )
            student_id = cur.fetchone()[0]

    print(f"Student added successfully. ID: {student_id}")
    return student_id


# update a student's email using their student ID
def updateStudentEmail(student_id, new_email):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE students
                SET email = %s
                WHERE student_id = %s;
                """,
                (new_email, student_id)
            )
            updated = cur.rowcount

    print(f"Students updated: {updated}")


# Delete a student using their student ID
def deleteStudent(student_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM students
                WHERE student_id = %s;
                """,
                (student_id,)
            )
            deleted = cur.rowcount

    print(f"Students deleted: {deleted}")

# Display the menu and run the selected function
def main():
    global db_password

    db_password = getpass.getpass(
        "Enter your PostgreSQL postgres password: "
    )

    while True:
        print("\nStudent Management System")
        print("1. Get all students")
        print("2. Add student")
        print("3. Update student email")
        print("4. Delete student")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()

        try:
            if choice == "1":
                getAllStudents()

            elif choice == "2":
                first_name = input("First name: ")
                last_name = input("Last name: ")
                email = input("Email: ")
                enrollment_date = input(
                    "Enrollment date (YYYY-MM-DD): "
                )

                # Validate the supplied date.
                date.fromisoformat(enrollment_date)

                addStudent(
                    first_name,
                    last_name,
                    email,
                    enrollment_date
                )

            elif choice == "3":
                student_id = int(input("Student ID: "))
                new_email = input("New email: ")

                updateStudentEmail(student_id, new_email)

            elif choice == "4":
                student_id = int(input("Student ID: "))
                deleteStudent(student_id)

            elif choice == "5":
                print("Exiting program.")
                break

            else:
                print("Invalid choice. Try again.")

        except (ValueError, psycopg.Error) as error:
            print("Error:", error)


if __name__ == "__main__":
    main()