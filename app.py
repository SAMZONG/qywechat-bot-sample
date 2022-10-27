# /usr/bin/env python3
# -*- coding: UTF-8 -*-


"""

Author: samzong.lu
E-mail: samzong.lu@gmail.com

"""

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/qywxbot/callbak', methods=['GET', 'POST'])
def qywxbot_callbak():
    data = request.get_json()
    headers = request.headers

    print(data, '\n', headers)

    return {"code": 200, "message": 'qywxbot_callbak'}


if __name__ == '__main__':
    app.run(debug=True, port=5010)
