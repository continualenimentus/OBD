# Example of Markdown Tags

## Headers
# H1 Header
## H2 Header
### H3 Header
#### H4 Header
##### H5 Header
###### H6 Header

## Emphasis
*Italic text*  
**Bold text**  
***Bold and italic text***

## Lists
### Unordered List
- Item 1
- Item 2
    - Subitem 2.1
    - Subitem 2.2

### Ordered List
1. First item
2. Second item
     1. Subitem 2.1
     2. Subitem 2.2

## Links
[GitHub](https://github.com)

## Images
![Alt text](https://via.placeholder.com/150)

## Blockquotes
> This is a blockquote.

## Code
Inline `code`

```python
# Code block
print("Hello, World!")
```

## Tables
| Header 1 | Header 2 |
|----------|----------|
| Row 1    | Data 1   |
| Row 2    | Data 2   |

## Horizontal Rule
---

## Task List
- [x] Task 1
- [ ] Task 2

# Obsidian brain dumper

## Description
This application is intended to be used along with some other existing applications to make note taking and keeping a clear mind easy.
The intention is to allow a Obsidian(or other markdown note taking app) user to use a set hotkey to bring up a prompt that will
write whatever is on their mind directly into a markdown file without bringing up another application.  A similar application already
exists on mobile(put the link here) and it is what Obsidian brain dumper is based on.  This application assumes the user has the knowledge
to correctly install Obsidian(or already has it) and Auto Hot Key.  A video will be made available at [this link](https://github.com)
on how to install, configure and use everything.

## Specifications
This application was developed using python 3.12.3 and customtkinter(a visual library).  It uses JSON files for configuration and
i18n(allowing multiple languages to be supported).  The only current language is English however everything has been put in place for a
user to add their own language file and switch to it if they wish to do so.  This process will also be described in [this video](https://github.com)
for the user to follow along.  The application is made to be functionnal even if the configuration and language files are deleted(it will 
recreate said files from a template), but not if they are modified.

## Installation and usage
This guide/demonstration assumes the user is using Obsidian and AutoHotKey
1. Install Python version 3.12.3 or later
2. Download the code for OBD
3. Move the file outside of the downloads folder(unknown bugs have been found when trying to do it from the downloads folder)
3. Open a command prompt where the files have been downloaded
4. Run the following command in the command prompt that was just opened `npm install customtkinter` (this will install the visual library)
5. Create a shortcut to OBD.py
6. Download AutoHotKey(an application that allows the setting of custom hotkey combinations)
7. Install AutoHotKey
8. Add AutoHotKey to your startup applications(this step is not necessary but if not done the user will have to manually start it every 
time their computer is turned off)
 Add a custom hotkey calling to the shortcut created at step 5
 Restart the AutoHotKey script
 Try the hotkey combination(should work, a window will be brought up)
 Click the configure button
 Set the folder as the place in your obsidian vault where you want the application to add the notes to
 Set the name of the file that should be created/edited.
    By adding the date here, you can have a note a day or if you want every one to be its individual note you can add only the time to the file name
 Set the writing template(keep in mind the application writes a .md file so any .md syntax will show as such)
 Set the writing mode
 Click save
 The application should now be fully functionnal.  You can use the RETURN/ENTER key to write the text or the ESCAPE key to exit the application
    The main color of the application is the theme of your computer.
   