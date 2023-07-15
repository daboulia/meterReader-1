

class Meter:
    def __init__(self, type, serial, cons_factor = 1, curr_reading = 0, prev_reading = 0):
        self.type = type
        self.serial = serial
        self.cons_factor = cons_factor
        self.curr_reading = curr_reading
        self.prev_reading = prev_reading

    def set_curr_reading(self, new_curr_reading):
        self.prev_reading = self.curr_reading
        self.curr_reading = new_curr_reading

    def get_consumption(self):
        cons = (self.curr_reading - self.prev_reading) * self.cons_factor
        return cons

    def get_meter_info(self):
        return self.type, self.serial


meter_1 = Meter('gas', 1001)

print(meter_1.get_meter_info())
meter_1.set_curr_reading(1000)
print(meter_1.get_consumption())
meter_1.set_curr_reading(2200)
print(meter_1.get_consumption())




















