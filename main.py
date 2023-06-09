import re
from typing import List, Tuple

def find_tracebacks(logs:str) -> Tuple[List[str]]:
    """
    Looks for the patterns of Tracebacks inside a log string, 
    then returns everything it finds.

    Returns a tuple with 2 items: List of full tracebacks, List of exception lines
    """
    lines_log = logs.split("\n")

    pattern1 = re.compile(r'\[.*\]:\s*Traceback \(most recent call last\):')
    pattern2 = re.compile(r'\[.*\]:\s*File "/.*')
    pattern3 = re.compile(r'(\[.*\]:\s*.*(Exception|Error): .*)')

    traceback_string = pattern1.match
    file_tracing_string = pattern2.match
    exception_string = pattern3.match

    traceback_list = []
    exception_list = []
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
            # Also adds exception string to exception list
            string += (line + "\n")
            traceback_list.append(string)
            exception_list.append(line)
    return traceback_list, exception_list

if __name__ == "__main__":
    # Get logs
    with open('console.txt', "r") as file:
        logs = file.read()

    # Process logs
    traceback_list, exceptions = find_tracebacks(logs)
    print(len(traceback_list))
    for x in traceback_list:
        print(x)
    
    for x in exceptions:
        print(x)

