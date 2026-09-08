# Frontend — Tax Intelligence System (React PWA)

## Setup

```bash
npm install
cp .env.example .env
npm start
```

## Structure

```
src/
  pages/       # one file per PRD UI/UX page: Login, Dashboard, Map, VenueDetail
  components/  # shared UI pieces (Navbar, ProtectedRoute, ...)
  services/    # api.js — axios client talking to the FastAPI backend
  context/     # AuthContext — stores JWT + role, drives RBAC in the UI
```

PWA config (manifest, service worker) lives in `public/`.
