import axios from "axios";

const api = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL || "http://localhost:8000/api/v1",
});

// Attach the JWT (if present) to every outgoing request.
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("tis_token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const authApi = {
  login: (email, password) => api.post("/auth/login", { email, password }),
};

export const venueApi = {
  list: () => api.get("/venues"),
  create: (payload) => api.post("/venues", payload),
  update: (venueId, payload) => api.put(`/venues/${venueId}`, payload),
  remove: (venueId) => api.delete(`/venues/${venueId}`),
};

export const revenueApi = {
  estimate: (venueId) => api.get(`/revenue/${venueId}/estimate`),
};

export const anomalyApi = {
  get: (venueId) => api.get(`/anomaly/${venueId}`),
};

export const sustainabilityApi = {
  get: (venueId) => api.get(`/sustainability/${venueId}`),
};

export const dashboardApi = {
  summary: () => api.get("/dashboard/summary"),
};

export default api;
