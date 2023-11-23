### Video:
Video may be found at the link https://youtu.be/awY2zE0CnnY

### How to set up the databasae:

  Firstly, make sure that the PostgreSQL service is running on your computer   

  Create a new database titled 'A4', which will contain the students table

  Code to create the table:

    CREATE TABLE students (
      student_id SERIAL PRIMARY KEY,
      first_name VARCHAR(255) NOT NULL,
      last_name VARCHAR(255) NOT NULL,
      email VARCHAR(255) NOT NULL UNIQUE,
      enrollment_date DATE
    )

  Open the query tool on the A4 database and paste the above code into it, then execute.

  #### Code to insert the initial data:

    INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
    ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

  With the query tool still open, populate the students table by executing the above code


#### To run the application application.py:
  python application.py

As you can see in the video, uncommenting the different function calls in main will allow the different functions to be tested.

### Explanation of each function:

```
def getAllStudents()
```
  This function should select all rows from the 'students' table, and then iterate over all options, printing each row through each iteration.

---

```
def addStudent(first_name, last_name, email, enrollment_date)
```
  Adds a student with the parameters passed into the students table.

---

```
def updateStudentEmail(student_id, new_email)
```
  Using the passed student_id argument, a specific student's email shall be overwritten with the new_email parameter.

---

```
def deleteStudent(student_id)
```
  Removes a student completely from the table where the student_id matches the one passed into the function.

---

```
def main()
```
  Used to call the database functions from.
