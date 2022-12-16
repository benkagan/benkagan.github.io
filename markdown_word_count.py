import json

with open('final_project.ipynb') as json_file:
    data = json.load(json_file)

wordCount = 0
for each in data['cells']:
    cellType = each['cell_type']
    if cellType == "markdown":
        content = each['source']
        for line in content:
            temp = [word for word in line.split() if "#" not in word or "-" not in word] # we might need to filter for more markdown keywords here
            wordCount = wordCount + len(temp)
print(wordCount)