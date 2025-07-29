// components/Home.jsx
import { useState } from 'react';
import '../styles/Home.css';
import Map from './Map';
import LocationSearch from './LocationSearch';

export default function Home() {
  const [source, setSource] = useState(null);
  const [destination, setDestination] = useState(null);
  const [submitted, setSubmitted] = useState(false);
  const [paragraph, setParagraph] = useState("");

    const handleShowOnMap = async () => {
    if (!source || !destination) {
        alert("Please select both locations.");
        return;
    }

    setSubmitted(true);

    const data = {
        source,
        destination,
        timestamp: new Date().toISOString()
    };

    try {
        const response = await fetch("http://localhost:8000/transit/locations", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
        });

        const result = await response.json();

        if (!response.ok) throw new Error(result.message);

        console.log("✅ Data sent and received AI response!");
        setParagraph(result.message); // ✅ show in UI
    } catch (err) {
        console.error("❌ Error:", err);
        alert("AI failed: " + err.message);
    }
    };

  return (
    
    <div className="home-container">
      <h1>PHEIDIPPIDES</h1>
      <div className="two-columns">
        <Map
          source={submitted ? source : null}
          destination={submitted ? destination : null}
        />
        <div className="home-features">
          <h2 className="home-features-heading">Inputs</h2>
          <div className="features-inputs">
            <LocationSearch label="Source" onSelect={setSource} />
            <LocationSearch label="Destination" onSelect={setDestination} />
            <button onClick={handleShowOnMap}>Show on Map</button>
          </div>
        </div>
      </div>
      {paragraph && (
        <div className="ai-paragraph">
            <h2>Recommended Transit Routes:</h2>
            <p>{paragraph}</p>
        </div>
        )}
    </div>
  );
}
