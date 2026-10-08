'''12. Simple API User Program
• Use requests.get() to call a simple public API.
• Check the response status code.
• Convert the response to JSON.
• Display the names of the users returned by the API.'''

import requests

# Call the API
response = requests.get("https://jsonplaceholder.typicode.com/users")

# Check the response status code
print("Status Code:", response.status_code)

# Convert response to JSON
users = response.json()

# Display the names of users
print("User Names:")

for user in users:
    print(user["name"])