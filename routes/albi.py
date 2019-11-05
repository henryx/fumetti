# -*- coding: utf-8 -*-

# Copyright (C) 2019 Enrico Bianchi (enrico.bianchi@gmail.com)
# Project Name: fumetti
# Description   A RESTful API for managing a collection of comic books
# License       GPL version 2 (see LICENSE for details)
import json

from flask import Response, request


def albi():
    if request.method == "GET":
        resp = get_albi()
    elif request.method == "POST":
        resp = post_albi()
    else:
        res = {"msg": "Request not allowed", "op": "ko"}
        resp = Response(json.dumps(res), status=405, mimetype="application/json")

    return resp


def get_albi():
    res = {"msg": "GET albi requested", "op": "ok"}
    resp = Response(json.dumps(res), status=200, mimetype="application/json")
    return resp


def post_albi():
    content = request.get_json("data")

    # TODO: save data into database and return response

    res = {"msg": "POST albi requested", "op": "ok"}
    resp = Response(json.dumps(res), status=200, mimetype="application/json")
    return resp
