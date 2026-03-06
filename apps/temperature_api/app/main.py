import time
import logging
import os
import random

from fastapi import FastAPI, Query, Path

SensorID = str
Location = str

CLIENT_LOCATION_BY_SENSOR: dict[SensorID, Location] = dict(
    (id, os.getenv("SENSOR_LOCATION_%s" % id, "Unknown")) for id in os.getenv("SENSOR_IDS", "0").split(","))

CLIENT_SENSOR_BY_LOCATION: dict[Location, SensorID] = dict((v, k) for k, v in CLIENT_LOCATION_BY_SENSOR.items())

app = FastAPI(
    title="Temperature API",
    description="Приложение для снятия показателй температуры с сенсоров клиента",
    version="1.0.0")

def generate_temperature(location: Location, sensor_id: SensorID):
    return dict(
        value=random.gauss(23.0, 10.0),
        unit="C",
        timestamp=time.strftime('%Y-%m-%dT%H:%M:%SZ'),
        location=location,
        status="active",
        sensor_id=sensor_id,
        sensor_type="temperature",
        description="Temperature sensor at %s" % location
    )


@app.get("/temperature",
         description="Возвращает текущее значение температуры в заданом пространстве")
def get_temperature_by_location(
        location: Location = Query(
            description="Расположение сенсора температуры у клиента"
        )):
    logging.info("get temperature by location: location=%s", location)
    return generate_temperature(location, CLIENT_SENSOR_BY_LOCATION.get(location, 0))


@app.get("/temperature/{sensor_id}",
         description="Возвращает текущее значение температуры сенсора")
def get_temperature_by_sensor(
        sensor_id: SensorID = Path(
            description="Идентификатор сенсора температуры"
        )):
    logging.info("get temperature by sensor: id=%i", sensor_id)
    return generate_temperature(CLIENT_LOCATION_BY_SENSOR.get(sensor_id, "Unknown"), sensor_id)


@app.get("/health",
         description="Возвращает информацию о состоянии системы")
def health_check():
    return {"status": "healthy"}
