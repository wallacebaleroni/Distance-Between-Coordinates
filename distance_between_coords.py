import math

cities = [
		  {'name': 'Madrid', 	'latitude': 40.416692, 'longitude': -3.703720},
		  {'name': 'Barcelona', 'latitude': 41.385063, 'longitude': 2.173404},
		  {'name': 'Milano',	'latitude': 45.464203, 'longitude': 9.189982},
		 ]

def create_matrix():
	num_of_cities = len(cities)
	distances = [[0 for col in range(num_of_cities)] for row in range(num_of_cities)]

	labels = []

	for i in range(num_of_cities):
		labels.append(cities[i]['name'])
		for j in range(num_of_cities):
			if i < j:
				distances[i][j] = int(distance_in_km_between_earth_coordinates(cities[i]['latitude'], cities[i]['longitude'],
																		       cities[j]['latitude'], cities[j]['longitude']))

	export(labels, distances)

def distance_in_km_between_earth_coordinates(lat1, lon1, lat2, lon2):
  earthRadiusKm = 6371;

  d_lat = degreesToRadians(lat2-lat1);
  d_lon = degreesToRadians(lon2-lon1);

  lat1 = degreesToRadians(lat1);
  lat2 = degreesToRadians(lat2);

  a = math.sin(d_lat/2) * math.sin(d_lat/2) + math.sin(d_lon/2) * math.sin(d_lon/2) * math.cos(lat1) * math.cos(lat2); 
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a)); 
  return earthRadiusKm * c;

def degreesToRadians(degrees):
  return degrees * math.pi / 180;


def export(labels, distances):
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

create_matrix()