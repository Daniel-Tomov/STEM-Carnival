import client


# provide the name of the sensor and the data from the sensor
# sensor_name is not stored in the secrets because there may
# be more than one sensor tied to one client
client.client_send("height", "100")