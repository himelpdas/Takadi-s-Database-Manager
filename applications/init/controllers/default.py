# -*- coding: utf-8 -*-

def index():
    response.flash = T("Welcome CSCI 380!")
    response.title="Takadi's Database Manager"
    message = 'Please %s the database'
    welcome = "Welcome%s!"
    if IS_ADMIN:
        message = message % "use the navigation bar above to edit"
        welcome = welcome % " administrator, %s" % auth.user.first_name.capitalize()
    elif auth.is_logged_in():
        message = message % "use the navigation bar above to view"
        welcome = welcome % ", %s" % auth.user.first_name.capitalize()
    else:
        message = message % "register/login to access"
        welcome = welcome % ", %s" % "Guest"
    return dict(welcome = welcome, message=message)

response.title = request.function.capitalize()

@auth.requires_login()
def costume():
    grid = SQLFORM.grid(db.costume,
               editable = IS_ADMIN,
               deletable = IS_ADMIN,
               create = IS_ADMIN,
                       )
    return dict(grid=grid)

@auth.requires_login()
def customer():
    grid = SQLFORM.grid(db.customer,
               editable = IS_ADMIN,
               deletable = IS_ADMIN,
               create = IS_ADMIN,
                       )
    return dict(grid=grid)

@auth.requires_login()
def order():
    db.customer.id.readable = False
    db.costume.id.readable = False

    rental = db((db.rental.customer==db.customer.id) &
                (db.rental.costume==db.costume.id))

    grid = SQLFORM.grid(rental,
               editable = IS_ADMIN,
               deletable = IS_ADMIN,
               create = IS_ADMIN,
               field_id = db.rental.id,
               )

    return dict(grid=grid)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
