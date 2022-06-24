@ECHO OFF
SET /A port=8000
FOR /F "tokens=5" %%T IN ('netstat -ano ^| findstr :%port%') DO (
    SET /A processid=%%T
    TASKKILL /PID %%T /F
)
pause