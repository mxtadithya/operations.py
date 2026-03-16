courses = {"Python", "Java", "MERN", "Data Science"}

enrollments = [
    (1, "Rahul", "Python"),
    (2, "Meera", "Java")
]

def add_enrollment():
    global enrollments

    student_id = int(input("Enter Student ID: "))

    for e in enrollments:
        if e[0] == student_id:
            print("Student ID already exists.")
            return

    name = input("Enter Student Name: ")
    course = input("Enter Course Name: ")

    
    if course not in courses:
        print("Course does not exist.")
        return


    for e in enrollments:
        if e[0] == student_id and e[2] == course:
            print("Student already enrolled in this course.")
            return

    enrollments.append((student_id, name, course))
    print("Enrollment added successfully")



def view_enrollments():
    if not enrollments:
        print("No enrollments found.")
        return

    print("\nID\tName\tCourse")
    for e in enrollments:
        print(e[0], "\t", e[1], "\t", e[2])


def view_by_course():
    course = input("Enter course name: ")

    if course not in courses:
        print("Course does not exist.")
        return

    print(f"Students enrolled in {course}:")
    found = False
    for e in enrollments:
        if e[2] == course:
            print(e[1])
            found = True

    if not found:
        print("No students enrolled in this course.")



def update_course():
    global enrollments

    student_id = int(input("Enter Student ID: "))
    new_course = input("Enter new course name: ")

    if new_course not in courses:
        print("Course does not exist.")
        return

    for i in range(len(enrollments)):
        if enrollments[i][0] == student_id:
            name = enrollments[i][1]
            enrollments[i] = (student_id, name, new_course)
            print("Course updated successfully")
            return

    print("Student not found.")


def delete_enrollment():
    global enrollments

    student_id = int(input("Enter Student ID: "))

    for e in enrollments:
        if e[0] == student_id:
            enrollments.remove(e)
            print("Enrollment removed successfully")
            return

    print("Student not found.")


while True:
    print("\nCourse Enrollment System")
    print("1. Add Enrollment")
    print("2. View All Enrollments")
    print("3. View Enrollments By Course")
    print("4. Update Course")
    print("5. Delete Enrollment")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_enrollment()
    elif choice == "2":
        view_enrollments()
    elif choice == "3":
        view_by_course()
    elif choice == "4":
        update_course()
    elif choice == "5":
        delete_enrollment()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")