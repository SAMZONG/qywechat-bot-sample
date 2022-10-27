# /usr/bin/env python3
# -*- coding: UTF-8 -*-


"""

Author: samzong.lu
E-mail: samzong.lu@gmail.com

"""

import base64
from Crypto.Cipher import AES
from flask import Flask, request
from WXBizJsonMsgCrypt import WXBizJsonMsgCrypt
from utils.verify_signature import verify_signature

import re
import time
import hashlib
import socket
import struct
import string
import random

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/qywxbot/callbak', methods=['GET', 'POST'])
def qywxbot_callbak():
    data = request.args

    token = "435e1Jo1v5V"
    encoding_aes_key = "WXcTP6xzWGpK7V"
    corp_id = "9db93"

    wxcpt = WXBizJsonMsgCrypt(token, encoding_aes_key, corp_id)

    msg_signature = data['msg_signature']
    msg_timestamp = data['timestamp']
    msg_nonce = data['nonce']
    msg_encrypt = data['echostr']

    def aes_decrypt(msg_encrypt: str, encoding_aes_key: str) -> str:
        """
        AES算法解密信息
        """
        aes_msg = base64.b64decode(msg_encrypt)  # 对密文base64解码
        aes_key = base64.b64decode(encoding_aes_key + "=")  # EncodingAESKey转AESKey
        random_msg = AES.new(aes_key, AES.MODE_CBC, AES.MODE_CBC, aes_key[0:16]).decrypt(aes_msg)  # 使用AESKey做AES解密
        pad_num: int = random_msg[-1]  # 去掉补位字符串
        return random_msg[:-pad_num].decode()

    print(msg_encrypt, "11111111111", encoding_aes_key)
    msg = aes_decrypt(msg_encrypt, encoding_aes_key)
    print(msg)

    if verify_signature(token, msg_signature, msg_timestamp, msg_nonce, msg_encrypt):
        print(msg_signature)

    return '{}'.format(msg_signature)


if __name__ == '__main__':
    app.run(debug=True, port=5010)
