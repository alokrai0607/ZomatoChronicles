import requests
import json

# Define the base URL for the Zomato API
base_url = "https://developers.zomato.com/api/v2.1"

# Replace 'YOUR_ZOMATO_API_KEY' with your actual Zomato API key
headers = {"user-key": "YOUR_ZOMATO_API_KEY"}

# Define the endpoint for searching restaurants
search_endpoint = f"{base_url}/search"

# Define parameters for the search query
city_name = "New York"  # Change this to the desired city
params = {"q": city_name}

# Make the GET request to the API
response = requests.get(search_endpoint, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()

    # Extract and print relevant information from the API response
    for restaurant in data["restaurants"]:
        name = restaurant["restaurant"]["name"]
        address = restaurant["restaurant"]["location"]["address"]
        rating = restaurant["restaurant"]["user_rating"]["aggregate_rating"]

        print(f"Name: {name}")
        print(f"Address: {address}")
        print(f"Rating: {rating}")
        print("-" * 30)
else:
    print("Error fetching data from the Zomato API.")
