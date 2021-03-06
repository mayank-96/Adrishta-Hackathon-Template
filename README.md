## Check & Mate

### Project Overview

A brief description of 
* As Mentioned in the title, We have tried to create an application that helps chess players newbies and seasoned veterans alike to improve their game.
* We have created a web app that allows the users to play against a bot and analyse their every move to get better.

### Solution Description
  * We use the Stockfish Chess engine to provide the user with a bot with difficulty levels ranging from a 1200 rating bot to a Grandmaster Level bot.
  * The Web App shows various information regarding the game as it progresses like the current winning probability, Mistakes, Inaccuracies, Blunders and Also an option to get the best possible move at the given Board State.
  
### Architecture Diagram

![Architectural Diagram](https://user-images.githubusercontent.com/62810976/100753422-c0478b00-340f-11eb-87b5-dfcaa57f204a.PNG)

### Technical Description

An overview of:
* The overall application is written in Flask Framework based on Python.
  We have used ChessboardJS for rendering the Chessboard and Python Chess and Stockfish libraries for the move evaluation and Other Functions.
  The App is deployed using Heroku platform making it easier to access by anyone over the internet.
* Since We Have already deployed a production version of the web app there are no setups required other than a internet browser and an active internet connection.
* The site can be accessed at : 

### Screenshots
![1](https://user-images.githubusercontent.com/62810976/100769500-23dab400-3422-11eb-90fa-df9b45e43987.PNG)
![2](https://user-images.githubusercontent.com/62810976/100779292-2e9b4600-342e-11eb-8665-0f940520faa9.PNG)
![3](https://user-images.githubusercontent.com/62810976/100779295-30650980-342e-11eb-8a61-d4d7966b6096.PNG)

### How to run the project?

1. Install all the libraries mentioned in the [requirements.txt](https://github.com/mayank-96/Adrishta-Hackathon-Template/blob/master/Application%20Code/requirements.txt) file.
2. Clone this repository in your local system.
3. Open the command prompt from your project directory and run the command `python server.py`.
4. Go to your browser and type `http://127.0.0.1:5000/` in the address bar.
5. Hurray! That's it.

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
