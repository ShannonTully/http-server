import requests
from cowpy import cow
import json


def test_server_sends_200_response():
    response = requests.get('http://127.0.0.1:3000')
    assert response.status_code == 200
    assert response.text == '''
<!DOCTYPE html>
<html>
<head>
    <title> cowsay </title>
</head>
<body>
    <header>
        <nav>
        <ul>
            <li><a href="/cowsay">cowsay</a></li>
        </ul>
        </nav>
    <header>
    <main>
        <!-- project description -->
    </main>
</body>
</html>
            '''


def test_server_sends_404_response():
    response = requests.get('http://127.0.0.1:3000/monkey')
    assert response.status_code == 404
    assert response.text == 'Not Found'


def test_server_sends_qs_back():
    response = requests.get('http://127.0.0.1:3000/cow?msg="Hello world"')
    assert response.status_code == 200
    assert response.text == cow.Moose().milk('"Hello world"')


def test_server_post_sends_back_json():
    response = requests.post('http://127.0.0.1:3000/cow?msg="Hello world"')
    assert response.status_code == 200
    content = {
                'content': cow.Moose().milk('"Hello world"')
            }
    assert response.text == json.dumps(content)


def test_server_sends_400_back():
    response = requests.get('http://127.0.0.1:3000/cow?broke="Hello world"')
    assert response.status_code == 400
