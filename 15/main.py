import os
from math import copysign, inf
from ast import literal_eval
from matplotlib import pyplot as plt
from tqdm import tqdm

FILENAME = "input.txt"


class SensorCover():
    min_x = None
    max_x = None
    min_y = None
    max_y = None

    def __init__(self, distance, sensor_pos) -> None:
        self.distance = distance
        self.sensor_pos = sensor_pos
        if __class__.min_x is None or self.sensor_pos[0]-self.distance < __class__.min_x:
            __class__.min_x = self.sensor_pos[0]-self.distance
        if __class__.max_x is None or self.sensor_pos[0]+self.distance > __class__.max_x:
            __class__.max_x = self.sensor_pos[0]+self.distance
        if __class__.min_y is None or self.sensor_pos[1]-self.distance < __class__.min_y:
            __class__.min_y = self.sensor_pos[1]-self.distance
        if __class__.max_y is None or self.sensor_pos[1]+self.distance > __class__.max_y:
            __class__.max_y = self.sensor_pos[1]+self.distance

    def in_sensor_range(self, cell):
        dif_x = abs(cell[0]-self.sensor_pos[0])
        dif_y = abs(cell[1]-self.sensor_pos[1])
        if dif_x + dif_y > self.distance:
            return False
        return True


def parse_data_gen() -> list:
    filedir = os.path.split(__file__)[0]
    with open(os.path.join(filedir, FILENAME)) as f:
        lines = f.read().split("\n")
    for line in lines:
        line = line.split()
        sensor = (int(line[2][2:-1]), int(line[3][2:-1]))
        beacon = (int(line[8][2:-1]), int(line[9][2:]))
        yield (sensor, beacon)


# def get_covered_cells(sensor, distance):
#     cells = set()
#     for x in range(distance+1):
#         y_distance = distance-x
#         for y in range(-y_distance, y_distance+1):
#             cells.add((sensor[0]+x, sensor[1]+y))
#             cells.add((sensor[0]-x, sensor[1]+y))
#     return cells


# def find_covered_zone():
#     covered_zone = set()
#     data_gen = parse_data_gen()
#     while sensor_beacon_pair := next(data_gen, False):
#         sensor, beacon = sensor_beacon_pair
#         sensor_distance = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])
#         covered_zone = covered_zone.union(get_covered_cells(sensor, sensor_distance))
#     return covered_zone


def get_detect_on_row(row, zone_coverage: set):
    cells_covered = set()
    for x in tqdm(range(SensorCover.min_x, SensorCover.max_x)):
        for sensor in zone_coverage:
            if sensor.in_sensor_range((x, row)):
                cells_covered.add((x, row))
                break
    return cells_covered

def get_not_detect_on_row(row, zone_coverage: set):
    cells_covered = set()
    bottom_range = max(SensorCover.min_x, 0)
    top_range =  min(SensorCover.max_x, 4000000)
    for x in tqdm(range(bottom_range+1, top_range-1)):
        for sensor in zone_coverage:
            if not sensor.in_sensor_range((x, row)) and sensor.in_sensor_range((x-1, row)) and sensor.in_sensor_range((x+1, row)):
                cells_covered.add((x, row))
                break
    return cells_covered



def get_sensor_coverage(sensor_beacon_pairs):
    sensorcoverage = set()
    for pair in sensor_beacon_pairs:
        x_distance = abs(pair[0][0] - pair[1][0])
        y_distance = abs(pair[0][1] - pair[1][1])
        distance = x_distance + y_distance
        sensorcoverage.add(SensorCover(distance, pair[0]))
    return sensorcoverage


if __name__ == "__main__":
    sensor_beacon_pairs = set([x for x in parse_data_gen()])
    sensorcoverage = get_sensor_coverage(sensor_beacon_pairs)
    # covered_zone = find_covered_zone()
    # for sensor_beacon_pair in a:
    #     covered_zone.discard(sensor_beacon_pair[0])
    #     covered_zone.discard(sensor_beacon_pair[1])
    # plt.figure()
    # plt.scatter([x[0] for x in covered_zone], [y[1] for y in covered_zone], c="b")
    # plt.scatter([x[0][0] for x in a], [y[0][1] for y in a], c="r")  # beacon
    # plt.scatter([x[1][0] for x in a], [y[1][1] for y in a], c="g")  # sensor
    # plt.show()
    bottom_range = max(SensorCover.min_x, 0)
    top_range =  min(SensorCover.max_x, 4000000)
    detected_cells = set()
    for y in tqdm(range(bottom_range, top_range)):
        detected_cells = detected_cells.union(get_not_detect_on_row(y, sensorcoverage))
        if detected_cells:
            break
    for sensor_beacon_pair in sensor_beacon_pairs:
        detected_cells.discard(sensor_beacon_pair[0])
        detected_cells.discard(sensor_beacon_pair[1])
    print(detected_cells)
    print(detected_cells[0][0]*4000000+detected_cells[0][1])
