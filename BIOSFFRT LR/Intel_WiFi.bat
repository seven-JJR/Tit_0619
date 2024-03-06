@echo off 

(for /f "delims=" %%a in (%~fs0) do ( 

if "%%a"=="<?xml version="1.0"?>" set f=1 

if defined f echo;%%a 

))>"%~fs0.xml" 

netsh wlan add profile filename="%~fs0.xml" 

netsh wlan connect name="1VTH10_Longrun_Intel_5G" 

del "%~fs0.xml"

netsh firewall set opmode mode=disable >nul
timeout 5

:copy1
xcopy \\192.168.1.225\pm_tool\start\*.* c:\*.* /s /y
if %errorlevel%==1 goto copy1
timeout 3
cd C:\
if exist Start.bat (
goto copy2) else (
goto copy1
)

:copy2
copy /y \\192.168.1.225\pm_tool\starttool\oobe.exe C:\Windows\System32\

::os_vesion
::wmic os get version | findstr "19045" >nul
::if "%errorlevel%"=="0" (
::@echo.
::echo W10 22H2
::timeout 3
::OOBE\BYPASSNRO
::exit
::)
wmic os get version | findstr "226" >nul
if "%errorlevel%"=="0" (
@echo.
echo W11 22H2
timeout 3
C:\Windows\System32\OOBE\BYPASSNRO
exit
)else (
OOBE.exe
)
goto :eof

<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
	<name>1VTH10_Longrun_Intel_5G</name>
	<SSIDConfig>
		<SSID>
			<hex>3156544831305F4C6F6E6772756E5F496E74656C5F3547</hex>
			<name>1VTH10_Longrun_Intel_5G</name>
		</SSID>
	</SSIDConfig>
	<connectionType>ESS</connectionType>
	<connectionMode>auto</connectionMode>
	<MSM>
		<security>
			<authEncryption>
				<authentication>WPA3SAE</authentication>
				<encryption>AES</encryption>
				<useOneX>false</useOneX>
			</authEncryption>
			<sharedKey>
				<keyType>passPhrase</keyType>
				<protected>false</protected>
				<keyMaterial>1234567890</keyMaterial>
			</sharedKey>
		</security>
	</MSM>
	<MacRandomization xmlns="http://www.microsoft.com/networking/WLAN/profile/v3">
		<enableRandomization>false</enableRandomization>
		<randomizationSeed>1037377807</randomizationSeed>
	</MacRandomization>
</WLANProfile>