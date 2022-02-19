f = open('pellican.txt', 'w')
f.write('Pellican file \n')
f.close()
# open file and append a line
f = open('pellican.txt', 'a')
f.write('a wonderful bird is the pellican \n')
f.close()
f = open('pellican.txt', 'a')
f.write('his beak holds more than his bellican \n')
# neccesary to seperate items as they're added in one line
lines = ['He can take in his beak \n', 'Enough food for a week \n', "But I'm dammed if I know how the helican"]
f = open('pellican.txt', 'a')
f.writelines(lines)
f.close()
