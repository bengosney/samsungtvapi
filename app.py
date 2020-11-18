import samsungctl
from flask import Flask, abort, jsonify, request

app = Flask(__name__)

config = {
    "name": "Web API",
    "description": "Web API",
    "id": "",
    "host": "192.168.1.107",
    "port": 55000,
    "method": "legacy",
    "timeout": 0,
}

validCodes = [
    'KEY_POWEROFF',
    'KEY_UP',
    'KEY_DOWN',
    'KEY_LEFT',
    'KEY_RIGHT',
    'KEY_CHUP',
    'KEY_CHDOWN',
    'KEY_ENTER',
    'KEY_RETURN',
    'KEY_CH_LIST',
    'KEY_MENU',
    'KEY_SOURCE',
    'KEY_GUIDE',
    'KEY_TOOLS',
    'KEY_INFO',
    'KEY_RED',
    'KEY_GREEN',
    'KEY_YELLOW',
    'KEY_BLUE',
    'KEY_PANNEL_CHDOWN',
    'KEY_VOLUP',
    'KEY_VOLDOWN',
    'KEY_MUTE',
    'KEY_0',
    'KEY_1',
    'KEY_2',
    'KEY_3',
    'KEY_4',
    'KEY_5',
    'KEY_6',
    'KEY_7',
    'KEY_8',
    'KEY_9',
    'KEY_DTV',
    'KEY_HDMI',
    'KEY_CONTENTS',
]


@app.route('/')
def home():
    return 'Old Samsung TV remote API'

@app.route('/api/')
def codes():
    return jsonify({'validCodes': validCodes})

@app.route('/api/<string:keyCode>/', methods=['GET', 'POST'])
def tv(keyCode):
    print(f'requesting {keyCode}')
    keyCode = keyCode.upper()
    if keyCode not in validCodes:
        abort(404)

    with samsungctl.Remote(config) as remote:
        remote.control(keyCode)

    print(f'Pressed {keyCode}')
    return jsonify({'keyCode': keyCode, 'status': 'ok'})
