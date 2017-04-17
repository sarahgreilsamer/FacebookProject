import students
import networkx as nx
import random

def initialize_graph():
    # a list of Student objects from the Caltech data, where each Student object has a list of attribute data called info
    caltech_students = students.initialize_student_list("Caltech_local.csv")

    # a list of all friendship connections in Caltech in the form [A, B], where A and B are friends
    caltech_friendships = students.create_friendships_list("Caltech_A.txt")

    G = nx.Graph()

    for friendship in caltech_friendships:
        G.add_node(int(friendship[0]))
        G.add_node(int(friendship[1]))
        G.add_edge(int(friendship[0]), int(friendship[1]))

    return G

def post_share(G, node, P, seen_so_far):
    # give a post to the node
    # P is the likelihood that any given person will share the post
    # (assume that the first node is guaranteed to share)
    # if a node "sees" a post, that is, one of their friends has shared the post
    # then increment the number of people who have seen it
    # and decide if they are also going to share it

    # assume that all of the node's friends see the post
    seen_so_far += len(G.neighbors(node))
    list_of_friends = G.neighbors(node)
    print (list_of_friends)

    # randomly decide if one of the node's friends will share the post, or if none will
    r = random.randint(0,1)
    if (r == 1):
        seen_so_far += post_share(G, list_of_friends[0], P, seen_so_far)

    # return the number of people that have seen the post
    return seen_so_far

# we need:
# the number of friends of the node
# the array of the node's friends


def share_post(node, P):
    pass

def main():
    g = initialize_graph()
    print(post_share(g, 1, .10, 0))

if __name__ == "__main__":
    main()
