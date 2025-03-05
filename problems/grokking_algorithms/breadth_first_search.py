from collections import deque

def breadth_first_search(name, graph, check):
    search_queue = deque()
    search_queue += graph[name]   
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if check(person):
                print(person)
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False
        
def test():
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["alice"] = ["juana m", "juanito m"]
    graph["bob"] = []
    graph["claire"] = []

    breadth_first_search("you", graph, lambda name : name[-1] == 'm') # givin a condition, it finds the first ocurrency
    breadth_first_search("you", graph, lambda name : name[0] == 'c')

test()