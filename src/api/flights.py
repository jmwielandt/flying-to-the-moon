import json
import logging
from typing import Any
from uuid import UUID

import jsonschema
from flask import Blueprint, Response, jsonify, request
from rethinkdb import r

from src.api.schemas import FLIGHT_SCHEMA
from src.db.connect import connect_db
from src.models.flights import separate_overbooked_passengers

app = Blueprint("flights", __name__, url_prefix="/flights")


@app.get("/<uuid:flight_uuid>")
def get_flight(flight_uuid: UUID):
    flight_id: str = str(flight_uuid)
    con = connect_db()
    result = r.table("flights").get(flight_id).run(con)
    return jsonify(result)


@app.post("/")
def create_flight():
    flight: dict[str, Any] = request.json  # type: ignore

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

    overbooked_passengers = separate_overbooked_passengers(flight)
    # TEMP:
    logging.debug(
        "OVERBOOKED_PASSENGERS:\n" + json.dumps(overbooked_passengers, indent=2)
    )

    con = connect_db()
    result = r.table("flights").insert(flight).run(con)
    flight_id = result["generated_keys"][0]
    inserted_flight = r.table("flights").get(flight_id).run(con)
    # TODO: improve api output
    return jsonify(inserted_flight)


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
