@echo off
REM Virtual environment activation
echo =======================================================
echo Virtual environment activation
call "%~dp0..\socomecenv\Scripts\activate"
REM Update Requirements
echo =======================================================
echo Update Requirements (requirements.txt)
python -m pip freeze --local > requirements.txt
echo =======================================================
echo Project virtual environment requirements.txt is updated
echo =======================================================
pause