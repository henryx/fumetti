#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2019 Enrico Bianchi (enrico.bianchi@gmail.com)
# Project Name: fumetti
# Description   A RESTful API for managing a collection of comic books
# License       GPL version 2 (see LICENSE for details)
import os

from flask import Flask
from flask_cors import CORS

from routes.albi import albi_route
from routes.collane import collane_route
from routes.editore import editore_route
from routes.index import index_route
from routes.lookup import lookup_route
from routes.serie import serie_route
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
        host=os.environ.get("FUMETTI_DB_HOST", default="localhost"),
        port=os.environ.get("FUMETTI_DB_PORT", default="5432"),
        dbname=os.environ.get("FUMETTI_DB_NAME", default=""),
        user=os.environ.get("FUMETTI_DB_USER", default=""),
        password=os.environ.get("FUMETTI_DB_PASSWORD", default="")
    )


def main():
    config()

    app.register_blueprint(index_route)
    app.register_blueprint(albi_route)
    app.register_blueprint(serie_route)
    app.register_blueprint(collane_route)
    app.register_blueprint(editore_route)
    app.register_blueprint(lookup_route)

    app.run(debug=os.environ.get("FUMETTI_DEBUG", default=False), host=os.environ.get("FUMETTI_HOST", default="localhost"),
            port=os.environ.get("FUMETTI_PORT", default="8000"))


if __name__ == '__main__':
    main()
