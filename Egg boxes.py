# Egg Boxes. How many omlettes can you make?

numofboxes = int(input("How many boxes of eggs do you have?: "))
eggs_in_box = 6
eggs_for_omelette = 4
total = numofboxes * eggs_in_box // eggs_for_omelette
leftover = numofboxes * eggs_in_box % eggs_for_omelette
msg = "You can make {} omelettes with {} boxes of eggs".format(total,numofboxes)
leftmsg = "You would have {} eggs remaining".format(leftover)
print(msg)
print(leftmsg)
