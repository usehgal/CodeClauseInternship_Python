import tkinter as tk
import time
import winsound

alarms = []

def alarm():
    current_time = time.strftime("%H:%M:%S")

    for alarm_time in alarms:
        if current_time == alarm_time:
            alarm_window = tk.Toplevel(root)
            alarm_window.title("Alarm")
            alarm_window.geometry("250x150")
            alarm_window.config(bg="#ffd700")  # Set background color to gold

            def stop_alarm():
                alarm_window.destroy()

            def snooze_alarm():
                alarm_window.destroy()
                snooze_time = time.time() + 300  # 300 seconds = 5 minutes
                alarms.append(time.strftime("%H:%M:%S", time.localtime(snooze_time)))
                set_alarm_button.config(state=tk.NORMAL)  # Re-enable the "Set Alarm" button after snooze
                winsound.Beep(frequency, duration)  # Play a snooze notification sound

            stop_button = tk.Button(alarm_window, text="Stop", command=stop_alarm, font=("Helvetica", 12), bg="#ff6347")  # Set background color to tomato
            stop_button.pack(pady=10)

            snooze_button = tk.Button(alarm_window, text="Snooze (5 mins)", command=snooze_alarm, font=("Helvetica", 12), bg="#87ceeb")  # Set background color to sky blue
            snooze_button.pack(pady=5)

            set_alarm_button.config(state=tk.DISABLED)  # Disable the "Set Alarm" button when alarm rings

            # Play alarm sound
            frequency = 2500  # Set frequency to 2500 Hz
            duration = 2000  # Set duration to 2000 milliseconds (2 seconds)
            winsound.Beep(frequency, duration)

    root.after(1000, alarm)  # Check every 1 second for alarms

def add_alarm():
    alarm_time = alarm_entry.get()
    alarms.append(alarm_time)
    alarm_listbox.insert(tk.END, alarm_time)
    alarm_entry.delete(0, tk.END)

def delete_alarm():
    selected_index = alarm_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        alarms.pop(index)
        alarm_listbox.delete(index)

root = tk.Tk()
root.title("Alarm Clock")
root.geometry("400x400")
root.config(bg="#dcdcdc")  # Set background color to light grey

alarm_label = tk.Label(root, text="Python Alarm Clock", font=("Helvetica", 20), bg="#dcdcdc")  # Set background color to light grey
alarm_label.pack(pady=10)

enter_time_label = tk.Label(root, text="Enter alarm time (HH:MM:SS)", font=("Helvetica", 12), bg="#dcdcdc")  # Set background color to light grey
enter_time_label.pack()

alarm_entry = tk.Entry(root, font=("Helvetica", 16), bg="#ffffff")  # Set background color to white
alarm_entry.pack(pady=10)

add_alarm_button = tk.Button(root, text="Add Alarm", command=add_alarm, font=("Helvetica", 12), bg="#90ee90")  # Set background color to light green
add_alarm_button.pack(pady=5)

delete_alarm_button = tk.Button(root, text="Delete Alarm", command=delete_alarm, font=("Helvetica", 12), bg="#ff6347")  # Set background color to tomato
delete_alarm_button.pack(pady=5)

alarm_listbox = tk.Listbox(root, font=("Helvetica", 12), selectbackground="#87ceeb")  # Set background color of selected item to sky blue
alarm_listbox.pack(pady=10)

set_alarm_button = tk.Button(root, text="Start Alarms", command=alarm, font=("Helvetica", 12), bg="#ffa500")  # Set background color to orange
set_alarm_button.pack(pady=10)

root.mainloop()
