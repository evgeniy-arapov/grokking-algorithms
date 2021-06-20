from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'


def search(graph, name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                return person
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
