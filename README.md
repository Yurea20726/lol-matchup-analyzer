# LOL Ranked Matchup Analyzer
I created a Python CLI tool called `lol_tool`, a League of Legends Ranked Matchup Analyzer.

`lol_tool` is a command-line application that uses the Riot Games API to analyze a player's recent ranked Solo/Duo matches. It provides detailed statistics, including recent match history, win rate, average KDA, most-played champions, and champion matchup performance. The tool helps players quickly understand their strengths, weaknesses, and performance trends through a simple terminal interface.

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

## Usage



## 1.Getting a Riot API Key

This project requires a Riot Games API key.

Go to:

https://developer.riotgames.com/

Log in or Sign up with your Riot account and generate a Development API Key.

Copy the key that starts with:

RGAPI-

example: "RGAPI-01bc9999-c999-9f99-9999-be99fff9d9c9"

Development keys expire after approximately 24 hours. So you may need to regenerate a new key later.

## 2. Install the project

uv add: 
```powershell
"git+https://github.com/Yurea20726/lol-matchup-analyzer.git"
```
```powershell
uv init
```
# Run:

Set your API key:

example: "RGAPI-01bc9999-c999-9f99-9999-be99fff9d9c9"
```powershell
$env:RIOT_API_KEY="RGAPI-01bc9999-c999-9f99-9999-be99fff9d9c9"
```

```powershell
$env:RIOT_API_KEY="YOUR_API_KEY"
```
# Run:
```powershell
uv run lol_tool
```

The program will ask for:

- Summoner Name

- Tag Line

- Match Region

- Account Region

## Use these match regions:

  - KR / JP: asia
  
  - NA / BR / LAN / LAS: americas
  
  - EUW / EUNE / TR / RU: europe
  
  - TW / SG / VN / OCE: sea

## Example Input

  ### Example for a Korean account:

  - Summoner Name: Hide on bush

  - Tag Line: KR1

  - Match Region(asia/americas/europe/sea): asia

  - Account Region(asia/americas/europe/sea): asia

  or any player you want to analyze

  ### Example for a Europe account:

  - Summoner Name: G2 Caps

  - Tag Line: 1323

  - Match Region(asia/americas/europe/sea): europe

  - Account Region(asia/americas/europe/sea): europe

if show:
```powershell
Failed to get player.
Status Code: 401
Response: {'status': {'message': 'Unknown apikey', 'status_code': 401}}
```
Verify that you are not a robot at the API website


# Features

- Analyze up to 100 recently ranked solo/duo games
- Display the 20 most recent ranked matches
- Show win rate and average KDA
- Show the most played champions
- Show champion win rates
- Show matchup statistics
- Look up a specific champion's matchups
- Region Guide



## Example Output
### Recent Ranked Solo/Duo Matches:
```text
WIN | MIDDLE | Yone vs Ahri | 8/3/7 | KDA 5.00

LOSS | TOP | Rumble vs Jayce | 5/8/6 | KDA 1.38

Total Games: 100

Wins: 57

Win Rate: 57.0%
```
### Most Played Champions

```text
Yone
  Games: 15
  Wins: 9
  Win Rate: 60.0%

Azir
  Games: 12
  Wins: 7
  Win Rate: 58.0%

Ryze
  Games: 10
  Wins: 5
  Win Rate: 50.0%
```

### Champion Matchup Lookup (or EXIT): Yone
```text
Yone Matchups

vs Ahri
3 Games
66.7% Win Rate
```

