# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

import json
import httplib
import re
import urllib

appId = "sm3IJPOksqi4vIIN99wmppWnGWFZ0lvsVLNQ9VuO"
apiKey = "4udDwLuCkvJLR09ypSp1xsgKKVwBDmncRSRBd24K"


def get_info(strng):
    if strng == "get users":
        connection = httplib.HTTPSConnection('api.parse.com', 443)
        params = urllib.urlencode({
            "where": json.dumps({
                "isTutor": True
            })
        })
        connection.connect()
        connection.request('GET', '/1/classes/_User?%s' % params, '', {
               "X-Parse-Application-Id": "sm3IJPOksqi4vIIN99wmppWnGWFZ0lvsVLNQ9VuO",
               "X-Parse-REST-API-Key": "4udDwLuCkvJLR09ypSp1xsgKKVwBDmncRSRBd24K"
             })
        return json.loads(connection.getresponse().read())
    elif strng == "get messages":
        connection = httplib.HTTPSConnection('api.parse.com', 443)
        connection.connect()
        connection.request('GET', '/1/classes/ParseMessage', '', {
               "X-Parse-Application-Id": appId,
               "X-Parse-REST-API-Key": apiKey
        })
        return json.loads(connection.getresponse().read())


def index():
    curr_user_id = request.vars.currUserId
    return dict(curr_user_id=curr_user_id)


def name_list():
    # pass in args from the search button and query with those args. somehow
    users = get_info("get users")
    session.users = users
    return dict(users=users)


def editprof():
    return dict()


def messaging():
    users = get_info("get users")
    session.users = users

    curr_user_id = request.args(0)

    return dict(users=users, curr_user_id=curr_user_id)


def message_user():
    # replace non-alphanumeric characters from args with spaces
    title = request.args(0)
    tutor_name = re.sub('[^0-9a-zA-Z]+', ' ', title)

    users = get_info("get users")
    session.users = users

    curr_user_id = request.args(3)
    recipient_id = request.args(2)
    user_list = [curr_user_id, recipient_id]
    # print user_list
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    params = urllib.urlencode({
        "where": json.dumps({
            "senderId": {
                "$in": user_list
             },
            "recipientId": {
                 "$in": user_list
            }
        }),
        "order": "createdAt"
    })
    connection.connect()
    connection.request('GET', '/1/classes/ParseMessage?%s' % params, '', {
               "X-Parse-Application-Id": appId,
               "X-Parse-REST-API-Key": apiKey
    })

    messages = json.loads(connection.getresponse().read())
    # print messages
    # session.messages = messages
    return dict(tutor_name=tutor_name, users=users, messages=messages,curr_user_id=curr_user_id,  recipient_id=recipient_id)

def load_messages():
    sender_id = request.args(0)
    recipient_id = request.args(1)
    user_list = [sender_id, recipient_id]
    print user_list
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    params = urllib.urlencode({
        "where": json.dumps({
            "senderId": {
                "$in": user_list
             },
            "recipientId": {
                 "$in": user_list
            }
        }),
        "order": "createdAt"
    })
    connection.connect()
    connection.request('GET', '/1/classes/ParseMessage?%s' % params, '', {
               "X-Parse-Application-Id": appId,
               "X-Parse-REST-API-Key": apiKey
    })

    messages = json.loads(connection.getresponse().read())
    print messages
    return dict(messages=messages)


def tutorsignup():
    return dict()


def studentsignup():
    return dict()
