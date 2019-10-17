#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2019 Enrico Bianchi (enrico.bianchi@gmail.com)
# Project Name: fumetti
# Description   A RESTful API for managing a collection of comic books
# License       GPL version 2 (see LICENSE for details)
import routes

__author__ = "Enrico Bianchi"
__copyright__ = "Copyright 2019, Enrico Bianchi"
__credits__ = ["Enrico Bianchi", ]
__license__ = "GPLv2"
__maintainer__ = "Enrico Bianchi"
__email__ = "enrico.bianchi@gmail.com"
__status__ = "Development"
__version__ = "0.0.0"

from flask import Flask
from flask_cors import CORS

app = Flask("fumetti")
CORS(app)


def main():
    for url in routes.ROUTES:
        app.add_url_rule(url, view_func=routes.ROUTES[url])

    app.run(debug=True)


if __name__ == '__main__':
    main()
