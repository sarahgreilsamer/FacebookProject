'''Info on data
Each of the school .mat files has an A matrix (sparse) and a
"local_info" variable, one row per node: a student/faculty status
flag, gender, major, second major/minor (if applicable), dorm/house,
year, and high school. Missing data is coded 0.'''

'''Question: Do we know how many edges each person has?'''

#constants
FILE_NAME = 'Amherst75'
total_students = 2235

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

def count_status(list_students):
    all_status = []
    for student in list_students:
        if int(student[0]) in all_status:
            pass
        else:
            all_status.append(int(student[0]))
    all_status = sorted(all_status)
    s = len(all_status)
    count_status = []
    for i in range(0, s):
        count_status.append(0)
    for student in list_students:
        for x in range(0, s):
            if int(student[0]) == int(all_status[x]):
                count_status[x] =+ 1
    return count_status

def count_gender(list_students):
    all_gender = []
    for student in list_students:
        if int(student[1]) in all_gender:
            pass
        else:
            all_gender.append(int(student[1]))
    all_gender = sorted(all_gender)
    t = len(all_gender)
    count_gender = []
    for i in range (0, t):
        count_gender.append(0)
    for student in list_students:
        for x in range(0, t):
            if int(student[0]) == int(all_gender[x]):
                count_gender[x] =+ 1
    return count_gender

def count_major(list_students):
    all_major = []
    for student in list_students:
        if int(student[2]) in all_major:
            pass
        else:
            all_major.append(int(student[2]))
    all_status = sorted(all_major)
    u = len(all_major)
    count_major = []
    for i in range(0, u):
        count_major.append(0)
    for student in list_students:
        for x in range(0, u):
            if int(student[2]) == int(all_status[x]):
                count_major[x] =+ 1
    return count_major

def count_secondmm(list_students):
    all_secondmm = []
    for student in list_students:
        if int(student[3]) in all_secondmm:
            pass
        else:
            all_secondmm.append(int(student[3]))
    all_secondmm = sorted(all_secondmm)
    v = len(all_secondmm)
    count_secondmm = []
    for i in range(0, v):
        count_secondmm.append(0)
    for student in list_students:
        for x in range(0, v):
            if int(student[3]) == int(all_secondmm[x]):
                count_secondmm[x] =+ 1
    return count_secondmm

def count_housing(list_students):
    all_housing = []
    for student in list_students:
        if int(student[4]) in all_housing:
            pass
        else:
            all_housing.append(int(student[4]))
    all_housing = sorted(all_housing)
    w = len(all_housing)
    count_housing = []
    for i in range(0, w):
        count_housing.append(0)
    for student in list_students:
        for x in range(0, v):
            if int(student[4]) == int(all_housing[x]):
                count_housing[x] =+ 1
    return count_housing

def count_year(list_students):
    all_year = []
    for student in list_students:
        if int(student[5]) in all_year:
            pass
        else:
            all_year.append(int(student[5]))
    all_year = sorted(all_year)
    v = len(all_year)
    count_year = []
    for i in range(0, v):
        count_year.append(0)
    for student in list_students:
        for x in range(0, v):
            if int(student[5]) == int(all_year[x]):
                count_year[x] =+ 1
    return count_year

def count_highschool(list_students):
    all_highschool = []
    for student in list_students:
        if int(student[0]) in all_highschool:
            pass
        else:
            all_highschool.append(int(student[6]))
    all_highschool = sorted(all_highschool)
    w = len(all_highschool)
    count_highschool = []
    for i in range(0, w):
        count_highschool.append(0)
    for student in list_students:
        for x in range(0, w):
            if int(student[6]) == int(all_highschool[x]):
                count_highschool[x] =+ 1
    return count_highschool