import json

username_dict1 = {}
username_dict2 = {}
results = {}
rankings = {}
with open('botometer.txt', 'r') as username_file:
    for line in username_file:
        line = line.replace("'", '"')
        line = json.loads(line)

for key in line:
    nums = line[key].replace(' ', '').split('/')
    score = float(nums[0])/float(nums[1])
    username_dict1[key] = int(round(score * 100, 2))

with open('botsentinel.txt', 'r') as username_file:
    for line in username_file:
        line = line.replace('%', '').replace('\n', '').replace(' ', ': ')
        line = line.split(':')
        line[1] = line[1].strip()
        if line[1] == '':
            line = ''
        else:
            username_dict2[line[0]] = int(line[1])

normal = 0
satisfactory = 25
disruptive = 50
problematic = 75

for key in username_dict1:
    if key in username_dict2:
        if (username_dict1[key] >= normal and username_dict1[key] < satisfactory) and (username_dict2[key] >= normal and username_dict2[key] < satisfactory):
            results[key] = True
            rankings[key] = 'normal'
        elif (username_dict1[key] >= satisfactory and username_dict1[key] < disruptive) and (username_dict2[key] >= satisfactory and username_dict2[key] < disruptive):
            results[key] = True
            rankings[key] = 'satisfactory'
        elif (username_dict1[key] >= disruptive and username_dict1[key] < problematic) and (username_dict2[key] >= disruptive and username_dict2[key] < problematic):
            results[key] = True
            rankings[key] = 'disruptive'
        elif (username_dict1[key] >= problematic) and (username_dict2[key] >= problematic):
            results[key] = True
            rankings[key] = 'problematic'
        else:
            results[key] = False

values = [value for value in results.values()]
ranking = [ranking for ranking in rankings.values()]
print(values.count(True))
print(values.count(False))

print(ranking.count('normal'))
print(ranking.count('satisfactory'))
print(ranking.count('disruptive'))
print(ranking.count('problematic'))