# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

import json
import httplib

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


def index():
    return dict()


def name_list():
    users = get_info("get users")
    session.users = users
    return dict(users=users)


def editprof():
    return dict()

