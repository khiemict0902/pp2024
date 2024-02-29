class Object():
    def __init__(self, id: int, name: str):
        self._id = id 
        self._name = name
    
    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def print(self):
        print(f"{self._id} - {self._name}")

class Student(Object):
    def __init__(self, id: int, name: str, dob: str):
        super().__init__(id, name)
        self._dob = dob 

    def getDob(self):
        return self._dob

    def print(self):
        print(f"{self._id} - {self._name} - {self._dob}")

class Course(Object):
    pass

class Mark(object):
    def __init__(self,courseId: int, studentId: int, mark: float):
        self._courseId = courseId
        self._studentId = studentId
        self._mark = mark

    def getCourseId(self):
        return self._courseId

    def getStudentId(self):
        return self._studentId

    def getMark(self):
        return self._mark

studentList = []
courseList = []
markList = []

def inputStudent(studentList):
    while True:
        try:
            numStudent = int(input("Enter the number of Student: "))
            if numStudent <= 0:
                print("must be positive")
            else:
                break
        except:
            print("It's must be interger")
    
    for _ in range(numStudent):
        id = int(input("Id: "))
        name = str(input("Name: "))
        dob = str(input("DoB: "))
        s = Student(id,name,dob)
        studentList.append(s)

def listStudent(studentList):
    for student in studentList:
        student.print()

def inputCourse(courseList):
    while True:
        try:
            numC = int(input("Enter the number of Course: "))
            if numC <= 0:
                print("must be positive")
            else:
                break
        except:
            print("It's must be interger")
    
    for _ in range(numC):
        id = int(input("Id: "))
        name = str(input("Name: "))
        c = Course(id,name)
        courseList.append(c)

def listCourse(courseList):
    for c in courseList:
        c.print()

def inputMark(markList, studentList, courseList):
    if not courseList:
        print("There aren't any courses yet")
        return
    if not studentList:
        print("There aren't any student yet")
        return

    while True:
        listCourse(courseList)
        optionC = int(input("Choose the course (0 for exit)"))
        if optionC == 0:
            break
        elif optionC > len(courseList):
            print("Invalid input")
        else:
            while True:
                listStudent(studentList)    
                optionS = int(input("Choose the student (0 for exit)"))
                if optionS == 0:
                    break
                elif optionS > len(studentList):
                    print("Invalid")
                else:
                    m = float(input("Input mark"))
                    mark = Mark(optionC-1,optionS-1,m)
                    markList.append(mark)

def listMark(markList, courseList, studentList):
    while True:
        listCourse(courseList)
        print("choose the couse (0 for exit)")
        optionC = int(input())
        if optionC == 0:
            break
        elif optionC > len(courseList):
            print("Invalid")
        else:
            for m in markList:
                if m.getCourseId() == optionC-1:
                    s = m.getStudentId()
                    sl = studentList[s]
                    print(f"{sl.getId()} - {sl.getName()} - {sl.getDob()} - {m.getMark()}")

    


def main():
    while True:
        print("""
        0. Exit
        1. Input students
        2. List students
        3. Input courses
        4. List courses
        5. Seclect a course, input mark
        6. List Marks
        """)
        option = int(input("Choice: "))
        if option == 0:
            break
        elif option == 1:
            inputStudent(studentList)
        elif option == 2:
            listStudent(studentList)
        elif option == 3:
            inputCourse(courseList)
        elif option == 4:
            listCourse(courseList)
        elif option == 5:
            inputMark(markList,studentList,courseList)
        elif option == 6:
            listMark(markList,courseList,studentList)

if __name__ == "__main__":
    main()
