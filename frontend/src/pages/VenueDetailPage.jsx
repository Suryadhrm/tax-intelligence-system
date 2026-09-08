import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { venueApi, revenueApi, anomalyApi, sustainabilityApi } from "../services/api";
import Navbar from "../components/Navbar";

// Section 12.4 Venue Detail Page: profile + prediction + PBJT + risk + sustainability.
export default function VenueDetailPage() {
  const { venueId } = useParams();
  const [venue, setVenue] = useState(null);
  const [revenue, setRevenue] = useState(null);
  const [anomaly, setAnomaly] = useState(null);
  const [sustainability, setSustainability] = useState(null);

  useEffect(() => {
    venueApi.list().then(({ data }) => setVenue(data.find((v) => v.venue_id === venueId)));
    revenueApi.estimate(venueId).then(({ data }) => setRevenue(data)).catch(() => {});
    anomalyApi.get(venueId).then(({ data }) => setAnomaly(data)).catch(() => {});
    sustainabilityApi.get(venueId).then(({ data }) => setSustainability(data)).catch(() => {});
  }, [venueId]);

  return (
    <div className="venue-detail-page">
      <Navbar />
      <h1>{venue?.nama || "Memuat..."}</h1>

      <section>
        <h2>Profil</h2>
        <pre>{JSON.stringify(venue, null, 2)}</pre>
      </section>

      <section>
        <h2>Prediksi Omzet & PBJT</h2>
        <pre>{JSON.stringify(revenue, null, 2)}</pre>
      </section>

      <section>
        <h2>Risiko Anomali</h2>
        <pre>{JSON.stringify(anomaly, null, 2)}</pre>
      </section>

      <section>
        <h2>Sustainability</h2>
        <pre>{JSON.stringify(sustainability, null, 2)}</pre>
      </section>
    </div>
  );
}
