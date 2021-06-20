from collections import deque
from search import search, person_is_seller

graph = {}

graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy", "you"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = ["you"]
graph["jonny"] = []

search_queue = deque()

search_queue += graph["you"]

mango_seller = None

while search_queue:
    person = search_queue.popleft()
    if person_is_seller(person):
        mango_seller = person
        break
    else:
        search_queue += graph[person]

if mango_seller:
    print mango_seller + " is a mango seller"
else:
    print "Mango seller not found"

second_mango_seller_result = search(graph, "you")

if second_mango_seller_result:
    print second_mango_seller_result + " is a mango seller"
else:
    print "Mango seller not found"

