import { useEffect, useState } from "react";
import { dashboardApi } from "../services/api";
import Navbar from "../components/Navbar";

// Section 12.2 Dashboard Page: summary cards + September venue/risk comparisons (Module 8).
export default function DashboardPage() {
  const [summary, setSummary] = useState(null);

  useEffect(() => {
    dashboardApi
      .summary()
      .then(({ data }) => setSummary(data))
      .catch(() => setSummary(null)); // endpoint not implemented yet — see backend TODO
  }, []);

  return (
    <div className="dashboard-page">
      <Navbar />
      <h1>Dashboard</h1>
      {/* TODO Sprint 11: summary cards (total venue, total omzet, total PBJT, jumlah anomali) */}
      {/* TODO Sprint 11: September venue comparison + risk distribution chart (recharts) */}
      <pre>{JSON.stringify(summary, null, 2)}</pre>
    </div>
  );
}
