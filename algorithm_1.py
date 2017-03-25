'''Info on data
Each of the school .mat files has an A matrix (sparse) and a
"local_info" variable, one row per node: a student/faculty status
flag, gender, major, second major/minor (if applicable), dorm/house,
year, and high school. Missing data is coded 0.'''

'''Question: Do we know how many edges each person has?'''

#constants
FILE_NAME = 'caltech.txt'

#read text file
def prepare_text(filename_data):
    with open(filename_data) as file:
        text = file.read()
    return text

#create lists of students
def create_students(text):
    list_students = [] #list of all students where each student is a list
    lines = text.splitlines() #should return a list of strings
    for each_line in lines: #for each string in the list of strings append that string
        list_students.append(each_line.split()) #list of student is a list of lists of strings
    return list_students

'''def get_regression_coeff(filename_coeff):
    return list_coeff

def find_attribute(list_students):
    total_students = 0
    for each
    return list_per_attribute

def calculate_weights(list_students):
    return list_weights

def calculate_score(list_students, list_coeff):
    return list_influencers'''

text = prepare_text(FILE_NAME)
list_students = create_students(text)
print(list_students)

