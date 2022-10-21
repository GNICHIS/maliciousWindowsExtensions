On Error Resume Next

'VBS can be used to run hidden batch files, 

Set oShell = WScript.CreateObject ("WScript.Shell")
oShell.run "calc.exe"
Set oShell = Nothing