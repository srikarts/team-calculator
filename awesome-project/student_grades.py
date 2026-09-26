from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    id : int
    name : str
    subject : str
    grade : int

class StudentCreate(BaseModel):
    name: str
    subject: str
    grade: int

students = [
    Student(id=1, name='Alice', subject='Math', grade=92),
    Student(id=2, name='Bob', subject='Science', grade=78),
    Student(id=3, name='Charlie', subject='Math', grade=85),
    Student(id=4, name='Diana', subject='English', grade=95),
    Student(id=5, name='Eve', subject='Science', grade=88),
]

@app.get('/students/', status_code=status.HTTP_201_CREATED)
def show_students(subject:str = None, grade:int=None):
    if subject and grade:
        return [student for student in students if student.subject.lower()==subject.lower() and student.grade>=grade]
    elif subject:
        return [student for student in students if student.subject.lower()==subject.lower()]
    elif grade:
        return [student for student in students if student.grade>=grade]
    return students

@app.get('/students/{student_id}')
def show_student(id:int):
    for student in students:
        if student.id == id:
            return student
    raise HTTPException(status_code=404, detail=f"Student with {student_id} not found!")

@app.post('/students/')
def create_student(student: StudentCreate):
    new_id = max((s.id for s in students),default=0)+1
    new_student = Student(id=new_id, **student.dict())
    students.append(new_student)
    return new_student  

@app.get('/top-student/')
def top_student():
    max_grade = max([s.grade for s in students])
    return [student for student in students if student.grade == max_grade]


@app.put('/students/{student_id}')
def update_student(student_id:int,stu_update:StudentCreate):
    for i,student in enumerate(students):
        if student.id == id:
            updated_student = Student(id=id, **stu_update.dict())
            students[i] = updated_student
            return updated_student
    
    raise HTTPException(status_code=404, detail=f"Student with id {id} not found!")


@app.delete('/students/{student_id}')
def delete_student(student_id:int):
    for student in students:
        if student.id == stu_id:
            students.remove(student)
            return {"Student Deleted Successfully"}
    raise HTTPException(status_code=404, detail=f"Student with id {stu_id} not found")
        




