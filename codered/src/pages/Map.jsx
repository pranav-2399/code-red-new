// components/Map.jsx
import { MapContainer, TileLayer, Marker, Popup, useMap } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import 'leaflet-routing-machine/dist/leaflet-routing-machine.css';
import Routing from './Routing'; // or the correct relative path
import L from 'leaflet';
import { useEffect } from 'react';
const markerIcon = new L.Icon({
  iconUrl: 'https://unpkg.com/leaflet@1.7.1/dist/images/marker-icon.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
});

function FlyToLocations({ source, destination }) {
  const map = useMap();

  useEffect(() => {
    if (source && destination) {
      const bounds = L.latLngBounds([
        [source.lat, source.lon],
        [destination.lat, destination.lon],
      ]);
      map.fitBounds(bounds, { padding: [50, 50] });
    } else if (source) {
      map.setView([source.lat, source.lon], 13);
    } else if (destination) {
      map.setView([destination.lat, destination.lon], 13);
    }
  }, [source, destination, map]);

  return null;
}

export default function Map({ source, destination }) {
  return (
    <div className="map-holder">
      <MapContainer
        center={[20.5937, 78.9629]}
        zoom={5}
        scrollWheelZoom={true}
        className="custom-map"
        style={{ height: '100%', minHeight: '400px', borderRadius: '2%' }}
      >
        <TileLayer
          url="https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png"
        />

        {source && (
          <Marker position={[source.lat, source.lon]} icon={markerIcon}>
            <Popup>Source: {source.display_name}</Popup>
          </Marker>
        )}
        {destination && (
          <Marker position={[destination.lat, destination.lon]} icon={markerIcon}>
            <Popup>Destination: {destination.display_name}</Popup>
          </Marker>
        )}

        <FlyToLocations source={source} destination={destination} />
        {source && destination && (
          <Routing source={source} destination={destination} />
        )}
      </MapContainer>
    </div>
  );
}
