# -*- coding: utf-8 -*-

# Copyright (C) 2019 Enrico Bianchi (enrico.bianchi@gmail.com)
# Project Name: fumetti
# Description   A RESTful API for managing a collection of comic books
# License       GPL version 2 (see LICENSE for details)
from contextlib import contextmanager

import psycopg2.pool
from flask import current_app


def open_db(host, port, dbname, user, password):
    pool = psycopg2.pool.ThreadedConnectionPool(1, 20,
                                                host=host, port=port,
                                                dbname=dbname, user=user,
                                                password=password)

    return pool


@contextmanager
def get_db_conn():
    try:
        conn = current_app.config["pgpool"].getconn()
        yield conn
    finally:
        current_app.config["pgpool"].putconn(conn)


@contextmanager
def get_db_cur(commit=False):
    with get_db_conn() as conn:
        cur = conn.cursor()
        try:
            yield cur
            if commit:
                conn.commit()
        finally:
            cur.close()


def execute_query_lookup(query):
    data = []

    with get_db_cur() as cur:
        try:
            cur.execute(query)
            results = cur.fetchall()
            for item in results:
                data.append({"id": item[0], "name": item[1]})

            res = {"data": data, "op": "ok"}
        except psycopg2.OperationalError:
            res = {"op": "ko", "msg": "Error to connect to database"}

    return res


def insert_albo(data):
    query = "INSERT INTO albi(id_serie, numero_albo, data_pubblicazione, prezzo_copertina, id_valuta, id_rilegatura, id_stato_conservazione, note) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"

    with get_db_cur(True) as cur:
        try:
            cur.execute(query, (data["serie"], data["numero"], data["date"], data["prezzo"], data["valuta"],
                                data["rilegatura"], data["conservazione"], data["note"]))
        except psycopg2.Error as e:
            return False
        return True


def select_serie():
    query = "SELECT id_serie, nome FROM serie ORDER BY nome"

    data = []
    with get_db_cur() as cur:
        try:
            cur.execute(query)
            results = cur.fetchall()
            for item in results:
                data.append({"id": item[0], "name": item[1]})
        except psycopg2.Error as e:
            return [], True

    return data, False


def insert_serie(data):
    query = "INSERT INTO serie(nome, id_collana, id_status_serie, id_periodicita, id_genere_serie, note) VALUES(%s, %s, %s, %s, %s)"

    with get_db_cur(True) as cur:
        try:
            cur.execute(query, (data["name"], data["collana"], data["status_serie"], data["periodicita"],
                                data["genere"], data["note"]))
        except psycopg2.Error as e:
            return False
        return True


def select_collane():
    query = "SELECT id_collana, nome FROM collane ORDER BY nome"

    data = []
    with get_db_cur() as cur:
        try:
            cur.execute(query)
            results = cur.fetchall()
            for item in results:
                data.append({"id": item[0], "name": item[1]})
        except psycopg2.Error as e:
            return [], True

    return data, False


def select_editore():
    query = "SELECT id_casa_editrice, nome FROM case_editrici ORDER BY nome"

    data = []
    with get_db_cur() as cur:
        try:
            cur.execute(query)
            results = cur.fetchall()
            for item in results:
                data.append({"id": item[0], "name": item[1]})
        except psycopg2.Error as e:
            return [], True

    return data, False
