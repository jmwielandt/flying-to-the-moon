FLIGHT_SCHEMA = {
    "type": "object",
    "properties": {
        "flightCode": {"type": "string"},
        "passengers": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "number"},
                    "name": {"type": "string"},
                    "hasConnections": {"type": "boolean"},
                    "age": {"type": "number"},
                    "flightCategory": {
                        "type": "string",
                        "enum": ["Black", "Platinum", "Gold", "Normal"],
                    },
                    "reservationId": {"type": "string"},
                    "hasCheckedBaggage": {"type": "boolean"},
                },
            },
        },
    },
}
