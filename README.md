# LOL Matchup Analyzer

A Python CLI tool that analyzes League of Legends ranked solo/duo match history using the Riot Games API.

## Features

- Analyze up to 100 recently ranked solo/duo games
- Display the 20 most recent matches
- Calculate win rate
- Calculate average KDA
- Show most played champions
- Show champion win rates
- Show matchup statistics
- Champion matchup lookup

## Requirements

- Python
- uv
- Riot Games API Key

## Getting a Riot API Key

Visit:

https://developer.riotgames.com/

Log in with your Riot account and generate a Development API Key.

Copy the key that starts with:

RGAPI-

Development keys expire after approximately 24 hours.

## Run

Set your API key:

```powershell
$env:RIOT_API_KEY="YOUR_API_KEY"
