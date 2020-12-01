import os
import tempfile
import json
import chess
import engine

import pytest

from server import app

@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def post_json(client, url, json_dict):
    return client.post(url, data=json.dumps(json_dict), content_type='application/json')

def json_of_response(response):
    return json.loads(response.data.decode('utf8'))

def test_new_game(client):
    response = client.get('/new_game')
    json_response = json_of_response(response)
    assert json_response['board'] == "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    assert response.status_code == 200

def test_random_move_api(client):
    response = post_json(client, '/random_move', {'board': chess.Board().fen()})
    json_response = json_of_response(response)
    assert len(json_response['board']) > 30
    assert response.status_code == 200

def test_best_random_move_api(client):
    response = post_json(client, '/best_random_move', {'board': 'rnbqkbnr/ppp1pppp/8/3p4/3PP3/8/PPP2PPP/RNBQKBNR b KQkq - 0 1'})
    json_response = json_of_response(response)
    assert json_response['board'] == 'rnbqkbnr/ppp1pppp/8/8/3Pp3/8/PPP2PPP/RNBQKBNR w KQkq - 0 2'
    assert response.status_code == 200

def test_best_minimax_move_api(client):
    response = post_json(client, '/best_minimax_move', {'board': 'rnbqkbnr/ppp1pppp/8/3p4/3PP3/8/PPP2PPP/RNBQKBNR b KQkq - 0 1'})
    json_response = json_of_response(response)
    assert json_response['board'] == 'rnbqkbnr/ppp1pppp/8/8/3Pp3/8/PPP2PPP/RNBQKBNR w KQkq - 0 2'
    assert response.status_code == 200

def test_score(client):
    minmax = engine.Minmax()
    assert minmax.calculate_score() == 0
    minmax.set_board('4k3/8/8/8/8/8/4P3/4K3 w - - 5 39')
    assert minmax.calculate_score() == 10

def test_best_move(client):
    minmax = engine.Minmax('rnbqkbnr/ppp1pppp/8/3p4/3PP3/8/PPP2PPP/RNBQKBNR b KQkq - 0 1')
    assert minmax.calculate_best_move() == 'd5e4'

