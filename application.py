# Created by Will Chartrand 101229796

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="A4",
    user="postgres",
    password="student")

curr = conn.cursor()


def getAllStudents():
    sql = """SELECT * FROM students;"""
    curr.execute(sql)
    conn.commit()

    print("All students:")
    for x in curr.fetchall():
        print(x);


def addStudent(first_name, last_name, email, enrollment_date):
    sql = """INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);"""
    curr.execute(sql, (first_name, last_name, email, enrollment_date,))
    conn.commit()

def updateStudentEmail(student_id, new_email):
    sql = """UPDATE students SET email = %s WHERE student_id = %s"""
    curr.execute(sql, (new_email, student_id))
    conn.commit()

def deleteStudent(student_id):
    sql = """DELETE FROM students WHERE student_id = %s"""
    curr.execute(sql, (student_id,))
    conn.commit()

def main():
    
    #getAllStudents()
    #addStudent("Will", "Chartrand", "willchartrand@example.com", "2000-10-10")
    #updateStudentEmail(2, "newTestEmail@example.com")
    deleteStudent(2)

if __name__ == "__main__":
    main()
