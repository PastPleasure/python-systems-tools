import os



path = input("Enter the path: ")
path = os.path.expanduser(path)

while not (os.path.exists(path) and os.path.isfile(path)):
    print("Invalid path. Please try again.")
    path = input("Enter the path: ")
    path = os.path.expanduser(path)

with open(path, 'r') as file:
    text = file.read()
    text = text.lower()

split_text = text.split()
word_count = {}
for word in split_text:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


print(word_count)