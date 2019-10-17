#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2019 Enrico Bianchi (enrico.bianchi@gmail.com)
# Project Name: fumetti
# Description   A RESTful API for managing a collection of comic books
# License       GPL version 2 (see LICENSE for details)


__author__ = "Enrico Bianchi"
__copyright__ = "Copyright 2019, Enrico Bianchi"
__credits__ = ["Enrico Bianchi", ]
__license__ = "GPLv2"
__maintainer__ = "Enrico Bianchi"
__email__ = "enrico.bianchi@gmail.com"
__status__ = "Development"
__version__ = "0.0.0"

import json

from flask import Flask, Response
from flask_cors import CORS

app = Flask("fumetti")
CORS(app)


@app.route("/")
def home():
    res = {"msg": "Fumetti REST API", "op": "ok"}
    resp = Response(json.dumps(res), status=200, mimetype="application/json")
    return resp


if __name__ == '__main__':
    app.run(debug=True)
