


import requests
import os
from datetime import datetime
import time

# Magnus Carlsen's username on Chess.com
USERNAME = "MagnusCarlsen"

# Function to download games for a specific month
def download_games(year, month):
    url = f"https://api.chess.com/pub/player/{USERNAME}/games/{year}/{month:02d}"
    headers = {
        "User-Agent": "Enter Your user agent"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # print(1)
        if 'games' in data:
            return data['games']
    else:
        print(f"Failed to download games: {response.status_code}")
    return []

# Function to save games in PGN format
def save_games_pgn(games, file_path):
    with open(file_path, 'a') as f:
        for game in games:
            if 'pgn' in game:
                f.write(game['pgn'] + '\n\n')

# Main function to download all games and save them
def download_all_games():
    if not os.path.exists('chess_games'):
        os.makedirs('chess_games')
    
    current_year = datetime.now().year
    current_month = datetime.now().month
    file_path = f"chess_games/{USERNAME}_all_games.pgn"
    
    for year in range(2014, current_year + 1):
        for month in range(1, 13):
            if year == current_year and month > current_month:
                break
            # print(f"Downloading games for {year}-{month:02d}")
            games = download_games(year, month)
            if games:
                save_games_pgn(games, file_path)
                print(f"Saved {len(games)} games for {year}-{month:02d}")
            # else:
                # print(f"No games found for {year}-{month:02d}")
            time.sleep(1)

if __name__ == "__main__":
    download_all_games()