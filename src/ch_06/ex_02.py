# reading and writing json data
import json

data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}

print(format('Python to JSON', '*^20'))
json_str = json.dumps(data)
print(json_str)

# writing json to a file
with open('data.json', 'w') as f:
    json.dump(data, f)

print(format('JSON to Python', '*^20'))
py_data = json.loads(json_str)
print(py_data)

# reading json from a file
with open('data.json') as f:
    json.load(f)

if __name__ == '__main__':
    pass
