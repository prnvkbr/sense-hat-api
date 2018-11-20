from sense_hat import SenseHat


class Hat:

    sense = SenseHat()
    sense.clear()

    @staticmethod
    def get_data():

        t = sense.get_temperature()
        h = sense.get_humidity()

        return {"temp": str(t), "humidity": str(h)}
