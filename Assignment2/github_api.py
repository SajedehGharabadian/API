import requests

username = "SajedehGharabadian" 
url = f"https://api.github.com/users/{username}"
user_data = requests.get(url)
json_file = user_data.json()

print("The number of followers:",json_file['followers'])
print("The number of following:",json_file['following'])