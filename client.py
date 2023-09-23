import adafruit_requests as requests
from client_secrets import secrets
import wifi
import socketpool


def connect():
    global wifi
    print("Connecting to %s" % secrets["ssid"])
    wifi.radio.connect(secrets["ssid"], secrets["password"])
    print("Connected to %s!" % secrets["ssid"])


def client_send(sensor_value):
    socket = socketpool.SocketPool(wifi.radio)
    http = requests.Session(socket)
    response = http.get(
        url="http://"
        + secrets["server"]
        + ":"
        + secrets["port"]
        + "/sensor/"
        + secrets["game_uuid"]
        + "/"
        + secrets["sensor_uuid"],
        data=sensor_value,
    )
    print(response.text)


def game_send(game_uuid, player_uuid):
    socket = socketpool.SocketPool(wifi.radio)
    http = requests.Session(socket)
    response = http.get(
        url="http://"
        + secrets["server"]
        + ":"
        + secrets["port"]
        + "/game/"
        + secrets["game_uuid"],
        data=player_uuid,
    )
    print(response.text)


connect()
