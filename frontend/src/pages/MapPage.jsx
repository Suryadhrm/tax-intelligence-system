import { useEffect, useState } from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import { venueApi } from "../services/api";
import Navbar from "../components/Navbar";
import "leaflet/dist/leaflet.css";

// Section 12.3 Map Page: venue markers colored by risk category (Module 8).
const JAKARTA_BARAT_CENTER = [-6.1683, 106.7588];

export default function MapPage() {
  const [venues, setVenues] = useState([]);

  useEffect(() => {
    venueApi.list().then(({ data }) => setVenues(data)).catch(() => setVenues([]));
  }, []);

  return (
    <div className="map-page">
      <Navbar />
      <MapContainer center={JAKARTA_BARAT_CENTER} zoom={12} style={{ height: "80vh" }}>
        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
        {venues.map((v) => (
          <Marker key={v.venue_id} position={[v.latitude, v.longitude]}>
            <Popup>{v.nama}</Popup>
          </Marker>
        ))}
      </MapContainer>
    </div>
  );
}
