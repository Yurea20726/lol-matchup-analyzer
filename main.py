import os
import requests
from collections import Counter

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

wins = 0
total_games = len(match_ids)
champions = []
total_kills = 0
total_deaths = 0
total_assists = 0

for match_id in match_ids:

    match_url = (
        f"https://asia.api.riotgames.com/lol/match/v5/matches/{match_id}"
    )

    match_response = requests.get(
        match_url,
        headers=headers
    )

    match_data = match_response.json()

    participants = match_data["metadata"]["participants"]
    

    my_index = participants.index(puuid)

    me = match_data["info"]["participants"][my_index]
    champions.append(me["championName"])

    if me["win"]:
        wins += 1

    total_kills += me["kills"]
    total_deaths += me["deaths"]
    total_assists += me["assists"]

win_rate = wins / total_games * 100
champion_counts = Counter(champions)

most_played = champion_counts.most_common(3)

avg_kills = total_kills / total_games
avg_deaths = total_deaths / total_games
avg_assists = total_assists / total_games

kda = (total_kills + total_assists) / max(1, total_deaths)

print(f"\nTotal Games: {total_games}")
print(f"Wins: {wins}")
print(f"Win Rate: {win_rate:.1f}%")

print("\nAverage Stats:")
print(f"Kills: {avg_kills:.1f}")
print(f"Deaths: {avg_deaths:.1f}")
print(f"Assists: {avg_assists:.1f}")
print(f"KDA: {kda:.2f}")
print("\nMost Played Champions:")

for champion, games in most_played:
    print(f"{champion}: {games} games")