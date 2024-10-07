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

**Games Played by Magnus in chess.com**: 14/12/2014 to 21/09/2024

**Total Games by Magnus**: 5765

## Outcomes
**Total Types of Games Played by Magnus **
- *Bullet* - 1538 (1 total games 1163, 1|1 total games 375) (1 minutes per player | increment of one second per move)  
- *Blitz* - 3983 (3 minute's total games 2537, 3|1 minute's total games 1106, 3|2 minute's total games 103, 5 minute's total games 44, 5|1 minute's total games 128, 5|2 minute's total games 65)
- *Rapid* - 244 (10 minute's total games 7, 10|2 minute's total games 95, 15 minute's total games 7, 15|2 minute's total games 52, 15|3 minute's total games 72, 25|25 minute's total games 11)

**Total Types of Chess Openings with variations by Magnus**: 1316
  - Alapin Sicilian Defense, Alekhines Defense, Amar Opening, Anderssen Opening, Barnes Opening, Benko Gambit, Benoni Defense, Birds Opening, Bishops Opening Berlin, Bogo Indian Defense, Budapest Gambit, Caro Kann Defense, Catalan Opening, Center Game, Clemenz Opening, Closed Sicilian Defense, Colle System, Danish Gambit, Dutch Defense, English Defense, English Opening, Englund Gambit, Four Knights Game, French Defense, Giuoco Piano Game, Grob Opening, Grunfeld Defense, Indian Game, Italian Game, Kadas Opening, Kings Fianchetto Opening, Kings Gambit Accepted Bishops Gambit, Kings Indian Attack, Kings Indian Defense, Kings Pawn Opening, Lion Defense Anti Philidor Lions Cave Variation, London System, Magnus Sicilian, Mieses Opening 1, Modern Defense, Neo Grunfeld Defense, Nimzo Indian Defense, Nimzowitsch Defense, Nimzowitsch Larsen Attack, Old Benoni Defense, Old Indian Defense, Owens Defense, Petrovs Defense, Philidor Defense, Pirc Defense, Polish Opening, Ponziani Opening, Queens Gambit Accepted, Queens Gambit Declined, Queens Indian Defense, Queens Pawn Opening, Reti Opening, Richter Veresov Attack 3, Ruy Lopez Opening Alapin Defense, Saragossa Opening, Scotch Game, Semi Slav Defense, Sicilian Defense, Slav Defense, Sodium Attack, Tarrasch Defense, Three Knights Opening, Torre Attack, Trompowsky Attack, Van Geet Opening, Van t Kruijs Opening 1, Vienna Game, Ware Opening.


**Opponents(chess.com user names)**: 163 
  - 12teen, aa175, abhijeetgupta1016, Abund, Adar_07, agser, AhmadzadaA, Alexander_Zubov, alexrustemov, ALieRaiseAFireOozeUh, amintabatabaei, Andreikka, AnthonyWirig, Antipov_Mikhail_Al, artin10862, artooon, AryanTari, Azerichess, BardArtem, bascheyaro, Bauman_Guy, Bigfish1995, BillieKimbah, BilodeauA, bipe137, Blitzstream, BlueWizzard, BogdanDeac, BrandonJacobson, Bulldog167, BuLolo, ChessBrah, ChessLover0108, ChessWarrior7197, Chesswizard_2007, chito89, Chopper1905, ChristopherYoo, DanielDardha2005, DanielNaroditsky, DenLaz, DonkyDonkyDonkey, dretch, dropstoneDP, DrVelja, Duhless, DuleMudule, eljanov, Elprofessor21, Elsa167, EltajSafarli, exoticprincess, FabianoCaruana, FairChess_on_YouTube, Fandorine, Firouzja2003, fizmat_64, FormerProdigy, frederiksvane, garcho08, GeorgMeier, GGuseinov, GHANDEEVAM2003, GM_dmitrij, GMBenjaminBok, gmwesley_so, GMWSO, GOGIEFF, Grischuk, GroovyKettle, gurelediz, hansen, HansOnTwitch, Harsha_Bharathakoti, Haykoooo0o, HeartAblaze, Hikaru, ilqar_74, Indianlad, Iskusnyh, iturrizaga, jefferyx, JNWDUBDGBE, joppie2, Jospem, K_A_S_T_O_R, Kacparov, KazakhFighter04, kirillshevchenko, KNVB, Konavets, Krakozia, lachesisQ, LacusSomniorum, legendisback1, LevonAronian, LiemLe, LLavash, LPSupi, LyonBeast, Man-Chuk, Manukyan_Artak, MarcoRiehle, Marcus_Harvey, Masmos97, mbojan, Meri-Arabidze, MFBerna, Michelangelo, mishanick, MITerryble, MKlose11, moro182, Msb2, Neferpitou27, NeMeQuittePas, NevorLegov, nihalsarin, NikoTheodorou, Njal28, OhanyanEminChess, Oleksandr_Bortnyk, Parhamov, pasteta13, penguingm1, Philippians46, platy3, Polish_fighter3000, Prizant_academy, promen1999, Proverbs163, rasmussvane, RaunakSadhwani2005, rednova1729, RojonR, Rud_Makarian, SahajGrover, SantoBlue, scarabee43, SchmakAttack, SenorNadie, sergoy, ShimanovAlex, Sibelephant, sokidze, SpeedofLight0, spicycaterpillar, Statham, TigranLPetrosyan, TigrVShlyape, Tobias_Koelle, Tobi-Wan-Kenobi, vi_pranav, viditchess, VincentKeymer, Volodar_Murzin, vugarrasulov, WiniVidiVici, wonderfultime, XDPS, xxysoul6, yosephtaher, Zhigalko_Sergei.


## Use

- You can use my data collection to analyze Magnus Carlsen's games (link: https://github.com/mayurnix/Magnus-Carlsen-Chess-Games-Data-Analysis/blob/main/chess_games3.csv) 
- You can use my Python file to download other player data in pgn format (link: https://github.com/mayurnix/Magnus-Carlsen-Chess-Games-Data-Analysis/blob/main/magnusdata_from_chesscom.py)



## 🛠 Skills
Python, Jupyter Notebook, Data Analysis, MS Excel, Microsoft Power BI

