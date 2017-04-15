import students
import networkx as nx

def initialize_graph():
    # a list of Student objects from the Caltech data, where each Student object has a list of attribute data called info
    caltech_students = students.initialize_student_list("Caltech_local.csv")

    # a list of all friendship connections in Caltech in the form [A, B], where A and B are friends
    caltech_friendships = students.create_friendships_list("Caltech_A.txt")

    G = nx.Graph()

    for friendship in caltech_friendships:
        G.add_node(friendship[0])
        G.add_node(friendship[1])
        G.add_edge(friendship[0], friendship[1])

    return G

def initial_share(node, P):
    # give a post to the node
    # P is the likelihood that any given person will share the post
    # (assume that the first node is guaranteed to share)
    # if a node "sees" a post, that is, one of their friends has shared the post
    # then increment the number of people who have seen it
    # and decide if they are also going to share it

    # initialize the number of people who have seen the post to 1, for the initial node
    number_seen = 1


def main():
    g = initialize_graph()
    print (g.nodes())
    print (g.edges())

if __name__ == "__main__":
    main()
