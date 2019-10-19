# -*- coding: utf-8 -*-

# Copyright (C) 2019 Enrico Bianchi (enrico.bianchi@gmail.com)
# Project Name: fumetti
# Description   A RESTful API for managing a collection of comic books
# License       GPL version 2 (see LICENSE for details)
import json

from flask import Response

import utils.database


def get_serie():
    db = utils.database.get_db()

    res = {"msg": "Requested serie", "op": "ok"}
    resp = Response(json.dumps(res), status=200, mimetype="application/json")
    return resp
