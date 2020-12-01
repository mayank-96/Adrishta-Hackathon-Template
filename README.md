## Team Number \29 - \Check & Mate

The participants are required to fork this repository and create a public Github repository under their own username (Single repository per team). *Clone the repo on your local system and build on top of that*

The following created sections in this README.md need to be duly filled, highlighting the denoted points for the solution/implementation. 

**Please feel free to create further sub-sections in this markdown.** The idea is to understand all the particulars of your solution in a singular document.

### Project Overview

A brief description of 
* As Mentioned in the title, We have tried to create an application that helps chess players newbies and seasoned veterans alike to improve their game.
* We have created a web app that allows the users to play against a bot and analyse their every move to get better.

### Solution Description
  * We use the Stockfish Chess engine to provide the user with a bot with difficulty levels ranging from a 1200 rating bot to a Grandmaster Level bot.
  * The Web App shows various information regarding the game as it progresses like the current winning probability, Mistakes, Inaccuracies, Blunders and Also an option to get the best possible move at the given Board State.
  
#### Architecture Diagram

https://ibb.co/qB0TJTR

#### Technical Description

An overview of:
* The overall application is written in Flask Framework based on Python.
  We have used ChessboardJS for rendering the Chessboard and Python Chess and Stockfish libraries for the move evaluation and Other Functions.
  The App is deployed using Heroku platform making it easier to access by anyone over the internet.
* Since We Have already deployed a production version of the web app there are no setups required other than a internet browser and an active internet connection.
* The site can be accessed at : 
### Screenshots
Affix the relevant screenshots of the developed project here.

### Team Members
|Member Name        |     Email                 |        Contribution         |
|-------------------|---------------------------|-----------------------------|
|Mayank Pagar       |pagarmayank07@gmail.com    |Flask Application Development|
|Anirudh V.S.P      |anirudhvsp@gmail.com       |Chess Engine Integration     |
|Harsh Kumar Pandey |pandeyharsh1999@gmail.com  |FrontEnd Development         |

### References
Affix links to the online tools/repositories/blogs etc., which helped you along the development of the project
 * https://chessboardjs.com/  - for drawing the board
 * https://pypi.org/project/stockfish/ - for calculating and evaluating moves
 * https://pypi.org/project/chess/ - for Board Parsing and manipulation
 * https://www.chessprogramming.org/Pawn_Advantage,_Win_Percentage,_and_Elo - for providing very useful insights on calculating Win probability and Pawn Advantage
