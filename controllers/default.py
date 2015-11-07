# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

import json
import urllib2


def get_emails(url):
    """This Python function is not a controller.  A function defines a controller in web2py
    iff it does not take any arguments.  This function takes arguments, and so it's a normal
    function you can call from your controllers."""
    try:
        r = urllib2.urlopen(url)
        email_list = json.load(r)
        r.close()
    except Exception, e:
        email_list = []
        session.message = T('Error in contacting server')
    return email_list


def index():
    """
    Displays list of all emails.
    """
    # Gets some fresh set of emails each time.
    email_list = get_emails('http://luca-teaching.appspot.com/fake_emails/default/get_emails')
    # We store the list of emails in the session.
    session.email_list = email_list
    # At this point, email_list is a list of dictionaries of this format:
    #     {
    #         'id': 'randomstringid',
    #         'from': 'sender@email.com',
    #         'date': 'somedateinISOformat',
    #         'subject': 'Your homework.',
    #         'text': 'Text of email, with \n\n used to separate paragraphs',
    #         'starred': True, # or False!
    #         'read': False, # Whether you have read it or not, can be True or False
    #     }
    # And you need to display the list of emails.
    return dict(email_list=email_list)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())
