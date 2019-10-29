# -*- coding: utf-8 -*-

# Copyright (C) 2019 Enrico Bianchi (enrico.bianchi@gmail.com)
# Project Name: fumetti
# Description   A RESTful API for managing a collection of comic books
# License       GPL version 2 (see LICENSE for details)
import json

from flask import Response, request


def albi():
    if request.method == "GET":
        get_albi()
    elif request.method == "POST":
        post_albi()


def get_albi():
    res = {"msg": "GET albi requested", "op": "ok"}
    resp = Response(json.dumps(res), status=200, mimetype="application/json")
    return resp


def post_albi():
    res = {"msg": "POST albi requested", "op": "ok"}
    resp = Response(json.dumps(res), status=200, mimetype="application/json")
    return resp
