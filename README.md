# LOL Ranked Matchup Analyzer

LOL Ranked Matchup Analyzer is a Python command-line tool that analyzes a League of Legends player's recent ranked solo/duo games using the Riot Games API. It shows recent matches, win rate, average KDA, most played champions, and champion matchup statistics.

# Features

- Analyze up to 100 recently ranked solo/duo games
- Display the 20 most recent matches
- Calculate win rate
- Calculate average KDA
- Show most played champions
- Show champion win rates
- Show matchup statistics
- Champion matchup lookup

# Requirements

- Python
- uv
- Riot Games API Key

# Usage
## 1. Install the project

Clone this repository and install dependencies with uv:

uv sync

## 2.Getting a Riot API Key

This project requires a Riot Games API key.

Go to:

https://developer.riotgames.com/

Log in or Sign up with your Riot account and generate a Development API Key.

Copy the key that starts with:

RGAPI-

Development keys expire after approximately 24 hours. So you may need to regenerate a new key later.

# Run:

Set your API key:

```powershell
$env:RIOT_API_KEY="YOUR_API_KEY"
```
# Run:
```powershell
uv run main.py
```

The program will ask for:

-Summoner Name

-Tag Line

-Match Region

-Account Region

## Example Input

  # Example for a Korean account:

  -Summoner Name: Hide on bush

  -Tag Line: KR1

  -Match Region(asia/americas/europe/sea): asia

  -Account Region(asia/americas/europe/sea): asia

  or any player you want to analyze

  # Example for a Europe account:

  -Summoner Name: G2 Caps

  -Tag Line: 1323

  -Match Region(asia/americas/europe/sea): europe

  -Account Region(asia/americas/europe/sea): europe

# Features

-Analyze up to 100 recently ranked solo/duo games
-Display the 20 most recent ranked matches
-Show win rate and average KDA
-Show the most played champions
-Show champion win rates
-Show matchup statistics
-Look up a specific champion's matchups
-Region Guide

## Use these match regions:

KR / JP: asia
NA / BR / LAN / LAS: americas
EUW / EUNE / TR / RU: europe
TW / SG / VN / OCE: sea

# Example Output
## Recent Ranked Solo/Duo Matches:

WIN | MIDDLE | Yone vs Ahri | 8/3/7 | KDA 5.00
LOSS | TOP | Rumble vs Jayce | 5/8/6 | KDA 1.38

Total Games: 100
Wins: 57
Win Rate: 57.0%

## Most Played Champions:

Yone
Games: 15
Wins: 9
Win Rate: 60.0%

## Champion Matchup Lookup (or EXIT): Yone

Yone Matchups

vs Ahri
3 Games
66.7% Win Rate

