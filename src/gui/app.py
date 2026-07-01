import customtkinter as ctk 

#--------------------------------
#Functions
#--------------------------------

def show_basic():
    title_label.configure(
        text="Basic Calculator"
    )

def show_mechanics():
    title_label.configure(
        text="Mechanics Calculator"
    )

def show_thermodynamics():
    title_label.configure(
        text="Thermodynamics Calculator"
    )

def show_fluids():
    title_label.configure(
        text="Fluids Calculator"
    )

def show_physics():
    title_label.configure(
        text="Physics Calculator"
    )

def show_converter():
    title_label.configure(
        text="Converter"
    )        

def show_scientific():
    title_label.configure(
        text="Scientific Calculator"
    )

def show_material_properties():
    title_label.configure(
        text="Material Properties"
    )

def button_click(value):

    print(repr(value))

    if value == "AC":
        display.delete(0, "end")
        display.insert(0, "0")

    elif value == "⌫":

        current =display.get()

        current = current[:-1]

        display.delete(0,"end")

        if current == "":
            display.insert(0, "0")
        else:
            display.insert(0, current) 

    else:

        if display.get() == "0":
            display.delete(0, "end")               
                           

        display.insert("end", value)


#--------------------------------
# Window
#--------------------------------

app = ctk.CTk()

app.title("Engineering Calculator")

app.geometry("1000x700")

#--------------------------------
# Header
#--------------------------------

title_label = ctk.CTkLabel(
    app, 
    text="Engineering Calculator",
    font=("Arial", 30, "bold")
)

title_label.pack(pady=15)

#--------------------------------
# Main frame 
#--------------------------------

main_frame = ctk.CTkFrame(app)

main_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)

#-------------------------------
# Sidebar
#-------------------------------

sidebar = ctk.CTkFrame(
    main_frame,
    width=260,
    fg_color="#242424"

)

sidebar.pack(
    side="left",
    fill="y"
)

sidebar_title = ctk.CTkLabel(
    sidebar,
    text="Modules",
    font=("Arial", 20, "bold")
)

sidebar_title.pack(pady=(20,30))

basic_button = ctk.CTkButton(
    sidebar,
    text="Basic",
    width=180,
    height=40,
    command=show_basic
)

basic_button.pack(pady=10)

mechanics_button = ctk.CTkButton(
    sidebar,
    text="Mechanics",
    width=180,
    height=40,
    command=show_mechanics
)

mechanics_button.pack(pady=10)

thermo_button = ctk.CTkButton(
    sidebar,
    text="Thermodynamics",
    width=180,
    height=40,
    command=show_thermodynamics
)

thermo_button.pack(pady=10)


fluids_button = ctk.CTkButton(
    sidebar,
    text="Fluids",
    width=180,
    height=40,
    command=show_fluids
)

fluids_button.pack(pady=10)

physics_button = ctk.CTkButton(
    sidebar,
    text="Physics",
    width=180,
    height=40,
    command=show_physics
)

physics_button.pack(pady=10)

converter_button = ctk.CTkButton(
    sidebar,
    text="Converter",
    width=180,
    height=40,
    command=show_converter
)

converter_button.pack(pady=10)

scientific_button = ctk.CTkButton(
    sidebar,
    text="Scientific",
    width=180,
    height=40,
    command=show_scientific
)

scientific_button.pack(pady=10)

material_button = ctk.CTkButton(
    sidebar,
    text="Material Properties",
    width=180,
    height=40,
    command=show_material_properties
)

material_button.pack(pady=10)   

#--------------------------------
# Content Area
#--------------------------------

content = ctk.CTkFrame(
    main_frame,
)

display = ctk.CTkEntry(
    content,
    font=("Arial",32),
    justify="right",
    height=60
)

display.pack(
    fill="x",
    padx=20,
    pady=20
)

display.insert(0, "0")

#--------------------------------
# Calculator Buttons
#--------------------------------

button_frame = ctk.CTkFrame(content)

button_frame.pack(
    padx=20,
    pady=20
)

ac_button = ctk.CTkButton(
    button_frame,
    text="AC",
    width=90,
    height=60
)

ac_button.grid(
    row=0,
    column=0,
    padx=5,
    pady=5
)

bracket_button = ctk.CTkButton(
    button_frame,
    text="()",
    width=90,
    height=60
)

bracket_button.grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)

percent_button = ctk.CTkButton(
    button_frame,
    text="%",
    width=90,
    height=60
)

percent_button.grid(
    row=0,
    column=2,
    padx=5,
    pady=5
)

divide_button = ctk.CTkButton(
    button_frame,
    text="÷",
    width=90,
    height=60
)

divide_button.grid(
    row=0,
    column=3,
    padx=5,
    pady=5
)

buttons = [
    "AC", "()", "%", "÷",
    "7", "8", "9", "×",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "0", ".", "⌫", "="
]

for index, text in enumerate(buttons):

    row = index//4
    column = index % 4

    button = ctk.CTkButton(
        button_frame,
        text=text,
        width=90,
        height=60,
        command=lambda value=text: button_click(value)
    )

    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5
    )


content.pack(
    side="left",
    fill="both",
    expand=True,
    padx=10
)

show_basic()
app.mainloop()