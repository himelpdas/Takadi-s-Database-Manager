# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

response.logo = A(B('Tak',  #favicon.cc/
                    IMG(_src=XML('data:image/x-icon;base64,AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAACviQAws4sL78WfNf/Tr1T/069U/9OvVP/Tr1T/069U/9OvVP/Tr1T/069U/9OvVP/Tr1T/xZ81/7OLC++viQAws4sL7/TXnv/53aj/+d2o//rgsP/647j/+uO4//rjuP/647j/+uO4//rjuP/647j/+uCw//ndqP/0157/s4sL78upS//98+D//vbo//726P/+9uj//vbo//726P/+9uj//vbo//726P/+9uj//vbo//726P/64rT/+d2o/8CZKv/EqDr//vbo//726P/+9uj//vbo//726P/+9uj//vbo//726P/+9uj//vbo//726P/+9uj/++jE//ndqP/Bmir/sI4Az+vcrv/+9uj//vbo//726P/+9uj//vbo//726P/+9uj//vbo//726P/+9uj//vbo//rgsP/mxn7/roQAz7COADCwjgCvv6Is/8SoOv/EqDr/xKg6/8SoOv/EqDr/xKg6/8SoOv/EqDr/xKg6/8KjNv+8lSD/jGsh37COADAAAAAAAAAAABUPrv8eF83/HhfN/x4Xzf8eF83/HhfN/x4Xzf8eF83/HhfN/woHpP8uInH/LiJx/x8WZr8AAAAAAAAAAAAAAAATDae/HhfN/x4Xzf8eF83/HhfN/x4Xzf8eF83/HhfN/x0XrP+NaRz/yqZH/9OvVP+7kSD/rYAAYAAAAAAAAAAAEw2njxsVxP8eF83/HhfN/x4Xzf8bFMb/DQqr/wYFnf9PP1T/18J0//726P/87tT/9Nee/7eMFu8AAAAAAAAAABMNp2AZE7z/HhfN/x4Xzf8WELz/AwKW/wMClv8FA5j/XktP/+vcrv/+9uj//vbo//voxP/Alyr/AAAAAAAAAAATDadAGRK6/x4Xzf8eF83/BgWd/wMClv8MCKD/FhC0/15LeP/XwnT//vbo//726P/46Mr/soYL7wAAAAAAAAAAEw2nIBYQsf8eF83/HhfN/wQDl/8QC6T/HBXK/yQc7f8kHO3/jXI7/821V//XwnT/uJId/62AAGAAAAAAAAAAAAAAAAATDafPHRbL/xgSwP8QC6T/HhbT/yQc7f8kHO3/JBzt/yQc7f9HObL/RTep/y0gi78AAAAAAAAAAAAAAAAAAAAAEw2nYBkSuv8XEbf/HBXK/yQc7f8kHO3/JBzt/yQc7f8kHO3/JBzt/x4W0/8TDadwAAAAAAAAAAAAAAAAAAAAAAAAAAATDafPFQ+w/yMb6f8kHO3/JBzt/yQc7f8kHO3/JBzt/yAY3P8UDqzvEw2nIAAAAAAAAAAAAAAAAAAAAAAAAAAAEw2nEBMNp88XEbn/FxG5/xcRuf8XEbn/FxG5/xUPsO8TDaefEw2nMAAAAAAAAAAAgAEAAAAAAAAAAAAAAAAAAAAAAACAAQAAwAEAAMABAADAAAAA4AAAAOAAAADgAQAA4AEAAPADAADwAwAA+AcAAA=='), _rel="icon", _type="image/x-icon")), "di's", XML('&trade;&nbsp;'),
                  _class="navbar-brand", _href=URL("init", "default", "index.html"),
                  _id="web2py-logo")
response.title = request.application.replace('_', ' ').title()
response.subtitle = ''

# ----------------------------------------------------------------------------------------------------------------------
# read more at http://dev.w3.org/html5/markup/meta.name.html
# ----------------------------------------------------------------------------------------------------------------------
response.meta.author = myconf.get('app.author')
response.meta.description = myconf.get('app.description')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')

# ----------------------------------------------------------------------------------------------------------------------
# your http://google.com/analytics id
# ----------------------------------------------------------------------------------------------------------------------
response.google_analytics_id = None

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), request.function=="index", URL('default', 'index'), []),
    (T('Customer Information'), request.function=="customer", URL('default', 'customer'), []),
    (T('Costumes in Inventory'), request.function=="costume", URL('default', 'costume'), []),
    (T('Customer Order'), request.function=="order", URL('default', 'order'), []),
]

IS_ADMIN = bool(getattr(auth.user, "email", "").lower() in map(lambda e: e.lower(), ["himeldas@live.com", "makhtar@nyit.edu", "ahussa08@nyit.edu", "ahasan12@nyit.edu", "gsingh44@nyit.edu"]))


DEVELOPMENT_MENU = False


# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. remove in production
# ----------------------------------------------------------------------------------------------------------------------

def _():
    # ------------------------------------------------------------------------------------------------------------------
    # shortcuts
    # ------------------------------------------------------------------------------------------------------------------
    app = request.application
    ctr = request.controller
    # ------------------------------------------------------------------------------------------------------------------
    # useful links to internal and external resources
    # ------------------------------------------------------------------------------------------------------------------
    response.menu += [
        (T('My Sites'), False, URL('admin', 'default', 'site')),
        (T('This App'), False, '#', [
            (T('Design'), False, URL('admin', 'default', 'design/%s' % app)),
            LI(_class="divider"),
            (T('Controller'), False,
             URL(
                 'admin', 'default', 'edit/%s/controllers/%s.py' % (app, ctr))),
            (T('View'), False,
             URL(
                 'admin', 'default', 'edit/%s/views/%s' % (app, response.view))),
            (T('DB Model'), False,
             URL(
                 'admin', 'default', 'edit/%s/models/db.py' % app)),
            (T('Menu Model'), False,
             URL(
                 'admin', 'default', 'edit/%s/models/menu.py' % app)),
            (T('Config.ini'), False,
             URL(
                 'admin', 'default', 'edit/%s/private/appconfig.ini' % app)),
            (T('Layout'), False,
             URL(
                 'admin', 'default', 'edit/%s/views/layout.html' % app)),
            (T('Stylesheet'), False,
             URL(
                 'admin', 'default', 'edit/%s/static/css/web2py-bootstrap3.css' % app)),
            (T('Database'), False, URL(app, 'appadmin', 'index')),
            (T('Errors'), False, URL(
                'admin', 'default', 'errors/' + app)),
            (T('About'), False, URL(
                'admin', 'default', 'about/' + app)),
        ]),
        ('web2py.com', False, '#', [
            (T('Download'), False,
             'http://www.web2py.com/examples/default/download'),
            (T('Support'), False,
             'http://www.web2py.com/examples/default/support'),
            (T('Demo'), False, 'http://web2py.com/demo_admin'),
            (T('Quick Examples'), False,
             'http://web2py.com/examples/default/examples'),
            (T('FAQ'), False, 'http://web2py.com/AlterEgo'),
            (T('Videos'), False,
             'http://www.web2py.com/examples/default/videos/'),
            (T('Free Applications'),
             False, 'http://web2py.com/appliances'),
            (T('Plugins'), False, 'http://web2py.com/plugins'),
            (T('Recipes'), False, 'http://web2pyslices.com/'),
        ]),
        (T('Documentation'), False, '#', [
            (T('Online book'), False, 'http://www.web2py.com/book'),
            LI(_class="divider"),
            (T('Preface'), False,
             'http://www.web2py.com/book/default/chapter/00'),
            (T('Introduction'), False,
             'http://www.web2py.com/book/default/chapter/01'),
            (T('Python'), False,
             'http://www.web2py.com/book/default/chapter/02'),
            (T('Overview'), False,
             'http://www.web2py.com/book/default/chapter/03'),
            (T('The Core'), False,
             'http://www.web2py.com/book/default/chapter/04'),
            (T('The Views'), False,
             'http://www.web2py.com/book/default/chapter/05'),
            (T('Database'), False,
             'http://www.web2py.com/book/default/chapter/06'),
            (T('Forms and Validators'), False,
             'http://www.web2py.com/book/default/chapter/07'),
            (T('Email and SMS'), False,
             'http://www.web2py.com/book/default/chapter/08'),
            (T('Access Control'), False,
             'http://www.web2py.com/book/default/chapter/09'),
            (T('Services'), False,
             'http://www.web2py.com/book/default/chapter/10'),
            (T('Ajax Recipes'), False,
             'http://www.web2py.com/book/default/chapter/11'),
            (T('Components and Plugins'), False,
             'http://www.web2py.com/book/default/chapter/12'),
            (T('Deployment Recipes'), False,
             'http://www.web2py.com/book/default/chapter/13'),
            (T('Other Recipes'), False,
             'http://www.web2py.com/book/default/chapter/14'),
            (T('Helping web2py'), False,
             'http://www.web2py.com/book/default/chapter/15'),
            (T("Buy web2py's book"), False,
             'http://stores.lulu.com/web2py'),
        ]),
        (T('Community'), False, None, [
            (T('Groups'), False,
             'http://www.web2py.com/examples/default/usergroups'),
            (T('Twitter'), False, 'http://twitter.com/web2py'),
            (T('Live Chat'), False,
             'http://webchat.freenode.net/?channels=web2py'),
        ]),
    ]


if DEVELOPMENT_MENU:
    _()

if "auth" in locals():
    auth.wikimenu()
