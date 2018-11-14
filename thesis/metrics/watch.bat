@echo off
echo "Welcome to the pandoc-watcher-compiler, by Daniel Robinson"
:loop  
timeout -t 1 >nul  
for %%i in (metrics.md) do echo %%~ai|find "a">nul || goto :loop

set STARTTIME=%TIME%
echo %STARTTIME% file was changed
call compile.bat
set ENDTIME=%TIME%

rem Change formatting for the start and end times
for /F "tokens=1-4 delims=:.," %%a in ("%STARTTIME%") do (
   set /A "start=(((%%a*60)+1%%b %% 100)*60+1%%c %% 100)*100+1%%d %% 100"
)
for /F "tokens=1-4 delims=:.," %%a in ("%ENDTIME%") do (
   set /A "end=(((%%a*60)+1%%b %% 100)*60+1%%c %% 100)*100+1%%d %% 100"
)

rem Calculate the elapsed time by subtracting values
set /A elapsed=end-start

rem Format the results for output
set /A hh=elapsed/(60*60*100), rest=elapsed%%(60*60*100), mm=rest/(60*100), rest%%=60*100, ss=rest/100, cc=rest%%100
if %hh% lss 10 set hh=0%hh%
if %mm% lss 10 set mm=0%mm%
if %ss% lss 10 set ss=0%ss%
if %cc% lss 10 set cc=0%cc%

set DURATION=%hh%:%mm%:%ss%,%cc%

rem "echo Start    : %STARTTIME%"
rem "echo Finish   : %ENDTIME%"
rem "echo          ---------------"
echo %ENDTIME% finished compiling in %DURATION% 

attrib -a metrics.md
goto :loop