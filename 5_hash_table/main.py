book = dict()

book['apple'] = 0.67
book['milk'] = 1.49
book["avocado"] = 1.49

print book

# =======================================
phone_book = {"jenny": 67890, "emergency": 911}

print phone_book["jenny"]

# ======================================
voted = {}


def check_voter(name):
    if voted.get(name):
        print "kick them out!"
    else:
        voted[name] = True
        print "let them vote"


check_voter("tom")
check_voter("mike")
check_voter("mike")
