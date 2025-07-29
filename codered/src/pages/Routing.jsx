import { useEffect } from 'react';
import { useMap } from 'react-leaflet';
import L from 'leaflet';
import 'leaflet-routing-machine';

export default function Routing({ source, destination }) {
  const map = useMap();

  useEffect(() => {
    if (!map || !source || !destination) return;

    const url = `https://router.project-osrm.org/route/v1/driving/${source.lon},${source.lat};${destination.lon},${destination.lat}?alternatives=true&overview=full&geometries=geojson`;

    fetch(url)
      .then(res => res.json())
      .then(data => {
        if (!data.routes || data.routes.length === 0) return;

        // Remove existing layers if needed
        const layers = [];

        data.routes.slice(0, 3).forEach((route, index) => {
          const coords = route.geometry.coordinates.map(([lon, lat]) => [lat, lon]);

          const color = ['#6FA1EC', '#FF8C00', '#32CD32'][index]; // blue, orange, green

          const polyline = L.polyline(coords, {
            color,
            weight: 5,
            opacity: 0.8,
            dashArray: index === 0 ? null : '8',
          }).addTo(map);

          layers.push(polyline);
        });

        const bounds = L.latLngBounds(layers.flatMap(layer => layer.getLatLngs()));
        map.fitBounds(bounds, { padding: [50, 50] });

        return () => {
          layers.forEach(layer => map.removeLayer(layer));
        };
      })
      .catch(err => {
        console.error('Routing error:', err);
      });

  }, [map, source, destination]);

  return null;
}
