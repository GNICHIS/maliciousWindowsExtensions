# maliciousWindowsExtensions

In this repo, I just share what I believe to be a complete list of malicious extensions files that can be used in APT attacks and more precisely in spear-phishing attacks.

### What I mean when I say a malicious file ! 

Can .VBS files for example really be malicious ? no !
They are not. In fact, Visual basic script is nothing but just an Active Scripting language developed by Microsoft that is modeled on Visual Basic. It allows Microsoft Windows system administrators to generate powerful tools for managing computers with error handling, subroutines, and other advanced programming constructs. However apt actor can exploit the fact that such a scripting language can be used to create "softwares" equivalent in many features (command execution, download file from the internet, and execute it) to softwares created by a language like C++ in order to create Trojan downloader.

### What is special about these files ?

As I mentioned above these scripting languages can be exploited to create trojan downloader (which is a malicious software typically used to download a full capable RAT).

They are unkown and/or forgetten about ! 

A sophisticated apt actors can trick the users to run such unknown and forgetten files in their workstation, executing codes without the need to use advanced 0-day exploits.
And if you study a lot of APT operations will be surprised about the huge number of groups building their attacks based on this simple and effective technique, including a lot of the most sophisticated groups.

For certain, VBS files are so obvious and well known; but what about .wsh ? or .scr ? or ...!

And not just the "average" user who miss this technical knowledge, In the recent years I have been testing so many anti-phising solutions that claim the ability to filter out all the malicious extensions !
However, when I was testing these solutions, I usually endup finding at least 4 or 5 extensions that aren't filtered.


### How to use this repo ?
This repo is divided into many folders; each folder for a specific file extension. In each folder you will find two files : Readme.md for "documentation" and test.ext which will contain an example of an executable code.

Needless to say that you can not create a full functional remote access trojans based on these scripting languages, you can not create a keylogger or a tool to monitor a screen with VBS, but you can at least create a downloader,

If the suggested code(s) are not enough for what you are looking for, then just search for what you need.
I also may not complete all the required codes for all extensions, it is up to you to do a further search.

#### I'm sorry I'm a lazy person :') 

### How to test !
The approach of testing that I suggest is very simple, When you get access to an email box either via taking over an employee's email account or directly via asking the system administrator!
All what you need to do is to test each file extension per email ! 


Send an email with an attached empty file holding the desired extension,
If the email pass, then the extension is not filtered, otherwise it is. (as simple as that)