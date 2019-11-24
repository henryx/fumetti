#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2019 Enrico Bianchi (enrico.bianchi@gmail.com)
# Project Name: fumetti
# Description   A RESTful API for managing a collection of comic books
# License       GPL version 2 (see LICENSE for details)
import os

from flask import Flask
from flask_cors import CORS

from routes import *
from utils import database

__author__ = "Enrico Bianchi"
__copyright__ = "Copyright 2019, Enrico Bianchi"
__credits__ = ["Enrico Bianchi", ]
__license__ = "GPLv2"
__maintainer__ = "Enrico Bianchi"
__email__ = "enrico.bianchi@gmail.com"
__status__ = "Development"
__version__ = "0.0.0"

app = Flask("fumetti")
CORS(app)


def config():
    app.config["pgpool"] = database.open_db(
        host=os.environ.get("DATABASE_HOST", default="localhost"),
        port=os.environ.get("DATABASE_PORT", default="5432"),
        dbname=os.environ.get("DATABASE_NAME", default=""),
        user=os.environ.get("DATABASE_USER", default=""),
        password=os.environ.get("DATABASE_PASSWORD", default="")
    )


def main():
    config()

    ROUTES = {
        "/": {
            "func": index.index,
            "methods": ["GET"]
        },
        "/albi": {
            "func": albi.Albi().post_albi,
            "methods": ["POST"]
        },
        "/albi/<serie>": {
            "func": albi.Albi().get_albi,
            "methods": ["GET"]
        },
        "/collane": {
            "func": collane.get_collane,
            "methods": ["GET"]
        },
        "/conservazione": {
            "func": lookup.get_conservazione,
            "methods": ["GET"]
        },
        "/genere_serie": {
            "func": lookup.get_genere_serie,
            "methods": ["GET"]
        },
        "/periodicita": {
            "func": lookup.get_periodicita,
            "methods": ["GET"]
        },
        "/rilegatura": {
            "func": lookup.get_rilegatura,
            "methods": ["GET"]
        },
        "/serie": {
            "func": serie.Serie().request_serie,
            "methods": ["GET", "POST"]
        },
        "/status_serie": {
            "func": lookup.get_status_serie,
            "methods": ["GET"]
        },
        "/valuta": {
            "func": lookup.get_valuta,
            "methods": ["GET"]
        }
    }
    for url in ROUTES:
        app.add_url_rule(url, view_func=ROUTES[url]["func"], methods=ROUTES[url]["methods"])

    app.run(debug=os.environ.get("APP_DEBUG", default=False), host=os.environ.get("APP_HOST", default="localhost"),
            port=os.environ.get("APP_PORT", default="8000"))


@app.teardown_appcontext
def teardown_db(f):
    database.close_db()


if __name__ == '__main__':
    main()
