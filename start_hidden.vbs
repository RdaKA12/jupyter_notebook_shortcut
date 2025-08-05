' This VBS script silently runs the Jupyter Notebook launcher batch file
' Update the path below with the full path to your .bat file

Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "<PATH_TO_YOUR_BAT_FILE>\start_notebook.bat" & Chr(34), 0
Set WshShell = Nothing
