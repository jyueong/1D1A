word = input()

word = word.replace('c=', 'a')
word = word.replace('c-', 'a')
word = word.replace('dz=', 'a')
word = word.replace('d-', 'a')
word = word.replace('lj', 'a')
word = word.replace('nj', 'a')
word = word.replace('s=', 'a')
word = word.replace('z=', 'a')

print(len(word))