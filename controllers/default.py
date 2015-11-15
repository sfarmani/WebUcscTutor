# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

import json
import httplib

appId = "sm3IJPOksqi4vIIN99wmppWnGWFZ0lvsVLNQ9VuO"
apiKey = "4udDwLuCkvJLR09ypSp1xsgKKVwBDmncRSRBd24K"


def get_info(strng):
    return strng
    # if strng == "get users":
    #     connection = httplib.HTTPSConnection('api.parse.com', 443)
    #     connection.connect()
    #     connection.request('GET', '/1/users', '', {
    #            "X-Parse-Application-Id": appId,
    #            "X-Parse-REST-API-Key": apiKey
    #          })
    #     return json.loads(connection.getresponse().read())
    # elif strng == "signup as tutor":
    #     connection = httplib.HTTPSConnection('api.parse.com', 443)
    #     connection.connect()
    #     connection.request('POST', '/1/users', json.dumps({
    #            "username": "cooldude6",
    #            "password": "p_n7!-e8",
    #            "phone": "415-392-0202"
    #          }), {
    #            "X-Parse-Application-Id": appId,
    #            "X-Parse-REST-API-Key": apiKey,
    #            "X-Parse-Revocable-Session": "1",
    #            "Content-Type": "application/json"
    #          })
    #     return json.loads(connection.getresponse().read())


def index():
    users = get_info("get users")
    session.users = users
    return dict(users=users)


def name_list():
    users = get_info("get users")
    session.users = users

    return dict(users=users)



