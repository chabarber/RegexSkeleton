import re
pattern = re.compile()#enter regex search here

tags = []

target_file = input("Enter a file to search e.g 'data.txt': ")

for i, line in enumerate(open(target_file)):
    for match in re.finditer(pattern, line):
        if match.group() not in tags:
           tags.append(match.group())
        else:
           break

output_file = input("Name of file to output to e.g 'output.txt': ")
file1 = open(output_file, "w")        
for i in tags:
    file1.write(i + "\n")      

file1.close()
