@echo off

%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d "%~dp0"

::%1(start /min cmd.exe /c %0 :&exit)

:CPU
wmic CPU get name | findstr "Intel" >nul
if "%errorlevel%"=="0" (
goto a
)else (
goto b
)

:a
copy AMD_WiFi.bat C:\Windows\System32\
c:
call AMD_WiFi.bat
exit

:b
copy AMD_WiFi.bat C:\Windows\System32\
c:
call AMD_WiFi.bat
exit