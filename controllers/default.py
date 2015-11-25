# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

import json
import httplib
import re

appId = "sm3IJPOksqi4vIIN99wmppWnGWFZ0lvsVLNQ9VuO"
apiKey = "4udDwLuCkvJLR09ypSp1xsgKKVwBDmncRSRBd24K"


def get_info(strng):
    if strng == "get users":
        connection = httplib.HTTPSConnection('api.parse.com', 443)
        connection.connect()
        connection.request('GET', '/1/users', '', {
               "X-Parse-Application-Id": appId,
               "X-Parse-REST-API-Key": apiKey
        })
        return json.loads(connection.getresponse().read())
    elif strng == "get messages":
        connection = httplib.HTTPSConnection('api.parse.com', 443)
        connection.connect()
        connection.request('GET', '/1/classes/ParseMessage', '', {
               "X-Parse-Application-Id": appId,
               "X-Parse-REST-API-Key": apiKey
        })
        # print json.loads(connection.getresponse().read())
        return json.loads(connection.getresponse().read())


def index():
    return dict()


def name_list():
    users = get_info("get users")
    session.users = users
    return dict(users=users)


def editprof():
    return dict()


def messaging():
    users = get_info("get users")
    session.users = users
    return dict(users=users)


def message_user():
    # replace non-alphanumeric characters from args with spaces
    title = request.args(0)
    tutor_name = re.sub('[^0-9a-zA-Z]+', ' ', title)

    users = get_info("get users")
    session.users = users

    messages = get_info("get messages")
    # session.messages = messages
    return dict(tutor_name=tutor_name, users=users, messages=messages)


