import customtkinter
import tkinter
from datetime import datetime
from tkinter import filedialog
import os
import json

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

default_config = {
    "language": "en",
    "filePath": "",
    "fileName": "",
    "languages": [
        {
            "name": "en",
            "value": "English",
            "source": "./languages/en.json"
        }
    ],
    "writing_mode": "prepend",
    "writeTemplate": "- [ ] {text} \n"
}


current_date_example = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

default_language_data = {
    "title": "Add Note",
    "placeholder": "Insert value or text",
    "cancel": "Cancel",
    "ok": "Ok",
    "configure": "Configure",
    "config_screen": "Configure the settings for the plugin",
    "prepend": "Prepend",
    "append": "Append",
    "override": "Override",
    "file_path": "Select the location where you would like the text to be written to",
    "current_file": "Current file is writting at: ",
    "pick_folder": "Pick Folder",
    "file_name": "Enter the name of the file you would like to write to.",
    "save": "Save",
    "no_file_path": "No file path selected.",
    "name_entry_info": "  In order to add the date/time to the name of the file,\n use brackets ({ and }) to indicate following this example: \n my_file_{yyyy}-{mm}-{dd} {HH}:{MM}:{SS} \nwill become my_file_"+current_date_example+".\nIndividual parts of this will work.",
    "template_entry_info": "Escape characters and normal mark down syntax will work.\n Please indicate where the text should go by using {text}.\n A complete list of escape characters and .md syntax\n can be found online.  Escape characters of an already \nsaved template will not be displayed in the box.",
    "template": "Enter the template for the text you would like to write to the file.",
    "desc_prepend": "Prepend will put the text you enter at the beginning of the file\n and push the rest down.",
    "desc_append": "Append will put the text you enter at the end of the file.",
    "desc_override": "Override will replace the contents of the file\n with the text you enter.",
}

def load_config():
    try:
        with open("config.json", "r") as json_file:
            return json.load(json_file)
    except Exception as e:
        # initial setup/problem with the config file, returning to default values and creating the file
        with open("config.json", 'w') as file:
            json.dump(default_config, file, indent=4)
            return default_config
        
config_data = load_config()

def get_language_source():
    for lang in config_data["languages"]:
        if lang["name"] == config_data["language"]:
            return lang["source"]
        
def load_lang():
    lang = get_language_source()
    try:
        with open(lang, "r") as json_file:
            return json.load(json_file)
    except Exception as e:
        # problem with the lang file, returning to default english values and creating the file
        try:
            # Create the directory first
            os.makedirs("./languages", exist_ok=True)

            with open("./languages/en.json", 'w') as file:
                json.dump(default_language_data, file, indent=4)
                return default_language_data
        except FileNotFoundError as e:
            # This should not happen if os.makedirs was successful
            print("Unexpected FileNotFoundError:", e)
        except FileExistsError as e:
            print("Language file already exists.")
            # You might want to overwrite or handle this differently
            return default_language_data
        except Exception as e:
            # could not create the file or access the file, exiting
            exit()


language_data = load_lang()
print(language_data)


# POPUP
def show_config():
  global selected_file_path 
  selected_file_path = config_data["filePath"]
  # Create a new window for the popup
  popup = customtkinter.CTk()
  
  popup.configure(bg=root['bg'])
  
  radio_writing_mode = customtkinter.StringVar(value=config_data["writing_mode"])
  popup.title('Configuration')
  popup.iconbitmap("./Check.ico")

  radio_prepend = customtkinter.CTkRadioButton(master=popup, text=language_data['prepend'], variable=radio_writing_mode, value="prepend")
  prepen_desc = customtkinter.CTkLabel(master=popup, text=language_data['desc_prepend'], fg_color="white", text_color="black", corner_radius=10, padx=5, pady=5)
  prepen_desc.place(x=999999, y=999999)

  def show_prepend_desc(event):
    posx = event.x_root - (popup.winfo_rootx())-75
    posy = event.y_root - popup.winfo_rooty() + 30
    prepen_desc.place(x=posx, y=posy)
    prepen_desc.lift()

  def hide_prepend_desc(event):
    prepen_desc.place_forget()

  radio_prepend.bind("<Enter>", show_prepend_desc)
  radio_prepend.bind("<Leave>", hide_prepend_desc)

  radio_append = customtkinter.CTkRadioButton(master=popup, text=language_data['append'], variable=radio_writing_mode, value="append")
  append_desc = customtkinter.CTkLabel(master=popup, text=language_data['desc_append'], fg_color="white", text_color="black", corner_radius=10, padx=5, pady=5)
  append_desc.place(x=999999, y=999999)

  def show_append_desc(event):
    posx = event.x_root - (popup.winfo_rootx())-75
    posy = event.y_root - popup.winfo_rooty() + 30
    append_desc.place(x=posx, y=posy)
    append_desc.lift()

  def hide_append_desc(event):
    append_desc.place_forget()

  radio_append.bind("<Enter>", show_append_desc)
  radio_append.bind("<Leave>", hide_append_desc)

  radio_override = customtkinter.CTkRadioButton(master=popup, text=language_data['override'], variable=radio_writing_mode, value="override")
  override_desc = customtkinter.CTkLabel(master=popup, text=language_data['desc_override'], fg_color="white", text_color="black", corner_radius=10, padx=5, pady=5)
  override_desc.place(x=999999, y=999999)
  
  def show_override_desc(event):
    posx = event.x_root - (popup.winfo_rootx())-75
    posy = event.y_root - popup.winfo_rooty() -60
    override_desc.place(x=posx, y=posy)
    override_desc.lift()

  def hide_override_desc(event):
    override_desc.place_forget()

  radio_override.bind("<Enter>", show_override_desc)
  radio_override.bind("<Leave>", hide_override_desc)
  
  def pick_folder():
    global selected_file_path
    selected_file_path = filedialog.askdirectory()
    current_file_path_label.configure(text=language_data["current_file"]+selected_file_path)

  # Entry field for user input
  file_path_label = customtkinter.CTkLabel(master=popup, text=language_data['file_path'], width=450, padx=10, pady=5)
  file_path_label.grid(row=0, column=0, columnspan = 2, padx = 5, pady=5)
  display_text = selected_file_path if selected_file_path != "" else language_data["no_file_path"]
  current_file_path_label = customtkinter.CTkLabel(master=popup, text=language_data["current_file"]+display_text, width=150, padx=10, pady=5)
  current_file_path_label.grid(row=1, column=0, columnspan = 2, padx = 5, pady=5)
  file_path_entry = customtkinter.CTkButton(master=popup, width=300, command=pick_folder, text=language_data["pick_folder"])
  file_path_entry.grid(row=2, column=0, columnspan = 2, padx = 5, pady=5)
  # Come up with a solid set of instructions/characters to replace(date/time, etc)

# --starting with the info icon
  file_name_frame = customtkinter.CTkFrame(master=popup, fg_color=root['bg'])	
  file_name_frame.grid(row=3, column=0, columnspan = 2, padx = 5, pady=5)
  file_name_label = customtkinter.CTkLabel(width = 330, master=file_name_frame, text=language_data['file_name'], padx=10, pady=5)
  file_name_label.grid(row=0, column=0)
  info_icon = customtkinter.CTkLabel(master=file_name_frame, text="?", width=20, height=20, fg_color="gray", text_color="white", corner_radius=10)
  info_icon.grid(row=0, column=1)
  

# Create a label for additional information
  info_label = customtkinter.CTkLabel(master=popup, text=language_data['name_entry_info'], width=200, height=100, fg_color="white", text_color="black", corner_radius=10)
  info_label.grid(row=4, column=0, columnspan = 2)
  info_label.place(x=999999, y=999999)
  info_label.place_forget()
  def show_info(event):
    width = info_label.winfo_width()if info_label_template.winfo_width()>20 else 342
    posx = event.x_root - (popup.winfo_rootx()+width)
    posy = event.y_root - popup.winfo_rooty() + 20
    info_label.place(x=posx, y=posy, anchor="nw")
    info_label.lift()

  def hide_info(event):
    info_label.place_forget()

# Bind hover events to the info icon
  info_icon.bind("<Enter>", show_info)
  info_icon.bind("<Leave>", hide_info)
# --done with the info icon

  file_name_entry = customtkinter.CTkEntry(master=popup, width=300, placeholder_text=config_data["fileName"])
  file_name_entry.grid(row=5, column=0, columnspan = 2, padx = 5, pady=5)
  write_template_frame = customtkinter.CTkFrame(master=popup, fg_color=root['bg'])
  write_template_frame.grid(row=6, column=0, columnspan = 2, padx = 5, pady=5)
  write_template_frame = customtkinter.CTkLabel(width = 330, master=write_template_frame, padx=5, text=language_data['template'])
  write_template_frame.grid(row=0, column=0)

# Create a label for additional information
  info_label_template = customtkinter.CTkLabel(master=popup, text=language_data['template_entry_info'], width=200, height=100, fg_color="white", text_color="black", corner_radius=10)
  info_label_template.grid(row=4, column=0, columnspan = 2)
  info_label_template.place(x=999999, y=999999)
  info_label_template.place_forget()
  
  info_icon_template = customtkinter.CTkLabel(master=write_template_frame, text="?", width=20, height=20, fg_color="gray", text_color="white", corner_radius=10)
  info_icon_template.grid(row=0, column=1)

  def show_info_template(event):
    width =info_label_template.winfo_width() if info_label_template.winfo_width()>20 else 342
    posx = event.x_root - (popup.winfo_rootx()+width)
    posy = event.y_root - popup.winfo_rooty() + 20
    info_label_template.place(x=posx, y=posy)
    info_label_template.lift()

  def hide_info_template(event):
    info_label_template.place_forget()

# Bind hover events to the info icon
  info_icon_template.bind("<Enter>", show_info_template)
  info_icon_template.bind("<Leave>", hide_info_template)

#   donesoes
  write_template = customtkinter.CTkEntry(master=popup, width=300, placeholder_text=config_data["writeTemplate"])
  write_template.grid(row=7, column=0, columnspan = 2, padx = 5, pady=5)

# Create a dropdown menu for language selection
  language_options = [lang["value"] for lang in config_data["languages"]]
  selected_language = customtkinter.StringVar(value=config_data["languages"][0]["value"])
  def on_language_change(new_value):
    for lang in config_data["languages"]:
        if lang["value"] == new_value:
            change_language(lang["name"])
            break

  def change_language(newLang):
    global language_data
    # write the new language to the config file
    config_data["language"] = newLang
    with open("config.json", "w") as json_file:
        json.dump(config_data, json_file, indent=4)
    language_data = load_lang()
    addText()
    change_popup_language()

  def change_popup_language():
    radio_prepend.config(text=language_data["prepend"])
    radio_append.config(text=language_data["append"])
    radio_override.config(text=language_data["override"])
    file_path_label.config(text=language_data["file_path"])
    current_file_path_label.config(text=language_data["current_file"])
    file_path_entry.config(text=language_data["pick_folder"])
    file_name_label.config(text=language_data["file_name"])
    button_submit.config(text=language_data["save"])
    button_cancel.config(text=language_data["cancel"])

  language_dropdown = customtkinter.CTkOptionMenu(master=popup, variable=selected_language, values=language_options, command=on_language_change)
  language_dropdown.grid(row=9, column=1, padx = 5, pady=5)

  radio_prepend.grid(row=9, column=0, padx = 5, pady=5)
  radio_append.grid(row=10, column=0, padx = 5, pady=5)
  radio_override.grid(row=11, column=0, padx = 5, pady=5)

  # Define buttons for the popup
  def submit():
    global selected_file_path

    temp_file_name = file_name_entry.get()
    if(temp_file_name == ""):
        temp_file_name = config_data["fileName"]
    if(temp_file_name != config_data["fileName"]):
        config_data["fileName"] = temp_file_name
    if(selected_file_path != config_data["filePath"]):
        config_data["filePath"] = selected_file_path
        
    # TODO, look for the right language, this gues the name instead of the letter code
    if(selected_language.get() != config_data["language"]):
        config_data["language"] = selected_language.get()

    # this will change place to be in the add_to_obsidian function, replacement here will always result in an override
    # file_name = file_name_entry.get()
    # today = datetime.now()
    template = write_template.get()
    if(template != config_data["writeTemplate"]):
        if(template != ""):
            config_data["writeTemplate"] = template

    # 
    # print(file_name)
    if(selected_file_path == ""):

        # indicate to the user they need to set a file name
        return
    if(radio_writing_mode.get() != config_data["writing_mode"]):
        config_data["writing_mode"] = radio_writing_mode.get()
    config_data["filePath"] = selected_file_path
    with open("config.json", "w") as json_file:
        json.dump(config_data, json_file, indent=4)
    file_name_entry.delete(0, tkinter.END)  # Clear the entry
    popup.destroy()  # Close the popup window

  def close_popup():
    popup.destroy()  # Close the popup window without saving
  button_frame = customtkinter.CTkFrame(master=popup, fg_color=root['bg'])
  button_frame.grid(row=12, column=0, columnspan=2, padx=5, pady=5)

  # Create buttons with appropriate styling
  button_submit = customtkinter.CTkButton(master=button_frame, text='Save', command=submit, 
                                          fg_color=popup['bg'], hover_color=buttonColor, width=100, text_color=textColor)
  button_submit.grid(row=0, column=0)

  empty_label = customtkinter.CTkLabel(master=button_frame, text="", width=100)
  empty_label.grid(row=0, column=1)
  button_cancel = customtkinter.CTkButton(master=button_frame, text=language_data["cancel"], command=close_popup, 
                                          fg_color=popup['bg'], hover_color=buttonColor, width=100, text_color=textColor)
  button_cancel.grid(row=0, column=2)
  
  popup.mainloop()


root = customtkinter.CTk()
menuBar = tkinter.Menu(root)
root.title(language_data["title"])
root.iconbitmap("./Check.ico")

buttonColor = "#212121" if root['bg'] == "gray10" else "#E5E5E5"
textColor = "#D6D6D6" if root['bg'] == "gray10" else '#04127B'

frame = customtkinter.CTkFrame(master=root)
frame.pack(fill="both", expand=True)


entry1 = customtkinter.CTkEntry(master=frame, placeholder_text=language_data['placeholder'], width = 300)
entry1.grid(column=0, row=0, columnspan=4, sticky="ew", padx = 10, pady = (17, 10))

def cancel():
    # TODO investigate if the next line is necessary, doesn't seem to be
    entry1.delete(0, tkinter.END)
    exit()

def addToObsidian():
    # need to configure the path here according to what the user has set in the config file
    today = datetime.now()
    text = entry1.get()
    template = config_data["writeTemplate"]
    temp_text = template.replace("{text}", text)
    text = temp_text
    print(text)
    # craft the file path using the json file
    filepath = config_data["filePath"]
    file_name = config_data["fileName"]
    if "{" in file_name and "}" in file_name:
        replacements = {
            "yyyy": today.strftime("%Y"),
            "yy": today.strftime("%y"),
            "mm": today.strftime("%m"),
            "dd": today.strftime("%d"),
            "HH": today.strftime("%H"),
            "MM": today.strftime("%M"),
            "SS": today.strftime("%S")
        }

        for key, value in replacements.items():
            file_name = file_name.replace(f"{{{key}}}", value)
    file_to_write = filepath+"/"+file_name+".md"
    print(file_to_write)
    
    if not os.path.exists(file_to_write):
        with open(file_to_write, "w") as myfile:
            myfile.write("")

    print(text)

    with open(file_to_write, "r+") as myfile:
        if config_data["writing_mode"] == "prepend":
            current_text = myfile.read()
            myfile.seek(0, 0)
            myfile.write(text + current_text)
        elif config_data["writing_mode"] == "append":
            myfile.seek(0, 2)
            myfile.write(text)
    if config_data["writing_mode"] == "override":
        with open(file_to_write, "w") as myfile:
            myfile.write(text)
    entry1.delete(0, tkinter.END)
    exit()

label = customtkinter.CTkLabel(master=frame,text="",  width=150, padx = 10, pady = 5)
label.grid(column=0, row=1)

buttonCancel = customtkinter.CTkButton(master=frame, text=language_data['cancel'], command=cancel, 
                                       fg_color=buttonColor,
                                       hover_color=buttonColor, 
                                       width=75,
                                       text_color=textColor)
buttonCancel.grid(column=2, row=1, padx = 0, pady = (0, 8))
buttonAdd = customtkinter.CTkButton(master=frame, text=language_data['ok'], command=addToObsidian, 
                                    fg_color=buttonColor, 
                                    hover_color=buttonColor, 
                                    width=75,
                                    text_color=textColor)
buttonAdd.grid(column=3, row=1, padx = 0, pady = (0, 8))
hidden_label = customtkinter.CTkLabel(master=frame, text="", width=100)
hidden_label.grid(column=1, row=1)

button_popup = customtkinter.CTkButton(master=frame, text=language_data['configure'], command=show_config, 
                                        fg_color=buttonColor, hover_color=buttonColor, width=150, text_color=textColor)
button_popup.grid(column=0, row=1, padx=10, pady=10)

root.bind("<Escape>", lambda e: cancel())
root.bind("<Return>", lambda e: addToObsidian())


def addText():
    
    label.config(text=language_data["config_screen"])
    entry1.placeholder_text = language_data["placeholder"]
    buttonCancel.config(text=language_data["cancel"])
    buttonAdd.config(text=language_data["ok"])
    button_popup.config(text=language_data["configure"])

root.mainloop()