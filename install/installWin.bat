@Echo off

rem installs to C:\pyScripts
mkdir C:\pyScripts
copy ..\pycat.py C:\pyScripts\pycat.py
copy ..\pyget.py C:\pyScripts\pyget.py
copy ..\pygrep.py C:\pyScripts\pygrep.py

rem Installs to PATH
setx path "%path%;C:\Windows\pyScripts"
