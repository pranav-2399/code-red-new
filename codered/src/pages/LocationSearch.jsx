// components/LocationSearch.jsx
import { useState } from 'react';
import '../styles/SearchBox.css';

export default function LocationSearch({ label, onSelect }) {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const handleSearch = async (value) => {
    setQuery(value);
    if (value.length < 3) return;

    const res = await fetch(
      `https://nominatim.openstreetmap.org/search?q=${value}&format=json`
    );
    const data = await res.json();
    setResults(data);
  };

  const handleSelect = (place) => {
    setQuery(place.display_name);
    setResults([]);
    onSelect(place); // send selected place to parent
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
              {place.display_name}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
