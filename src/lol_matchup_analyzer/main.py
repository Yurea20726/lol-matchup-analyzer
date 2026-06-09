import os
import requests
from collections import Counter, defaultdict


def main():
    GAME_NAME = input("Summoner Name: ").strip()
    TAG_LINE = input("Tag Line: ").strip()

    MATCH_REGION = input(
        "Match Region (asia/americas/europe/sea): "
    ).strip().lower()

    ACCOUNT_REGION = input(
        "Account Region (asia/americas/europe): "
    ).strip().lower()

    MATCHES_TO_DISPLAY = 20
    MATCHES_TO_ANALYZE = 100
    display_count = 0

    API_KEY = os.getenv("RIOT_API_KEY")

    if not API_KEY:
        print("RIOT_API_KEY not found.")
        raise SystemExit()

    headers = {
        "X-Riot-Token": API_KEY
    }

    account_url = (
        f"https://{ACCOUNT_REGION}.api.riotgames.com"
        f"/riot/account/v1/accounts"
        f"/by-riot-id/{GAME_NAME}/{TAG_LINE}"
    )

    account_response = requests.get(
        account_url,
        headers=headers
    )

    account_data = account_response.json()

    if (
        account_response.status_code != 200
        or "puuid" not in account_data
    ):
        print("Failed to get player.")
        print("Status Code:", account_response.status_code)
        print("Response:", account_data)
        raise SystemExit()

    puuid = account_data["puuid"]

    print(f"\nPlayer: {GAME_NAME}#{TAG_LINE}")

    matches_url = (
        f"https://{MATCH_REGION}.api.riotgames.com"
        f"/lol/match/v5/matches"
        f"/by-puuid/{puuid}"
        f"/ids?queue=420&start=0"
        f"&count={MATCHES_TO_ANALYZE}"
    )

    matches_response = requests.get(
        matches_url,
        headers=headers
    )

    match_ids = matches_response.json()

    if matches_response.status_code != 200:
        print("Failed to get matches.")
        print("Status Code:", matches_response.status_code)
        print("Response:", match_ids)
        raise SystemExit()

    if len(match_ids) == 0:
        print("No ranked solo/duo matches found.")
        raise SystemExit()

    wins = 0
    total_games = len(match_ids)

    total_kills = 0
    total_deaths = 0
    total_assists = 0

    champion_counts = Counter()
    champion_wins = Counter()

    matchup_counts = defaultdict(int)
    matchup_wins = defaultdict(int)

    champion_matchups = defaultdict(int)
    champion_matchup_wins = defaultdict(int)

    print("\nRecent Ranked Solo/Duo Matches:")

    for match_id in match_ids:
        match_url = (
            f"https://{MATCH_REGION}.api.riotgames.com"
            f"/lol/match/v5/matches/{match_id}"
        )

        match_response = requests.get(
            match_url,
            headers=headers
        )

        if match_response.status_code != 200:
            print(f"Skipping {match_id}")
            continue

        match_data = match_response.json()

        participants = (
            match_data["metadata"]["participants"]
        )

        my_index = participants.index(puuid)

        me = (
            match_data["info"]["participants"]
            [my_index]
        )

        my_champion = me["championName"]
        my_position = me["teamPosition"]
        my_team = me["teamId"]

        opponent_champion = "Unknown"

        for player in match_data["info"]["participants"]:
            if (
                player["teamId"] != my_team
                and player["teamPosition"] == my_position
            ):
                opponent_champion = (
                    player["championName"]
                )
                break

        result = "WIN" if me["win"] else "LOSS"

        kills = me["kills"]
        deaths = me["deaths"]
        assists = me["assists"]

        game_kda = (
            kills + assists
        ) / max(1, deaths)

        if display_count < MATCHES_TO_DISPLAY:
            print(
                f"{result} | "
                f"{my_position} | "
                f"{my_champion} vs "
                f"{opponent_champion} | "
                f"{kills}/{deaths}/{assists} | "
                f"KDA {game_kda:.2f}"
            )

        display_count += 1

        champion_counts[my_champion] += 1

        matchup_counts[
            (my_champion, opponent_champion)
        ] += 1

        champion_matchups[
            (my_champion, opponent_champion)
        ] += 1

        if me["win"]:
            wins += 1

            champion_wins[
                my_champion
            ] += 1

            matchup_wins[
                (my_champion, opponent_champion)
            ] += 1

            champion_matchup_wins[
                (my_champion, opponent_champion)
            ] += 1

        total_kills += kills
        total_deaths += deaths
        total_assists += assists

    win_rate = wins / total_games * 100

    avg_kills = total_kills / total_games
    avg_deaths = total_deaths / total_games
    avg_assists = total_assists / total_games

    overall_kda = (
        total_kills + total_assists
    ) / max(1, total_deaths)

    print(f"\nTotal Games: {total_games}")
    print(f"Wins: {wins}")
    print(f"Win Rate: {win_rate:.1f}%")

    print("\nAverage Stats:")
    print(f"Kills: {avg_kills:.1f}")
    print(f"Deaths: {avg_deaths:.1f}")
    print(f"Assists: {avg_assists:.1f}")
    print(f"KDA: {overall_kda:.2f}")

    print("\nMost Played Champions:")

    for champion, games in champion_counts.most_common(10):
        wins_for_champ = champion_wins[
            champion
        ]

        wr = (
            wins_for_champ / games
        ) * 100

        print()
        print(champion)
        print(f"Games: {games}")
        print(f"Wins: {wins_for_champ}")
        print(f"Win Rate: {wr:.1f}%")

    print("\nMatchup Summary:")

    for (
        champion,
        opponent
    ), games in sorted(
        matchup_counts.items(),
        key=lambda x: x[1],
        reverse=True,
    )[:20]:

        wins_in_matchup = matchup_wins[
            (champion, opponent)
        ]

        wr = (
            wins_in_matchup / games
        ) * 100

        print(
            f"{champion} vs {opponent}: "
            f"{games} games, "
            f"{wins_in_matchup} wins, "
            f"{wr:.1f}% WR"
        )

    while True:
        search_champion = input(
            "\nChampion Matchup Lookup (or EXIT): "
        ).strip()

        if search_champion.lower() in [
            "exit",
            "quit",
            "q",
        ]:
            print("Goodbye.")
            break

        print()
        print(f"{search_champion} Matchups")

        found = False

        for (
            champion,
            opponent
        ), games in sorted(
            champion_matchups.items(),
            key=lambda x: x[1],
            reverse=True,
        ):

            if champion.lower() != search_champion.lower():
                continue

            found = True

            wins_for_matchup = champion_matchup_wins[
                (champion, opponent)
            ]

            wr = wins_for_matchup / games * 100

            print()
            print(f"vs {opponent}")
            print(f"{games} Games")
            print(f"{wr:.1f}% Win Rate")

        if not found:
            print("No games found for that champion.")


if __name__ == "__main__":
    main()
