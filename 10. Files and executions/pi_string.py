filename = '/home/hridoy/github/Python-Crash-Course-CodeBase/10. Files and executions/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

py_str = ''

for line in lines:
    py_str += line.strip()

print(py_str)
print(len(py_str))