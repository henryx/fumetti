# -*- coding: utf-8 -*-

# Copyright (C) 2019 Enrico Bianchi (enrico.bianchi@gmail.com)
# Project Name: fumetti
# Description   A RESTful API for managing a collection of comic books
# License       GPL version 2 (see LICENSE for details)
import json

from flask import Blueprint, Response

import utils.database


collane_route = Blueprint('collane_route', __name__)


@collane_route.route("/collane", methods=("GET",))
def get_collane():
    data, err = utils.database.select_collane()
    if not err:
        res = {"data": data, "op": "ok"}
        resp = Response(json.dumps(res), status=200, mimetype="application/json")
    else:
        res = {"op": "ko", "msg": "Error to connect to database"}
        resp = Response(json.dumps(res), status=500, mimetype="application/json")

    return resp
