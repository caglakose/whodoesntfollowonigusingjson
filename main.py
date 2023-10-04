import json

with open('followers.json') as file:
    followers_json = json.load(file)

with open('following.json') as file:
    following_json = json.load(file)

followers_list = []

# Iterate through each follower in the list
for follower in followers_json:
    follower_username = follower["string_list_data"][0]["value"]
    
    # Append the follower's username to the followers_list
    followers_list.append(follower_username)

not_following_back = []

for following in following_json["relationships_following"]:
    following_username = following["string_list_data"][0]["value"]

    # Check if the following user is not in the followers_list
    if following_username not in followers_list:
        not_following_back.append(following_username)

for user in not_following_back:
    print(user)
