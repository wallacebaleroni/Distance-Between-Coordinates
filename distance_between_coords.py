import math

cities = [
    {'name': 'Milano', 'latitude': 45.464203, 'longitude': 9.189982},
    {'name': 'Madrid', 'latitude': 40.416692, 'longitude': -3.703720},
    {'name': 'Barcelona', 'latitude': 41.385063, 'longitude': 2.173404},
]
distances = [[0 for col in range(len(cities))] for row in range(len(cities))]


def create_matrix():
    labels = []

    for i in range(len(cities)):
        labels.append(cities[i]['name'])
        for j in range(len(cities)):
            if i != j:
                distances[i][j] = int(
                    distance_in_km_between_earth_coordinates(cities[i]['latitude'], cities[i]['longitude'],
                                                             cities[j]['latitude'], cities[j]['longitude']))

    return get_best_path(labels)


def distance_in_km_between_earth_coordinates(lat1, lon1, lat2, lon2):
    earth_radius_km = 6371

    d_lat = degrees_to_radians(lat2 - lat1)
    d_lon = degrees_to_radians(lon2 - lon1)

    lat1 = degrees_to_radians(lat1)
    lat2 = degrees_to_radians(lat2)

    a = math.sin(d_lat / 2) * math.sin(d_lat / 2) + math.sin(d_lon / 2) * math.sin(d_lon / 2) * math.cos(
        lat1) * math.cos(lat2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return earth_radius_km * c


def degrees_to_radians(degrees):
    return degrees * math.pi / 180


def export(labels):
    file_name = 'distances.csv'
    fp = open(file_name, 'w+')

    fp.write('Cities Names;')
    for i in range(len(labels)):
        if i < len(labels) - 1:
            fp.write(labels[i] + ';')
        else:
            fp.write(labels[i] + '\n')

    for i in range(len(distances)):
        fp.write(labels[i] + ';')
        for j in range(len(distances)):
            if j < len(distances) - 1:
                fp.write(str(distances[i][j]) + ';')
            else:
                fp.write(str(distances[i][j]) + '\n')

    fp.close()


def get_best_path(labels):
    candidates = list(range(len(labels)))

    shortest_path = None
    shortest_distance = 10000000

    for candidate in candidates:
        new_candidates = candidates.copy()
        new_candidates.remove(candidate)
        path, distance = get_best_path_recursive(candidate, new_candidates)

        if distance < shortest_distance:
            shortest_path = [candidate] + path
            shortest_distance = distance

    return shortest_path, shortest_distance


def get_best_path_recursive(current, candidates):
    if len(candidates) == 1:
        return candidates, distances[current][candidates[0]]

    shortest_path = None
    shortest_distance = 10000000

    for candidate in candidates:
        new_candidates = candidates.copy()
        new_candidates.remove(candidate)
        path, distance = get_best_path_recursive(candidate, new_candidates)

        if distances[current][candidate] + distance < shortest_distance:
            shortest_path = [candidate] + path
            shortest_distance = distances[current][candidate] + distance

    return shortest_path, shortest_distance


print(create_matrix())
