# COMP3005 - Assignment 3 - PostgreSQL Student Management
Name - Aneela Sharmeen

Student No. - 101277820

This program connects to a PostgreSQL database using Python and allows student records to be viewed, added, updated, and deleted

## Files

1. main.py - Contains the Python code for connecting to the database and running the functions
2. database.sql - Creates the students table and inserts the three starting records
3. README.md - Instructions for setting up and running the program.

## Setup

1. Install Python and PostgreSQL
2. Install psycopg by running python -m pip install psycopg.
3. Open pgAdmin and create a database called COMP3005_A3.
4. Open the Query Tool for that database and run database.sql.
5. Open the project folder in VS Code.
6. Run python main.py in the terminal.
7. Enter the PostgreSQL password when asked.

The program uses the local PostgreSQL server on port 5432. On my Windows setup, PostgreSQL 18 is installed in C:\Program Files\PostgreSQL\18.

## Functions

1. getAllStudents() - Displays all students in the database
2. addStudent() - Adds a student with their name, email, and enrollment date
3. updateStudentEmail() - Changes a student's email using their ID
4. deleteStudent() - Removes a student using their ID.

The program runs each function in order to demonstrate that they work. It starts by displaying the three students, adds Alice Johnson, updates her email, and then deletes her record

## Demo Video
[Watch my demonstration video: ]https://drive.google.com/file/d/1FvQXc1uJCY9IOSDDm4uPIKrnUQURoinn/view?usp=sharing
