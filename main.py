import tkinter as tk
from tkinter import messagebox, font


# DATA (stations, zones,rates)

ZONES = {
    "Aljada": 1,
    "Muweilah": 1,
    "AL mamsha": 2,
    "City center": 2,
    "Al majaz": 3
}

BASE_FARE = 2.0
EXTRA_ZONE_COST = 1.5


# calculating 

def calculate_fare(start_station, end_station):
    zones_crossed = abs(ZONES[start_station] - ZONES[end_station]) + 1
    if zones_crossed == 1:
        return BASE_FARE
    return BASE_FARE + (zones_crossed - 1) * EXTRA_ZONE_COST


root = tk.Tk()
root.title("CTA - Price calculator")
root.geometry("400x500")  
root.configure(bg="#f0f4f7") 


# Variables 
start_var = tk.StringVar()
end_var = tk.StringVar()


# Calculate and display function 

def calculate():
    start_station = start_var.get()
    end_station = end_var.get()
    if start_station == "" or end_station == "":
        messagebox.showerror("Error", "Please select both stations")
        return
    fare = calculate_fare(start_station, end_station)
    result_label.config(text=f"Distance rate  {start_station} → {end_station} :AED {fare:.2f} ")


# FONTS 

title_font = font.Font(family="Helvetica", size=18, weight="bold")
label_font = font.Font(family="Arial", size=12)
button_font = font.Font(family="Arial", size=12, weight="bold")
result_font = font.Font(family="Arial", size=14, weight="bold")


# INTERFACE

title_label = tk.Label(root, text="CTA rate calculator", font=title_font, bg="#f0f4f7", fg="#007acc")
title_label.pack(pady=30)

menu_frame = tk.Frame(root, bg="#f0f4f7")
menu_frame.pack(pady=20)

# Departure station 
start_label = tk.Label(menu_frame, text="Departure station  :", font=label_font, bg="#f0f4f7")
start_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
start_menu = tk.OptionMenu(menu_frame, start_var, *list(ZONES.keys()))
start_menu.config(width=20, font=label_font, bg="white", fg="black")
start_menu.grid(row=0, column=1, padx=10, pady=10)

# Arrival station 

end_label = tk.Label(menu_frame, text="Arrival station :", font=label_font, bg="#f0f4f7")
end_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
end_menu = tk.OptionMenu(menu_frame, end_var, *list(ZONES.keys()))
end_menu.config(width=20, font=label_font, bg="white", fg="black")
end_menu.grid(row=1, column=1, padx=10, pady=10)

# calculate buton 
calc_button = tk.Button(root, text="calculate", font=button_font, bg="#007acc", fg="white", width=25, height=2, command=calculate)
calc_button.pack(pady=25)

result_label = tk.Label(root, text="", font=result_font, fg="#007acc", bg="#f0f4f7")
result_label.pack(pady=20)

# Test
def run_tests():
    try:
        assert calculate_fare("Aljada", "Muweilah") == 3.0
        assert calculate_fare("Aljada", "AL mamsha") == 5.0
        assert calculate_fare("Aljada", "Al majaz") == 15.0
        assert calculate_fare("City center", "Al majaz") == 7.5
        print("PASSED ✅")
    except AssertionError:
        print("FAILED ❌")

run_tests()
root.mainloop()
