import os
from collections import Counter

# 1. Få path fra brukeren
path = input("Enter the path: ")
path = os.path.expanduser(path)

# 2. Sjekk at path finnes og er en mappe
while not (os.path.exists(path) and os.path.isdir(path)):
    print("Invalid path. Please try again.")
    path = input("Enter the path: ")
    path = os.path.expanduser(path)

# 3. Rekursivt hente alle filer
all_files = []

for root, dirs, files in os.walk(path):
    for file in files:
        all_files.append(os.path.join(root, file))

# 4. Print ut alle filene
print("Found files:")
for f in all_files:
    print(f)

# 5. Hente ut alle file extensions
    extensions = [os.path.splitext(f)[1].lower() for f in all_files if '.' in f]

# 6. Tell hvor mange filer av hver type
counter = Counter(extensions)

# 7. Print ut resultatet
print("\nFile types count:")
for ext, count in counter.items():
    print(f"{ext}: {count} filer")
