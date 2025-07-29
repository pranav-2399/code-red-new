import { useState } from 'react';
import '../styles/SearchBox.css';

const API_KEY = import.meta.env.VITE_OPENCAGE_API_KEY;

export default function LocationSearch({ label, onSelect }) {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const handleSearch = async (value) => {
    setQuery(value);
    if (value.length < 3) return;

    try {
      const res = await fetch(
        `https://api.opencagedata.com/geocode/v1/json?q=${encodeURIComponent(value)}&key=${API_KEY}`
      );
      const data = await res.json();

      setResults(data.results);
    } catch (error) {
      console.error("Geocoding error:", error);
    }
  };

  const handleSelect = (place) => {
    const name = place.formatted;
    setQuery(name);
    setResults([]);
    onSelect({
      display_name: name,
      lat: place.geometry.lat,
      lon: place.geometry.lng
    });
  };

  return (
    <div className="autocomplete">
      <label>{label}</label>
      <input
        value={query}
        onChange={(e) => handleSearch(e.target.value)}
        placeholder={`Search ${label}`}
        className='inputBox'
      />
      {results.length > 0 && (
        <ul className="suggestions">
          {results.map((place, index) => (
            <li key={index} onClick={() => handleSelect(place)}>
              {place.formatted}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
