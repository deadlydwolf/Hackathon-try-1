#HACKATHON

from pynput import mouse, keyboard
import time
import tkinter as tk
import mysql.connector as mysql

myconnection=mysql.connect(host="localhost",user="root",passwd="soumya",database="information")
cursor=myconnection.cursor()

#main box
main_box=tk.Tk()
main_box.title("Hackathon sample program")
main_box.geometry("400x300")
text_1=tk.Label(main_box,text="Emergency Response Coordination",font=("coppperplate gothic light",13)).place(x=65,y=10)


text_2=tk.Label(main_box,text="Press the button 3 times to activate",font=("coppperplate gothic light",11)).place(x=80,y=60)

check_button=tk.Button(main_box,text="click here!",command=lambda:clicked).place(x=250,y=85)

button_register=tk.Button(main_box,text="Register yourself",command=lambda:register()).place(x=140,y=130)

def register():
    root = tk.Tk()
    root.title("Enter Data")
    root.geometry("400x300")
    def on_button_click():
        name = name_entry.get()
        age = age_entry.get()
        contact_number = contact_entry.get()
        blood_group = blood_group_entry.get()

        # Insert data into the 'person' table
        query = "INSERT INTO person (name, age, contact_number, blood_group) VALUES (%s, %s, %s, %s)"
        values = (name, age, contact_number, blood_group)
        cursor.execute(query, values)
        myconnection.commit()

    # Create input boxes (entry widgets)
    name_label = tk.Label(root, text="Name:")
    name_label.pack()
    name_entry = tk.Entry(root)
    name_entry.pack()

    age_label = tk.Label(root, text="Age:")
    age_label.pack()
    age_entry = tk.Entry(root)
    age_entry.pack()

    contact_label = tk.Label(root, text="Contact Number:")
    contact_label.pack()
    contact_entry = tk.Entry(root)
    contact_entry.pack()

    blood_group_label = tk.Label(root, text="Blood Group:")
    blood_group_label.pack()
    blood_group_entry = tk.Entry(root)
    blood_group_entry.pack()

    # Create a button widget
    button = tk.Button(root, text="Submit", command=on_button_click)
    button.pack()

#Mouse Click Counter
def clicked(x,y,button,pressed):
    global click_count
    if pressed:
        click_counter_activation

# Define the function to handle mouse clicks
def on_click_activation(x, y, button, pressed):
    global click_count_activation
    if pressed:
        click_count_activation += 1

def click_counter_activation():
    # Define the time frame (in seconds)
    time_frame = 2  # 2 sec

    # Initialize the click counter
    click_count_activation = 0

    # Get the current time
    start_time = time.time()

    # Define the end time based on the time frame
    end_time = start_time + time_frame

    # Start listening to mouse clicks
    with Listener(on_click_activation=on_click_activation) as listener:
        # Keep listening until the end time is reached
        while time.time() < end_time:
            pass
    # Output the number of mouse clicks within the time frame
    print(f"Number of mouse clicks in {time_frame} seconds: {click_count}")
    
    # whether to proceed or not
    if click_count_activation==3:
        three_clicks_activated
    else:
        pass

def on_click_selection(x, y, button, pressed):
    global click_count_selection
    if pressed:
        click_count_selection += 1

def three_clicks_activated():
    # Define the time frame (in seconds)
    time_frame = 2  # 2 sec

    # Initialize the click counter
    click_count_selection = 0

    # Get the current time
    start_time = time.time()

    # Define the end time based on the time frame
    end_time = start_time + time_frame

    # Start listening to mouse clicks
    with Listener(on_click_selection=on_click_selection) as listener:
        # Keep listening until the end time is reached
        while time.time() < end_time:
            pass
    if click_count_selection!=0 and click_count_selection<=3:
        selection
    else:
        pass


def selection():
    if click_count_selection==1:
        Ambulance
    elif click_count_selection==2:
        Police
    elif click_count_selection==3:
        FireDepartment
    else:
        pass



main_box.mainloop()
