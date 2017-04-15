import students
import networkx as nx

# a list of Student objects from the Caltech data, where each Student object has a list of attribute data called info
caltech_students = students.initialize_student_list("Caltech_local.csv")

# a list of all friendship connections in Caltech in the form [A, B], where A and B are friends
caltech_friendships = students.create_friendships_list("Caltech_A.txt")
print (caltech_friendships)

G = nx.Graph()

for friendship in caltech_friendships:
    G.add_edge(friendship[0], friendship[1])

