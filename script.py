## Imports
import requests
import os

## Configuration
API_KEY = os.environ['APIKEY']
UNIVERSE_ID = 5227039366
COOKIES = {".ROBLOSECURITY": os.environ['COOKIESECRET']}

## Varibles
places = requests.get("https://develop.roblox.com/v1/universes/" + str(UNIVERSE_ID) + "/places?sortOrder=Asc&limit=100").json()["data"]

for i in range(len(places)):
    print("[LOG] fetching place data for placeId :: ", places[1]["id"])
    print("placeName in focus ::", places[1]["name"])
  
    place_data = requests.get("https://assetdelivery.roblox.com/v1/asset/?id=" + str(places[i]["id"]), cookies=COOKIES)
    version = int(place_data.history[0].headers["roblox-assetversionnumber"])
    response = requests.post("https://apis.roblox.com/universes/v1/" + str(UNIVERSE_ID) + "/places/" + str(places[i]["id"]) + "/versions?versionType=Published", data=place_data.content, headers={"x-api-key": API_KEY})
    print("[LOG] Published as", response.text)
    print()


# Wait for specific input
user_input = input("Input 'y' to shutdown all game servers, else 'enter' to close prompt... ").lower()

if user_input == "y":
    print("Shutting down servers for update")
else:
    print("Closing Prompt...")
    quit()

print("SHUTDOWN")
