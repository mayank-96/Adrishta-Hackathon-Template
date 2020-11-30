from flask import Flask, render_template
from chess_engine import *
from stockfish import Stockfish
import chess
import chess.engine
import re
board=chess.Board()
stockfish = Stockfish("stockfish.exe")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/move/<int:depth>/<path:fen>/')
def get_move(depth, fen):
    print(depth)
    engine1 = chess.engine.SimpleEngine.popen_uci("stockfish.exe")
    stockfish.set_fen_position(fen)
    board.set_fen(fen)
    print(fen)
    print("Calculating...")
    engine = Engine(fen)
    move = engine.iterative_deepening(depth - 1)
    move = stockfish.get_best_move()
    print("Move found!", move)
    x1=chess.Move.from_uci(move)
    board.push(x1)
    x=board.fen()
    stockfish.set_fen_position(x)
    smove=stockfish.get_best_move()
    print("suggested move is : ",smove)
    print()
    info = engine1.analyse(board, chess.engine.Limit(depth=20))
    score_str=str(info["score"])
    result = [int(d) for d in re.findall(r'-?\d+', score_str)]
    res=result[0]
    wprob=1/(1+(10**((1-res)/4)))
    print("Win Probability of White is : ",wprob)
    # result= stockfish.get_evaluation()
    # print(result)
    return move,smove


@app.route('/test/<string:tester>')
def test_get(tester):
    return tester


if __name__ == '__main__':
    app.run(debug=True)