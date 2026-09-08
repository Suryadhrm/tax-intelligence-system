import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function Navbar() {
  const { logout } = useAuth();
  return (
    <nav>
      <Link to="/dashboard">Dashboard</Link>
      <Link to="/map">Peta</Link>
      <button onClick={logout}>Keluar</button>
    </nav>
  );
}
