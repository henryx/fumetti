# -*- coding: utf-8 -*-

# Copyright (C) 2019 Enrico Bianchi (enrico.bianchi@gmail.com)
# Project Name: fumetti
# Description   A RESTful API for managing a collection of comic books
# License       GPL version 2 (see LICENSE for details)
from routes import index, serie, lookup

__all__ = ["index", "serie", "lookup"]

ROUTES = {
    "/": {
        "func": index.index,
        "methods": ["GET"]
    },
    "/serie": {
        "func": serie.get_serie,
        "methods": ["GET"]
    },
    "/valuta": {
        "func": lookup.get_valuta,
        "methods": ["GET"]
    },
    "/rilegatura": {
        "func": lookup.get_rilegatura,
        "methods": ["GET"]
    }
}
