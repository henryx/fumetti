# -*- coding: utf-8 -*-

# Copyright (C) 2019 Enrico Bianchi (enrico.bianchi@gmail.com)
# Project Name: fumetti
# Description   A RESTful API for managing a collection of comic books
# License       GPL version 2 (see LICENSE for details)
import json

from flask import Blueprint, Response

import utils

editore_route = Blueprint('editore_route', __name__)


@editore_route.route("/editore", methods=("GET",))
def get_collane():
    data, err = utils.database.select_editore()
    if not err:
        res = {"data": data, "op": "ok"}
        msg = json.dumps(res)
        resp = Response(msg, status=200, mimetype="application/json")
    else:
        res = {"op": "ko", "msg": "Error to connect to database"}
        resp = Response(json.dumps(res), status=500, mimetype="application/json")

    return resp
