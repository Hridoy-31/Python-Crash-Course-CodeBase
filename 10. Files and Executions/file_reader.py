filename = '/home/hridoy/github/Python-Crash-Course-CodeBase/10. Files and executions/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
