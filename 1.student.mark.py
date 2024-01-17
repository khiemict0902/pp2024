def inputNumberOfStudent():
    while (True):
        try:
            tmp = int(input("Enter number of student in the class: "))
            if tmp<=0:
                print("The number must be positive, Input again!")
            else:
                return tmp
        except:
            print("It's not a number, try again!")

def inputStudentInfo(numStudent,item):
    if (numStudent==0):
        print("There are no student in the class. Please input number of student first!")
        return
    for _ in range(numStudent):
        id = input("Input student id: ")
        name = input("Input name: ")
        dob = input("Date of Birth: ")
        st={"id":id,
            "name":name,
            "dob":dob}
        item.append(st)
    print(item)

def inputNumberOfCouse():
    while (True):
        try:
            tmp = int(input("Enter number of courses: "))
            if tmp<=0:
                print("The number must be positive, Input again!")
            else:
                return tmp
        except:
            print("It's not a number, try again!")

def inputCourseInfo(numCourse,item):
    if (numCourse==0):
        print("There are no course!")
        return
    for i in range(numCourse):
        id = input("Input course id: ")
        name = input("Input name: ")
        c={"id":id,
            "name":name}
        item.append(c)
    print(item)

def listCourses(courses):
    if not courses:
        print("There aren't any courses yet")
        return 

    print("Here is the course list: ")
    for i in range(len(courses)):
        print(f"{i+1}. {courses[i]['id']} - {courses[i]['name']}")    

def listStudents(students):
    if not students:
        print("There aren't any students yet")
        return

    print("Here is the student list: ")
    for i in range(len(students)):
        print(f"{i+1}. {students[i]['id']} - {students[i]['name']} - {students[i]['dob']}")

def inputMark(students,courses):    
    if not courses:
        print("There aren't any courses yet")
        return
    if not students:
        print("There aren't any student yet")
        return
    while True:
        try:
            listCourses(courses)
            optionCourse = int(input("Choose the courses (0 for exit): "))
            if optionCourse == 0:
                break
            elif optionCourse > len(courses):
                print("Invalid input, try again")
            else:
                while True:
                    try:
                        listStudents(students)
                        optionStudent = int(input("Choose the student (0 for turn back): "))
                        if optionStudent == 0:
                            break
                        elif optionStudent > len(students):
                            print("Invalid input, try again")
                        else:
                            if 'marks' not in courses[optionCourse - 1]:
                                courses[optionCourse - 1]['marks'] = []
                            midterm = input("Input midterm mark: ")
                            final = input("Input final mark: ")
                            marks = {
                                "studentId": students[optionStudent-1]['id'],
                                "studentName": students[optionStudent-1]['name'],
                                "midterm": midterm,
                                "final": final,
                                "total": 0.4*float(midterm)+0.6*float(final)
                            }
                            courses[optionCourse - 1]['marks'].append(marks)
                        
                    except:
                        print("Invalid input, try again!")
        except:
            print("Invalid input, try again!")

def printMark(courses):
    while True:
        try:
            listCourses(courses)
            optionCourse = int(input("Choose the courses (0 for exit): "))
            if optionCourse == 0:
                break
            elif optionCourse > len(courses):
                    print("Invalid input, try again")
            else:
                course = courses[optionCourse-1]
                if 'marks' in course:
                    print(f"Course: {course['id']} - {course['name']}:")
                    for mark in course['marks']:
                        print(f"    Student: {mark['studentName']} - Midterm: {mark['midterm']} - Final: {mark['final']} - Total: {mark['total']}")
                else:
                    print("No mark in this course yet.")
        except:
            print("Invalid input, try again!")

def main():
    courses = []
    students = []
    numStudent = 0
    numCourse = 0

    while(True):
        print("""
    0. Exit
    1. Input number of students
    2. Input student information
    3. Input number of courses
    4. Input course information
    5. Seclect a course, input mark
    6. List courses
    7. List student
    8. Show student marks 
    """)
        try:
            option = int(input("your choice: "))                                                         
            if option == 0:
                break
            elif option == 1:                                                                          
                numStudent = inputNumberOfStudent()
            elif option == 2:                                                   
                inputStudentInfo(numStudent,students)
            elif option == 3:
                numCourse = inputNumberOfCouse()
            elif option == 4:
                inputCourseInfo(numCourse,courses)
            elif option == 5:
                inputMark(students,courses)
            elif option == 6:
                listCourses(courses)
            elif option == 7:
                listStudents(students)
            elif option == 8:
                printMark(courses)
            else:
                print("Invalid input. Please try again!")
        except:
            print("Invalid input. Please try again!")            

if __name__ == "__main__":
    main()
