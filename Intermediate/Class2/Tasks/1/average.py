import json

with open('data.json', 'r') as file:
    data = json.load(file)

right = int(sum(data['right_side']) / len(data['right_side']))
left = round(sum(data['left_side']) / len(data['left_side']))
both = round((right + left) / 2)

print("Right side:", right)
print("Left side:", left)
print("Both sides:", both)
