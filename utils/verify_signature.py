# /usr/bin/env python3
# -*- coding: UTF-8 -*-


"""

Author: samzong.lu
E-mail: samzong.lu@gmail.com

"""

import hashlib


def verify_signature(token, msg_signature, msg_timestamp, msg_nonce, msg_encrypt):
    sort_list = [token, msg_timestamp, msg_nonce, msg_encrypt]
    sort_list.sort()
    sort_string = "".join(sort_list)

    return hashlib.sha1(sort_string.encode('utf-8')).hexdigest() == msg_signature


if __name__ == '__main__':
    pass
