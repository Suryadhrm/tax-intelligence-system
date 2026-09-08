import { createContext, useContext, useState } from "react";
import { authApi } from "../services/api";

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [token, setToken] = useState(localStorage.getItem("tis_token"));
  const [role, setRole] = useState(localStorage.getItem("tis_role"));

  async function login(email, password) {
    const { data } = await authApi.login(email, password);
    localStorage.setItem("tis_token", data.access_token);
    // NOTE: decode role from the JWT payload once a jwt-decode dependency is added;
    // for now the backend can also return role alongside the token if convenient.
    setToken(data.access_token);
  }

  function logout() {
    localStorage.removeItem("tis_token");
    localStorage.removeItem("tis_role");
    setToken(null);
    setRole(null);
  }

  return (
    <AuthContext.Provider value={{ token, role, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}
