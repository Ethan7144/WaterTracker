import tkinter as tk
import time
import threading

def show_popup():
    def close_popup():
        popup.destroy()

    popup = tk.Tk()
    popup.title("Hydration Reminder")
    popup.geometry("300x150")
    popup.resizable(False, False)

    label = tk.Label(popup, text="Time to drink water! 💧", font=("Arial", 14))
    label.pack(pady=20)

    button = tk.Button(popup, text="I drank my water!", command=close_popup, font=("Arial", 12), bg="#4CAF50", fg="white")
    button.pack(pady=10)

    popup.mainloop()

def reminder_loop():
    while True:
        show_popup()
        time.sleep(15 * 60)  # Wait 15 minutes after closing

if __name__ == "__main__":
    thread = threading.Thread(target=reminder_loop, daemon=True)
    thread.start()
    print("Hydration reminder running in background. Press Ctrl+C to stop.")

    while True:
        time.sleep(1)
