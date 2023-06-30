from flask import Flask, render_template, request
import csv

app = Flask(__name__)

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

def load_students_from_csv(file_path):
    students = []
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Name']
            age = int(row['Age'])
            grade = row['Grade']
            students.append(Student(name, age, grade))
    return students

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_student_info', methods=['POST'])
def get_student_info():
    student_name = request.form['name']
    student_info = "Student not found."
    
    for student in students:
        if student.name.lower() == student_name.lower():
            student_info = f"Name: {student.name}\nAge: {student.age}\nGrade: {student.grade}"
            break
    
    return render_template('index.html', student_info=student_info)

# Load student data from CSV file
student_data_file = "student_data.csv"
students = load_students_from_csv(student_data_file)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0' ,port=8080)
