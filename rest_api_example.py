import requests

# get response data from rest api 
target = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url = target)

# change json to python object
data = response.json()

# get name info only
name_list = []
for user in data:
    name_list.append(user["name"])

print(name_list)
