# -*- coding: utf-8 -*-
db.define_table("costume",
Field("name", requires=IS_NOT_IN_DB(db, 'costume.name')),
Field("color", requires=IS_IN_SET(["red", "orange", "blue", "purple", "green", "yellow", "white", "black", "grey", "silver", "gold", "teal"], zero=None, sort=True)),
Field("available", "boolean"),
auth.signature
)

db.define_table("customer",
Field("first_name"),
Field("last_name"),
Field("address"),
Field("telephone", requires=[IS_MATCH('\([0-9][0-9][0-9]\)[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]',
         error_message='Use the format (123)456-7890 (no spaces)'),
         IS_NOT_IN_DB(db, "customer.telephone")
                            ]),
auth.signature
)

db.define_table("rental",
Field("customer", db.customer, requires=IS_IN_DB(db, "customer.id", '%(first_name)s %(last_name)s (%(id)s)')),
Field("costume", db.costume, requires=IS_IN_DB(db, "costume.id", '%(name)s (%(id)s), Available=%(available)s')),
Field("rental_date", "date"),
Field("due_date", "date"),
auth.signature
)
