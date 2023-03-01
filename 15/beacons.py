from absl import app
import re

class Sensor:
    def __init__(self, sensor, beacon) -> None:
        self.sensor = sensor
        self.beacon = beacon

    def __repr__(self) -> str:
        return f'Sensor: {self.sensor} Beacon: {self.beacon}'
    
    def range(self):
        return abs(self.sensor[0] - self.beacon[0]) + abs(self.sensor[1] - self.beacon[1])
    
    # def boundary(self):


class Line:
    def __init__(self, number):
        self.number = number
        self.no_beacon = set()
    
    def process_sensor(self, sensor):
        distance_to_line = abs(sensor.sensor[1] - self.number)
        # print(f'distance_to_line {distance_to_line}')
        distance_along_line = sensor.range() - distance_to_line
        # print(f'distance_along_line {distance_along_line}')
        line_intersect = sensor.sensor[0]
        # print(f'line_intersect {line_intersect}')
        self.no_beacon |= set(range(line_intersect - distance_along_line, line_intersect + distance_along_line + 1, 1))
    
    def mark_beacon(self, sensor):
        if sensor.beacon[1] == self.number:
            self.no_beacon.discard(sensor.beacon[0])
        if sensor.sensor[1] == self.number:
            self.no_beacon.discard(sensor.sensor[0])
    
    def count_in_range(self, min, max):
        count = 0
        for i in self.no_beacon:
            if i >= min and i <= max:
                count += 1
        return count

    def __repr__(self) -> str:
        return f'Line {self.number}: {self.no_beacon}'


def main(argv):
    filename = argv[1]
    f = open(filename)

    sensors = []

    while input_line := f.readline():
        nums = list(map(int, re.findall(r'-?\d+', input_line)))
        sensors.append(Sensor((nums[0], nums[1]), (nums[2], nums[3])))

    min = 0
    max = 4000000
    for line_number in range(min, max + 1):
        line = Line(line_number)
        print('a')
        for sensor in sensors:
            line.process_sensor(sensor)
        
        print(f'line: {line_number} == {line.count_in_range(min, max)}')
        # for sensor in sensors:
        #     line.mark_beacon(sensor)
        if (line.count_in_range(min, max) < max - min + 1):
            print(f'line: {line_number} in rnage: {line.count_in_range(min, max)} {line}')
            for i in range(min, max + 1):
                if not (i in line.no_beacon):
                    print(f'{i}, {line_number}')
                    exit()

    # sensor = sensors[6]
    # print(sensor)
    # print(sensor.range())
    # line = Line(10)
    # line.process_sensor(sensors[6])
    # print(line)
    # print(line)
    


if __name__ == '__main__':
    app.run(main)