# -*- coding: utf-8 -*-

# Copyright (C) 2019 Enrico Bianchi (enrico.bianchi@gmail.com)
# Project Name: fumetti
# Description   A RESTful API for managing a collection of comic books
# License       GPL version 2 (see LICENSE for details)
import json

from flask import Response

import utils


def get_valuta():
    query = "SELECT id_valuta, simbolo FROM valuta"
    db = utils.database.get_db()

    res = utils.database.execute_query_lookup(db, query)

    if res["op"] == "ok":
        status = 200
    else:
        status = 500
    resp = Response(json.dumps(res), status=status, mimetype="application/json")

    return resp


def get_rilegatura():
    query = "SELECT id_rilegatura, descrizione FROM rilegatura"
    db = utils.database.get_db()

    res = utils.database.execute_query_lookup(db, query)

    if res["op"] == "ok":
        status = 200
    else:
        status = 500
    resp = Response(json.dumps(res), status=status, mimetype="application/json")

    return resp


def get_conservazione():
    query = "SELECT id_stato_conservazione, descrizione FROM stato_conservazione"
    db = utils.database.get_db()

    res = utils.database.execute_query_lookup(db, query)

    if res["op"] == "ok":
        status = 200
    else:
        status = 500
    resp = Response(json.dumps(res), status=status, mimetype="application/json")

    return resp


def get_status_serie():
    query = "SELECT id_status_serie, descrizione FROM status_serie"
    db = utils.database.get_db()

    res = utils.database.execute_query_lookup(db, query)

    if res["op"] == "ok":
        status = 200
    else:
        status = 500
    resp = Response(json.dumps(res), status=status, mimetype="application/json")

    return resp


def get_periodicita():
    query = "SELECT id_periodicita, descrizione FROM periodicita"
    db = utils.database.get_db()

    res = utils.database.execute_query_lookup(db, query)

    if res["op"] == "ok":
        status = 200
    else:
        status = 500
    resp = Response(json.dumps(res), status=status, mimetype="application/json")

    return resp


def get_genere_serie():
    query = "SELECT id_genere_serie, descrizione FROM genere_serie"
    db = utils.database.get_db()

    res = utils.database.execute_query_lookup(db, query)

    if res["op"] == "ok":
        status = 200
    else:
        status = 500
    resp = Response(json.dumps(res), status=status, mimetype="application/json")

    return resp
