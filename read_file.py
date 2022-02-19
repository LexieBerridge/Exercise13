f = open('pellican.txt', 'r')
fileneeded = f.read()
print(fileneeded)
# prints entire content of open file

print(type(fileneeded))
# class of this data is a string

list = fileneeded.split('\n')
print(len(list))
print(list)
# break file into list by splitting at each new line

for item in list:
    print(item)
# loop to itterate for the items in the list