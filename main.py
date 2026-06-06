import os
import requests

GAME_NAME = "Hide on bush"
TAG_LINE = "KR1"

API_KEY = os.getenv("RIOT_API_KEY")

headers = {
    "X-Riot-Token": API_KEY
}

# Step 1: Get PUUID
account_url = (
    f"https://asia.api.riotgames.com/riot/account/v1/accounts"
    f"/by-riot-id/{GAME_NAME}/{TAG_LINE}"
)

account_response = requests.get(account_url, headers=headers)
account_data = account_response.json()

puuid = account_data["puuid"]

print(f"Player: {GAME_NAME}#{TAG_LINE}")
print(f"PUUID: {puuid}")

# Step 2: Get Match IDs
matches_url = (
    f"https://asia.api.riotgames.com/lol/match/v5/matches"
    f"/by-puuid/{puuid}/ids?start=0&count=20"
)

matches_response = requests.get(matches_url, headers=headers)

match_ids = matches_response.json()

print("\nRecent Matches:")
for match in match_ids:
    print(match)