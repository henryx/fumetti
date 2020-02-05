# -*- coding: utf-8 -*-

# Copyright (C) 2019 Enrico Bianchi (enrico.bianchi@gmail.com)
# Project Name: fumetti
# Description   A RESTful API for managing a collection of comic books
# License       GPL version 2 (see LICENSE for details)
import json

from flask import Blueprint, Response, request

import utils.database

serie_route = Blueprint('serie_route', __name__)


@serie_route.route("/serie", methods=("GET",))
def get_serie():
    data, err = utils.database.select_serie()
    if not err:
        res = {"data": data, "op": "ok"}
        resp = Response(json.dumps(res), status=200, mimetype="application/json")
    else:
        res = {"op": "ko", "msg": "Error to connect to database"}
        resp = Response(json.dumps(res), status=500, mimetype="application/json")

    return resp


@serie_route.route("/serie", methods=("POST",))
def post_serie():
    content = request.get_json("data")
    # TODO: check if serie exists (act a lowercase for name?)

    if utils.database.insert_serie(content):
        res = {"data": content, "op": "ok"}
        resp = Response(json.dumps(res), status=200, mimetype="application/json")
    else:
        res = {"op": "ko", "msg": "Error to connect to database"}
        resp = Response(json.dumps(res), status=500, mimetype="application/json")

    return resp
