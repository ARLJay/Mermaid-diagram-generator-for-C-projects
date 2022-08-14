import sys, getopt, os, re
from collections import defaultdict

relative_path = False
result = False
files = defaultdict(str)
file_counter = 0

def generate_diagram():
    global file_counter
    files_in_path = os.listdir(relative_path)

    for file in files_in_path:
        if os.path.isfile(relative_path + "/" + file):
            files[file] = file_counter
            file_counter += 1

    print(result)
    f = open(result, "a")
    for key in files:
        f.write("  " + str(files[key]) + "[" + key + "]\n")
    f.write("\n")
    f.close()

    for key in files:
        f = open(relative_path + "/" + key, "r")
        found_includes = re.findall('#include .+', f.read())
        f.close()

        f = open(result, "a")
        for file in found_includes:
            file = re.split('<|>|\"', file)[1]
            if file in files:
                f.write("   " + str(files[file]) + "-->" + str(files[key]) + "\n")
        f.close()


if __name__=="__main__":
    relative_path = sys.argv[1]
    result = os.getcwd() + "/" + "mermaid_diagram.txt"
    f = open(result, "w")
    f.write("graph TD\n")
    f.close()
    generate_diagram()
