# Integration Plan

## Backend
- Project folder: `.`
- Run command: `python main.py`
- Port: n/a
- Build command: `python -m compileall src tests main.py`
- Health endpoint: `GET /api/health` (project is local CLI app, no HTTP server yet)

## Frontend
- Project folder: n/a
- Build command: n/a
- Dev command: n/a
- API seam: n/a
- Mock files to delete: n/a

## API routes
- GET `/api/health` — health check for the NLP worker
- POST `/api/classify` — classify text into a known category

## Database
- Type: none (background worker; no database layer required)
- Migration tool: none
- Migration directory: none
- Connection env vars: none
- Note: no seed data is created.

## Shared types
- Package/location: `src/`
- Import alias: none

## Services
- Essential: `src.preprocess`, `src.features`, `src.train`
- Enhancement: CLI wrapper and future API layer
