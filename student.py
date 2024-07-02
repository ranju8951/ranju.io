class Student:
    def __init__(self, name, reg_no, marks1, marks2, marks3):
        self.name = name
        self.reg_no = reg_no
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        self.average = self.calculate_average()

    def calculate_average(self):
        return (self.marks1 + self.marks2 + self.marks3) / 3

def get_student_details():
    name = input("Enter name: ")
    reg_no = input("Enter register number: ")
    marks1 = int(input("Enter marks for subject 1: "))
    marks2 = int(input("Enter marks for subject 2: "))
    marks3 = int(input("Enter marks for subject 3: "))
    return Student(name, reg_no, marks1, marks2, marks3)

def main():
    num_students = int(input("Enter the number of students: "))
    students = [get_student_details() for i in range(num_students)]
    students.sort(key=lambda student: student.average, reverse=True)

    print("\nStudents in rank order:")
    for rank, student in enumerate(students, start=1):
        print("Rank {}: {}, Reg No: {}, Average Marks: {:.2f}".format(rank, student.name, student.reg_no, student.average))

if __name__ == "__main__":
    main()



   
            
