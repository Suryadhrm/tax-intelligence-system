import { Navigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

// Module 1 (RBAC): blocks access to authenticated pages until a token exists.
// Extend with a `roles` prop + role check once per-page role restrictions are needed.
export default function ProtectedRoute({ children }) {
  const { token } = useAuth();
  if (!token) {
    return <Navigate to="/login" replace />;
  }
  return children;
}
