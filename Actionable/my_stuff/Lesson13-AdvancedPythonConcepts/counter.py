from collections import Counter

with open('Declaration_of_Independence.txt', 'r') as f:
    declaration = f.read()

declaration_list = declaration.split()

appendable = []
for each in declaration_list:
    if len(each) >= 6:
        appendable.append(each.upper())
c = Counter(appendable)

print(c.most_common(10))
