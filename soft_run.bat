@echo off
echo Starting Interior Bazzar Django Server...
REM Start the server
echo Starting server on http://127.0.0.1:8888/
python -m uvicorn interior_bazzar.asgi:application --port 8888 --host 0.0.0.0

pause 