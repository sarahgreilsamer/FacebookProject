
def read_in_lines(file, number_students):
    text_file = open(file, "r")
    lines = text_file.read().split('\n')
    students = []

    for i in range (number_students):
        new_student = [0] * number_students
        students.append(new_student)

    for i in range (len(lines) - 1):
        first =(int(((lines[i]).split(' '))[0]) -1)
        second =( int(((lines[i]).split(' '))[1]) -1 )
        students[first][second] = 1

    #test
    #print the first student's array of friend links
    print (students[0])
    #first student is friends with the fifth student
    print(students[0][4])
    #therefore fifth student is friends with the first student
    print(students[4][0])

def main():
    read_in_lines("caltech.txt", 770)

if __name__ == "__main__":
    main()