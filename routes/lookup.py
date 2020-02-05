# -*- coding: utf-8 -*-

# Copyright (C) 2019 Enrico Bianchi (enrico.bianchi@gmail.com)
# Project Name: fumetti
# Description   A RESTful API for managing a collection of comic books
# License       GPL version 2 (see LICENSE for details)
import json

from flask import Blueprint, Response

import utils

lookup_route = Blueprint('lookup_route', __name__)


@lookup_route.route("/valuta", methods=("GET",))
def get_valuta():
    query = "SELECT id_valuta, simbolo FROM valuta"

    res = utils.database.execute_query_lookup(query)

    if res["op"] == "ok":
        status = 200
    else:
        status = 500
    resp = Response(json.dumps(res), status=status, mimetype="application/json")

    return resp


@lookup_route.route("/rilegatura", methods=("GET",))
def get_rilegatura():
    query = "SELECT id_rilegatura, descrizione FROM rilegatura"

    res = utils.database.execute_query_lookup(query)

    if res["op"] == "ok":
        status = 200
    else:
        status = 500
    resp = Response(json.dumps(res), status=status, mimetype="application/json")

    return resp


@lookup_route.route("/conservazione", methods=("GET",))
def get_conservazione():
    query = "SELECT id_stato_conservazione, descrizione FROM stato_conservazione"

    res = utils.database.execute_query_lookup(query)

    if res["op"] == "ok":
        status = 200
    else:
        status = 500
    resp = Response(json.dumps(res), status=status, mimetype="application/json")

    return resp


@lookup_route.route("/status_serie", methods=("GET",))
def get_status_serie():
    query = "SELECT id_status_serie, descrizione FROM status_serie"

    res = utils.database.execute_query_lookup(query)

    if res["op"] == "ok":
        status = 200
    else:
        status = 500
    resp = Response(json.dumps(res), status=status, mimetype="application/json")

    return resp


@lookup_route.route("/periodicita", methods=("GET",))
def get_periodicita():
    query = "SELECT id_periodicita, descrizione FROM periodicita"

    res = utils.database.execute_query_lookup(query)

    if res["op"] == "ok":
        status = 200
    else:
        status = 500
    resp = Response(json.dumps(res), status=status, mimetype="application/json")

    return resp


@lookup_route.route("/genere_serie", methods=("GET",))
def get_genere_serie():
    query = "SELECT id_genere_serie, descrizione FROM genere_serie"

    res = utils.database.execute_query_lookup(query)

    if res["op"] == "ok":
        status = 200
    else:
        status = 500
    resp = Response(json.dumps(res), status=status, mimetype="application/json")

    return resp
