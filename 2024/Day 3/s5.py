from re import findall # RegEx python

print(sum([(lambda x : x[0] * x[1])([int(k) for k in findall("\d+", i)]) for i in findall("mul\(\d+,\d+\)", open(r'2024\Day 3\d3.txt', 'r').read())]))

"""
did i need to make it a one liner? no. but it was funny :)

how this works:
- open(r'2024\Day 3\d3.txt', 'r').read()
    - opens d3.txt (input) in read mode and immediately reads the file as a string
- findall("mul\(\d+,\d+\)", open)
    - detects all valid "mult" calls => puts them in a list
- func for i in findall
    - iterates over all "mult" calls
    - [int(k) for k in findall("\d+", i)]
        - for every mult call, finds every instance of integers and casts them to integers automatically and puts them in a two-ele list
    - (lambda x : x[0] * x[1])(previous)
        - runs the lamda function (multiplies elements of list) on each two integers
    - sum: obviously sums all of the mult calls for the answer

hypothetically O(n) time? idk RegEx time complexity
"""