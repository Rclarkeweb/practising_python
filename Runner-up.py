# Hackerrank challenge
n = int(input())
arr = map(int, input.split())

# add code
# convert map into a set to remove duplicates in the data
newset = set(arr)
# convert set into a list and then sort it
newlist = list(newset)
newlist.sort()
# select the second from last element
print(newlist[-2:][0])
