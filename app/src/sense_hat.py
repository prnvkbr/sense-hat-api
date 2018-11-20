from sense_hat import SenseHat


class Hat:

    sense = SenseHat()
    sense.clear()

    @staticmethod
    def get_data():

        t = Hat.sense.get_temperature()
        h = Hat.sense.get_humidity()

        return {"temp": str(t), "humidity": str(h)}
