from tkinter import Tk, Label, Entry, Button, messagebox
import random

def verify_otp_action (window, otp):
    otp_label = Label(window, text="Enter OTP:", bg="#1e3d59", fg="white", font=("Arial", 12))
    otp_entry = Entry(window, bg="#dbe2ef", font=("Arial", 12))
    verify_button = Button(window, text="Verify OTP", bg="#fca311", fg="white", font=("Arial", 12), command= lambda:verification(otp_entry.get(), otp))

    # Set the layout using the grid manager
    otp_label.grid(row=0, column=0, padx=10, pady=10)
    otp_entry.grid(row=0, column=1, padx=10)
    verify_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


    
def verification(entered_otp, otp):
    print(otp)
    print(entered_otp)


    if entered_otp == otp:
        messagebox.showinfo("Success", "OTP verification successful!")
    else:
        messagebox.showerror("Error", "Invalid OTP.")


