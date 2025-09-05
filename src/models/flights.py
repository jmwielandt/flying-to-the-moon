from collections import defaultdict
from typing import Any

PASSENGER_CATEGORIES = ["Black", "Platinum", "Gold", "Normal"]


def separate_overbooked_passengers(flight: dict[str, Any]) -> list[dict[str, Any]]:
    passengers: list[dict[str, Any]] = flight["passengers"]

    passenger_clusters = defaultdict(list)
    for passenger in passengers:
        passenger_clusters[passenger["reservationId"]].append(passenger)

    for passengers_list in passenger_clusters.values():
        sort_passengers_list(passengers_list)

    passenger_clusters = list(passenger_clusters.values())
    sort_passengers_clusters(passenger_clusters)

    booked_passengers = []
    overbooked_passengers = []

    for cluster in passenger_clusters:
        if len(booked_passengers) + len(cluster) <= flight["capacity"]:
            booked_passengers.extend(cluster)
        else:
            overbooked_passengers.extend(cluster)

    flight["passengers"] = booked_passengers

    return overbooked_passengers


def sort_passengers_list(passengers: list[dict]):
    passengers.sort(key=lambda x: x["age"], reverse=True)
    passengers.sort(key=lambda x: x["hasCheckedBaggage"], reverse=True)
    passengers.sort(key=lambda x: x["hasConnections"], reverse=True)
    passengers.sort(key=lambda x: PASSENGER_CATEGORIES.index(x["flightCategory"]))


def sort_passengers_clusters(clusters: list[list[dict[str, Any]]]):
    clusters.sort(key=lambda x: x[0]["age"], reverse=True)
    clusters.sort(key=lambda x: x[0]["hasCheckedBaggage"], reverse=True)
    clusters.sort(key=lambda x: x[0]["hasConnections"], reverse=True)
    clusters.sort(key=lambda x: PASSENGER_CATEGORIES.index(x[0]["flightCategory"]))
