import json
import logging
from uuid import UUID

import jsonschema
from flask import Blueprint, Response, jsonify, request
from rethinkdb import r

from src.api.schemas import FLIGHT_SCHEMA
from src.db.connect import connect_db

app = Blueprint("flights", __name__, url_prefix="/flights")


@app.get("/<uuid:flight_uuid>")
def get_flight(flight_uuid: UUID):
    flight_id: str = str(flight_uuid)
    con = connect_db()
    result = r.table("flights").get(flight_id).run(con)
    print(result)
    return jsonify(result)


@app.post("/")
def create_flight():
    flight = request.json

    # validate incoming json schema and handle the malformed case
    try:
        jsonschema.validate(instance=flight, schema=FLIGHT_SCHEMA)
    except jsonschema.ValidationError as e:
        logging.error(f"couldn't accept flight object: {e.message}")
        response = {
            "status": "error",
            "error": f"couldn't accept flight object: {e.message}",
        }
        return Response(
            status=400,
            response=json.dumps(response),
            content_type="application/json",
        )

    con = connect_db()
    result = r.table("flights").insert(flight).run(con)
    # TODO: improve api output
    return jsonify(result)


@app.put("/<uuid:flight_uuid>")
def update_flight(flight_uuid: UUID):
    flight_id: str = str(flight_uuid)
    flight = request.json

    # validate incoming json schema and handle the malformed case
    try:
        jsonschema.validate(instance=flight, schema=FLIGHT_SCHEMA)
    except jsonschema.ValidationError as e:
        logging.error(f"couldn't accept flight object: {e.message}")
        response = {
            "status": "error",
            "error": f"couldn't accept flight object: {e.message}",
        }
        return Response(
            status=400,
            response=json.dumps(response),
            content_type="application/json",
        )

    con = connect_db()
    result = r.table("flights").get(flight_id).update(flight).run(con)
    # TODO: improve api output
    return jsonify(result)


@app.delete("/<uuid:flight_uuid>")
def delete_flight(flight_uuid: UUID):
    flight_id: str = str(flight_uuid)
    con = connect_db()
    # soft delete
    result = r.table("flights").get(flight_id).delete(durability="soft").run(con)
    # TODO: improve api output
    return jsonify(result)
