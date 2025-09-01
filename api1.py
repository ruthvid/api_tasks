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

