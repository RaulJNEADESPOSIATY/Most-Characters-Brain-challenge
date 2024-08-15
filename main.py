#get a user to enter a sentence find the word with the most charecters
# and print it out and return the amount of charecters aswell

count = 0
the_input = ("")
user = input("please enter a string! ")
indivisual = user.split()

for x in range(len(indivisual)):
    if len(indivisual[x]) > count:
        count = len(indivisual[x])
        the_input = indivisual[x]
    elif len((indivisual[x])) < count:
        count = count
    elif len(indivisual[x]) == count:
        count = len(indivisual[x])
        the_input = indivisual[x]


print(count)
print(the_input)

#now simpliar
war = 0

request = input("please enter a string! ").split()

for x in range(len(request)):
    if len(request[x]) > war:
        war = len(request[x])
    elif len(request[x]) <= war:
        war = war

print(war)