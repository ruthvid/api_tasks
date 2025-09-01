import requests
# print(requests)
apiUrl = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(apiUrl)
print(response,"response")

data = response.json()
# print(data)

# 1. Fetch all posts and print the total number of posts returned.
count = 0
for i in data:
    count+=1
print(f" data has the total number {count} of ids in it")

# 2. Fetch the post with id = 15 and print its title only.
for i in data:
    if i["id"] == 15:
        print(i["title"])

# 3. Fetch all posts where userId = 3 and print the count of those posts.
count = 0
for i in data:
    if i["userId"] == 3:
        count += 1
print(f"userId with 3 has a total of {count} posts in it")
        

# 4. Fetch the post with id = 50 and print both title and body.
for i in data:
    if i["id"] == 50:
        print(i["title"])
        print(i["body"])


# 5. Fetch all posts for userId = 7 and display only the id values of those posts
for i in data:
    if i["userId"] == 7:
        print(i["id"])




# --------------------------------------------------second API------------------------------------------------------------

import requests

apiUrl = "https://jsonplaceholder.typicode.com/users"
response = requests.get(apiUrl)

# print(response)

if response.status_code == 200:
    data = response.json()
    # print(data)
    


# Count all users
#  Task: Fetch all users and print the total number of users returned.
count = 0
for i in data:
    count += 1
    
print(count)


# # Get a user by ID
# #  Task: Retrieve the user with id = 5 and print their name and email.
for i in data:
    if i["id"] == 5:
        print(i["name"] , i["email"])


# Filter users by username
#  Task: Fetch user(s) with username = "Bret" and print the entire JSON object for the match.
result = [i for i in data if i["username"] == "Bret"]
print(result)


# Search users by city in address
#  Task: Retrieve all users and print the names of those whose address.city is "South Christy".
for i in data:
    if i["address"]["city"] == "South Christy":
        print(i["name"])
        
city = [i["name"] for i in data if i["address"]["city"] == "South Christy"]
print(city)


# List user IDs by company name
#  Task: Fetch all users and print the id of each user whose company.name contains the word "Group".
for i in data:
    if "Group" in i["company"]["name"]:
        print(i["id"])



# --------------------------------------------------THIRD API------------------------------------------------------------

import requests

apiUrl = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(apiUrl)
if response.status_code == 200:
    data = response.json()
    # print(data)



# Count all todos
#  Task: Send a GET request to /todos and print the total number of todo items returned.
count=0
for i in data:
    count += 1
print(count)


# Get a specific todo by ID
#  Task: Use a GET request to fetch the todo with id = 42 and print its title.
for i in data:
    if i["id"] == 42:
        print(i["title"])


# Filter todos by userId
#  Task: Send a GET request with userId=3 (e.g., ?userId=3) and print how many todos belong to that user.
count = 0
for i in data:
    if i["userId"] == 3:
        count += 1
print(count)


# List incomplete todos
#  Task: Retrieve all todos and print the ids of todos where completed is false.
for i in data:
    if i["completed"] == False:
        print(i)


# Count completed todos for a user
#  Task: Fetch todos for userId=5 and count how many of those have completed = true.
count=0
for i in data:
    if i["userId"] == 5 and i["completed"] == True:
        count += 1
        print(i)
print(count)