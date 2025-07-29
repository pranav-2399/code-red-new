from services.ors import get_route

source = (77.5946, 12.9716)         # Bangalore (lon, lat)
destination = (77.7091, 12.9141)    # Whitefield (lon, lat)

result = get_route(source, destination)
print(result)
