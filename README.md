
# Magnus Carlsen Chess Games Data Analysis

Magnus Carlsen's chess game data analysis project involves studying and identifying patterns in his games using historical data. I'm focusing on several keys:

**Games Played Per Year/Month**: Analyzing the frequency of games Magnus Carlsen has played over time, identifying how his activity varies across different periods.

**Openings Used**: looking into the chess openings, investigating whether there are particular openings he favors and if there are any trends in how often he uses them.

**Time Controls**: Examining the types of time controls he plays under, such as how often he participates in rapid, blitz, or classical games. A specific example would be checking how frequently he plays 3-minute games.

**Win/Loss Patterns**: Analyzing how Magnus Carlsen wins or loses games. This includes understanding how many of his victories are achieved by checkmate, resignation, or other methods, and similarly, how he loses games.



## Data Collection

For the Data analysis project, the data collection process involved gathering a comprehensive dataset of his historical chess games. The following steps outline the process:



1. **Source of Data**: 
   The data was sourced from reputable online chess database such as *Chess.com*, which store detailed game records of professional players. These databases offer game archives that include information on Event, Site, Date, Round, White, Black, Result, CurrentPosition, Timezone, ECO, ECOUrl, UTCDate, UTCTime, WhiteElo, BlackElo, TimeControl, Termination, StartTime, EndDate, EndTime, Link, Moves.



2. **Game Attributes**: 
   The dataset includes various attributes related to each game:
- *Event:* indicating the match was played live on Chess.com.
- *Site:* "Chess.com" (the platform where the game was played).
- *Date:* The exact date when the game was played.
- *Round:* "-" (no specific round, as it is a casual online game).
- *White:* The White player.
- *Black:* The Black player.
- *Result:* 1-0 (white win- Black lose), 1/2-1/2 (Draw).
- *Current Position:* A FEN (Forsyth-Edwards Notation) string      representing the final position of the game after the Player’s checkmate.
- *Timezone:* UTC (the game was played in Coordinated Universal Time).
- *ECO*: Encyclopaedia of Chess Openings.
- *ECO URL:* A link to a resource on Chess.com explaining various Openings.
- *UTCDate:* same as the game date.
- *UTCTime:* The start time of the game in UTC.
- *WhiteElo:* White player rating.
- *BlackElo:* Black player rating.
- *TimeControl:* The Game's Duration, is categorized into classical, rapid, blitz, and bullet time formats.
- *Termination:* Players victory by checkmate, resignation, time, Game-abandoned, and Draw.
- *StartTime:* The game’s start time.
- *EndDate:* The game’s End Date.
- *EndTime:* The time when the game ended.
- *Link:* A URL to the game on Chess.com.
   
3. **Data Format**:
   The data was exported in a standardized format such as PGN (Portable Game Notation), which is commonly used to record chess games. Additional formats like CSV or Excel spreadsheets were used for organizing and analyzing the game statistics.

4. **Data Cleaning**:
   Before analysis, the dataset was cleaned to ensure accuracy and consistency. This involved:
- Removing duplicate games or entries.
- Verifying game results and outcomes.
- Standardizing opening names and time control labels to facilitate better grouping and comparison.

5. **Time Frame**: 
   The data spans multiple years of Carlsen’s career, providing a long-term view of his chess-playing patterns. For more granular analysis, the games were grouped by month and year.

This collection of data serves as the foundation for analyzing trends in Carlsen’s chess strategies, performance, and playing habits over time.



## About Data
**Games Played Year by Magnus in chess.com**: 2016, 2017, 2018, 2020, 2021, 2022, 2023, 2024

**Total Games by Magnus**: 5765
- *Bullet* - 1538
- *Blitz* - 3983
- *Rapid* - 244

**Total Chess Openings with variations by Magnus**: 1316



## Use

- You can use my data collection to analyze Magnus Carlsen's games (link: https://github.com/mayurnix/Magnus-Carlsen-Chess-Games-Data-Analysis/blob/main/chess_games3.csv) 
- You can use my Python file to download other player data in pgn formate (link: https://github.com/mayurnix/Magnus-Carlsen-Chess-Games-Data-Analysis/blob/main/magnusdata_from_chesscom.py)



## 🛠 Skills
Python, Data Analysis, MS Excel, Microsoft Power BI

