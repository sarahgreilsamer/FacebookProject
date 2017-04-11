filename_data = "Caltech_A.txt"

# a student object has a list of friend connections, a list of attributes,
# and a number of friends variable
class Student(object):
    def __init__(self, matrix_A, local_info):
        self.edge_array = matrix_A
        self.student_info = local_info
        # find out how many friends the student has
        count = 0
        for possible_edge in self.edge_array:
            if possible_edge == 1:
                count = count + 1
        self.number_friends = count

# reads in a text file with the A matrix
# which is a matrix of the connections between students
# and creates a list, for which every element is a list that represents a student
# and contains their connection data
# a 1 at a given index in that list indicates that a student is friends with the student at that index
# in the enclosing list
def read_in_A_matrix(file, number_students):
    text_file = open(file, "r")
    lines = text_file.read().split('\n')
    student_edges_list = []
    list_of_students = []

    # initialize each student's list of friends to all zeroes
    for i in range (number_students):
        new_student_edges = [0] * number_students
        student_edges_list.append(new_student_edges)

    # then find the indexes at which each student has a connection and set the value at those indexes to 1
    for i in range (len(lines) - 1):
        first =(int(((lines[i]).split(' '))[0]) -1)
        second =( int(((lines[i]).split(' '))[1]) -1 )
        student_edges_list[first][second] = 1

    return student_edges_list


def read_in_local_info(filename, number_students):
    # read in the local info matrix as a list
    with open(filename) as file:
        lines = file.read().splitlines()
    print ("lines: ", lines)

def create_student(edges, attributes):
    return Student(edges, attributes)

def prepare_text(filename_data):
    with open(filename_data) as file:
        text = file.read()
    return text

def create_local(text):
    local = [] #list of all students where each student is a list
    lines = text.splitlines() #should return a list of strings
    for each_line in lines: #for each string in the list of strings append that string
        local.append(each_line.split()) #list of student is a list of lists of strings
    return local

def main():
    # test on caltech data
    A = (read_in_A_matrix(filename_data, 770))
    local = create_local(prepare_text(filename_data))
    students = []

    # print the number of friends each student has
    for i in range(770):
        students.append(create_student(A[i], local[i]))

    for student in students:
        print (student.number_friends)

    print(students)

if __name__ == "__main__":
    main()