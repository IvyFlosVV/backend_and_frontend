# Ivy-Bot Backend (15113 Project)

## Overview
This is a simple Flask backend service hosted on Render. It acts as a secure proxy between my portfolio website and the Google Gemini API.

## Endpoints
- **POST /chat**: Accepts a JSON object `{"message": "user text"}`. 
- **Returns**: A JSON response `{"reply": "AI response"}`.

## Communication
The frontend (GitHub Pages) uses the `fetch()` API to send user input to the Render URL. The backend injects a specific "Ivy Persona" system prompt before forwarding the request to Gemini 1.5 Flash.

## Security & Secrets
The **GEMINI_API_KEY** is stored as an Environment Variable on Render. It is never exposed in the frontend code or committed to GitHub, fulfilling the assignment's security requirements.