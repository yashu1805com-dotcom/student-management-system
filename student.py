class Student:
    def __init__(self,student_id,name,age,course):
        self.student_id=student_id
        self.name=name
        self.age=age
        self.course=course
    def display_info(self):
        print(f"Student id:{self.student_id}")
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Course:{self.course}")
class StudentManagement:
    def __init__(self):
        self.students=[]
    def add_student(self):
        student_id=input("Enter the student id: ")
        name=input("Enter the student name: ")
        age=int(input("Enter the student age: "))
        course=input("Enter the student course: ")
        obj=Student(student_id,name,age,course)
        self.students.append(obj)
    def display_students(self):
        for stud in self.students:
            stud.display_info()
    def search_student(self):
        std_id=input("Enter the student id to search: ")
        found=False
        for Sid in self.students:
            if std_id== Sid.student_id:
                Sid.display_info()
                found=True
        if not found:
            print("Student not found")
    def update_student(self):
        upd_id=input("Enter the id to update the details: ")
        found=False
        for u_id in self.students:
            if upd_id==u_id.student_id:
                name=input("Enter the name: ")
                age=int(input("Enter the age: "))
                course=input("Enter the course: ")
                u_id.name=name
                u_id.age=age
                u_id.course=course
                u_id.display_info()
                found=True
                break
        if not found:
            print("Student not found")
    def delete_student(self):
        d_id=input("Enter the student id to delete:")
        found=False
        for dl in self.students:
            if d_id==dl.student_id:
                self.students.remove(dl)
                print("student deleted")
                found=True
                break
        if not found:
            print("Student not found")
system=StudentManagement()
while True:
    print("1. Add Student\n2. Display Student\n3. Search Student\n4. Update Student\n5. Delete Student\n6. Exit\n")
    try:
        choice=int(input("Enter your choice: "))
    except ValueError:
        print("Enter valid choice")
        continue
    if choice==1:
        system.add_student()
    elif choice==2:
        system.display_students()
    elif choice==3:
        system.search_student()
    elif choice==4:
        system.update_student()
    elif choice==5:
        system.delete_student()
    elif choice==6:
        print("Exit")
        break
    else:
        print("Invalid choice")