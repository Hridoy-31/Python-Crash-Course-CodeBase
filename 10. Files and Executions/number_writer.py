import json

filename = 'numbers.json'

numbers = [2,4,6,8,10]

with open(filename, 'w') as f:
    json.dump(numbers, f)

