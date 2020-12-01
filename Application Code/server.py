from flask import Flask, render_template, jsonify, request
import chess
import engine
import random
import json
import chess.engine
from stockfish import Stockfish
import re

app = Flask(__name__)
stockfish= Stockfish()
engine1 = chess.engine.SimpleEngine.popen_uci("stockfish.exe")
stockfish.set_skill_level(0)

@app.route('/')
def index1():
    return render_template('index.html')

@app.route('/howtoplay')
def howtoplay():
    return render_template('howtoplay.html')

@app.route('/ng', methods = ['POST'])
def index():
    if request.method == 'POST':
        result = request.form
        stockfish.set_skill_level(int(result['points']))
        return render_template('index.html')

@app.route('/new_game')
def new_game():
    board = chess.Board()
    return jsonify({'board': str(board.fen())})

@app.route('/random_move', methods = ['POST'])
def random_move():
    print(request.data)
    json_post = request.get_json(force=True)
    if ("board" in json_post):
        board = engine.Minmax(json_post['board'])
        board.random_move()
    else:
        board = chess.Board()
    return jsonify({'board': str(board.get_fen())})

@app.route('/best_random_move', methods = ['POST'])
def best_random_move():
    json_post = request.get_json(force = True)
    if ("board" in json_post):
        board = engine.Minmax(json_post['board'])
        uci_move = board.calculate_best_move()
        board.move(uci_move)

    return jsonify({'board': str(board.get_fen())})

graph=[]
@app.route('/best_minimax_move', methods = ['POST'])
def best_minimax_move():
    json_post = request.get_json(force = True)
    if ("board" in json_post):
        board = engine.Minmax(json_post['board'])
        uci_move = board.calculate_best_minimax_move(2)
        board.move(uci_move)
        board1=chess.Board(str(json_post['board']))
        fen=board1.fen()
        stockfish.set_fen_position(fen)
        move2=stockfish.get_best_move()
        Nf3 = chess.Move.from_uci(move2)
        board1.push(Nf3)
        fen= board1.fen()
        stockfish.set_fen_position(fen)
        move = stockfish.get_best_move()
        # x1=chess.Move.from_uci(move)
        # board.push(x1)
        x=board1.fen()
        info = engine1.analyse(board1, chess.engine.Limit(depth=20))
        score_str=str(info["score"])
        result = [int(d) for d in re.findall(r'-?\d+', score_str)]
        res=result[0]
        graph.append(res)
        if(len(graph)>1):
            corn=graph[-2]-graph[-1]
            print(corn)
            if(corn in range(40,90)):
                cor="inaccuracy"
            elif(corn in range(90,200)):
                cor="Mistake"
            elif(corn in range (200,10000)):
                cor="Blunder"
            else:
                cor="Good Move"
        else:
            cor=" "
        wprob=1/(1+(10**((1-res)/4)))
        print(move,wprob)
        wprob = float("{:.4f}".format(wprob))

    return jsonify({'board': str(board.get_fen()) , 'pred' : str(move) , 'prob': str(wprob), 'correct':str(cor)})


if __name__ == '__main__':
    app.run(debug=True)