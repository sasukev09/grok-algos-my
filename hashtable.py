voted = {}

voted["tom"] = True

def vote_now(name):
    if voted.get(name):
        return print("kick them out!")
    else:
        voted[name] =  True
        print("they can vote")

print(voted)
vote_now("tom")
vote_now("mike")
print(voted)