import re

with open('console.txt', "r") as file:
    logs = file.read()

lines_log = logs.split("\n")

result1 = re.findall(r'\[.*\]:\s*Traceback \(most recent call last\):', logs)
result2 = re.findall(r'\[.*\]:\s*File "/.*\n.*', logs)
result3 = re.findall(r'(\[.*\]:\s*.*(Exception|Error): .*)', logs)
print(len(result1))
print(len(result2))
print(len(result3))

pattern1 = re.compile(r'\[.*\]:\s*Traceback \(most recent call last\):')
pattern2 = re.compile(r'\[.*\]:\s*File "/.*')
pattern3 = re.compile(r'(\[.*\]:\s*.*(Exception|Error): .*)')

traceback_string = pattern1.match
file_tracing_string = pattern2.match
exception_string = pattern3.match

traceback_list = []
for index, line in enumerate(lines_log):
        
    if traceback_string(line):
        # create line
        string = line + "\n"

    elif file_tracing_string(line):
        # Add the file tracing + the next line
        string += (line + "\n")
        string += (lines_log[index+1] + "\n")

    elif exception_string(line):
        # Add the exception and adds to list (final line)
        string += (line + "\n")
        traceback_list.append(string)

for x in traceback_list:
    print(x)

