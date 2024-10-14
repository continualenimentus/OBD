# Obsidian brain dumper

## Description
This application is intended to be used along with some other existing applications to make note taking and keeping a clear mind easy.
The intention is to allow a Obsidian(or other markdown note taking app) user to use a set hotkey to bring up a prompt that will
write whatever is on their mind directly into a markdown file without bringing up another application.  A similar application already
exists on mobile(put the link here) and it is what Obsidian brain dumper is based on.  This application assumes the user has the knowledge
to correctly install Obsidian(or already has it) and Auto Hot Key.  A video will be made available at [this link](https://youtu.be/rK9AkaN-1Ng)
on how to install, configure and use everything.

## Specifications
This application was developed using python 3.12.3 and customtkinter(a visual library).  It uses JSON files for configuration and
i18n(allowing multiple languages to be supported).  The only current language is English however everything has been put in place for a
user to add their own language file and switch to it if they wish to do so.  This process will also be described in [this video](https://youtu.be/rK9AkaN-1Ng)
for the user to follow along.  The application is made to be functionnal even if the configuration and language files are deleted(it will 
recreate said files from a template), but not if they are modified.

## Links
Link to Python download page: https://www.python.org/downloads/
Link to the download page for AutoHotKey 2: https://www.autohotkey.com/v2/

## Installation and usage
This guide/demonstration assumes the user is using Obsidian and AutoHotKey
1. Install Python version 3.12.3 or later
2. Download the code for OBD
3. Move the file outside of the downloads folder(unknown bugs have been found when trying to do it from the downloads folder)
4. Open a command prompt where the files have been downloaded
5. Run the following command in the command prompt that was just opened `pip install customtkinter` (this will install the visual library)
6. Download AutoHotKey(an application that allows the setting of custom hotkey combinations)
7. Install AutoHotKey
8. Add a custom hotkey (example in OBD.ahk, it will need to be moved to where AutoHotKey keeps it scripts, you can find it by creating a new script)
9. Restart the AutoHotKey script
10. Add AutoHotKey to your startup applications(this step is not necessary but if not done the user will have to manually start it every 
time their computer is turned off, script OBD.ps1 should work)
   a. Press Windows+R simoutaneously
   b. Type `shell:startup` (will open the directory where your startup apps will be)
   c. Modify the OBD.ps1 script so it points to the location of your OBD.ahk script then save it
   d. Next time your PC starts, it should automatically boot AutoHotKey with the correct script
11. Try the hotkey combination(should work, a window will be brought up)
12. Click the configure button in OBD
13. Set the folder as the place in your obsidian vault where you want the application to add the notes to
14. Set the name of the file that should be created/edited.
    By adding the date here, you can have a note a day or if you want every one to be its individual note you can add only the time to the file name
15. Set the writing template(keep in mind the application writes a .md file so any .md syntax will show as such)
16. Set the writing mode
17. Click save
 The application should now be fully functionnal.  You can use the RETURN/ENTER key to write the text or the ESCAPE key to exit the application
    The main color of the application is the theme of your computer.