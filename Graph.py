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
        G.add_node(int(friendship[0]), hasShared = False, hasSeen = False)
        G.add_node(int(friendship[1]), hasShared = False, hasSeen = False)
        G.add_edge(int(friendship[0]), int(friendship[1]))

    return G

def post_share(G, n, P, seen_so_far):
    # give a post to the node
    # P is the likelihood that any given person will share the post
    # if a node "sees" a post, that is, one of their friends has shared the post,
    # then increment the number of people who have seen it
    # and decide if they are also going to share it

    G.node[n]['hasShared'] = True
    G.node[n]['hasSeen'] = True

    # assume that all of the node's friends see the post
    # if a node has already seen the post, don't add it to the count of people that have seen it
    list_of_friends = G.neighbors(n)
    for student in list_of_friends:
        if not G.node[student]['hasSeen']:
            seen_so_far += 1
            G.node[student]['hasSeen'] = True

    # take roughly P percent of the node's friends
    select_friends = int (P * len(list_of_friends))

    # randomly pick up to select_friends to share with
    for i in range (select_friends):
        r = random.randint(0, len(list_of_friends) - 1)
        # only share if the friend has not already shared the post before
        if not G.node[list_of_friends[r]]['hasShared']:
            G.node[list_of_friends[r]]['hasShared'] = False
            seen_so_far = post_share(G, list_of_friends[r], P, seen_so_far)

    # return the number of people that have seen the post
    return seen_so_far

def share_post(node, P):
    pass

def main():
    g = initialize_graph()
    print(post_share(g, 1, .10, 0))

if __name__ == "__main__":
    main()
