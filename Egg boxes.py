# Egg Boxes. How many omlettes can you make?

num_of_boxes = int(input("How many boxes of eggs do you have?: "))
eggs_in_box = 6
eggs_for_omelette = 4
total = num_of_boxes * eggs_in_box // eggs_for_omelette
leftover = num_of_boxes * eggs_in_box % eggs_for_omelette
msg = "You can make {} omelettes with {} boxes of eggs".format(total,num_of_boxes)
left_msg = "You would have {} eggs remaining".format(leftover)
print(msg)
print(left_msg)
