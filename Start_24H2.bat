
@echo off&setlocal Enabledelayedexpansion

%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d "%~dp0"


@echo.
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\LanmanWorkstation" /v AllowInsecureGuestAuth /t REG_DWORD /d 1 /f
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters " /v RequireSecuritySignature /t REG_DWORD /d 0 /f



@echo.
echo Set time zone to China
tzutil /s "China Standard Time"

@echo.
echo Sync Time with Server
net time \\192.168.1.225 /set /y


@echo.
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v ConsentPromptBehaviorAdmin /t REG_DWORD /d 0 /f
Xcopy \\192.168.1.225\pm_tool\Tit.exe  C:\Users\%username%\Desktop
