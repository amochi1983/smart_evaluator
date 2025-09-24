# Smart Evaluator Assistant - Deployment Guide

This document explains how to deploy the Smart Evaluator Assistant prototype on different platforms.

## Option 1: Streamlit Cloud (Recommended)
The easiest method to deploy and make the app public.

### Prerequisites
- GitHub account  
- Streamlit Cloud account (free)  

### Steps
1. Create GitHub repository and push code  
2. Log in to [Streamlit Cloud](https://streamlit.io/cloud)  
3. Click "New app", select repo, set `app.py` as entry point, then Deploy  
4. You’ll get a public URL to share  

## Option 2: Heroku
For deployment on Heroku.  
- Requires Heroku account + Heroku CLI  

### Steps
- Create `Procfile`: `web: streamlit run app.py --server.port $PORT`  
- Create `runtime.txt`: `python-3.11.0`  
- Deploy using `git push heroku main`  

## Option 3: GitHub Pages (Static Preview)
For static screenshots instead of full interactivity.

### Steps
- Take screenshots of each page  
- Create a simple HTML page embedding them  
- Push to `gh-pages` branch and enable GitHub Pages  

## Option 4: Local Deployment
For running locally.  
- Prerequisites: Python 3.11+, pip  
- Steps: clone repo, install `requirements.txt`, run `streamlit run app.py`, open `http://localhost:8501`  
