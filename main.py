from tkinter import Tk, Label, Entry, Button, messagebox
import smtplib
from email.message import EmailMessage
import random
import OTP_verification as OTP
from PIL import ImageTk, Image
from db_connection import connect, disconnect
import encrypt_decrypt
import create_account as cl

# Connect to the database
conn = connect()
cursor = conn.cursor()
otp = ""
entries = []
data = []


def clear_window():
    # Remove all widgets from the window
    for widget in tools:
        widget.destroy()
    tools.clear()


def enter_data(e):
    for i in entries:
        data.append(i.get())
    cl.create_account(data, entries)


def create_account(e):
    clear_window()
    image5 = Image.open("images/form.png")
    photo5 = ImageTk.PhotoImage(image5)
    image_label5 = Label(window, image=photo5, bg="#ffffff", borderwidth=0)
    image_label5.place(y=90, x=120)
    image_label5.image = photo5

    image6 = Image.open("images/create.png")
    photo6 = ImageTk.PhotoImage(image6)
    image_label6 = Label(window, image=photo6, bg="#ffffff", borderwidth=0, cursor="hand2")
    image_label6.image = photo6
    image_label6.bind("<Button-1>", enter_data)
    image_label6.place(x=190, y=670)

    pos = [105, 190, 263, 340, 410, 480, 550, 615]
    for i in range(8):
        entries.append(Entry(window, bg="white", font=("Arial", 16), highlightthickness=0, borderwidth=0,
                             foreground="#1e56df"))
        entries[i].place(x=150, y=pos[i])

    # messagebox.showinfo("Success", "Account created successfully!")


def send_otp():
    global otp
    # Generate a random one-time password
    otp = str(random.randint(100000, 999999))

    # Retrieve the entered username and password
    username = username_entry.get()
    password = password_entry.get()

    # Send the OTP via email
    msg = EmailMessage()
    msg.set_content(f"Your one-time password for CYBERSAFE online banking is: {otp}")
    msg["Subject"] = "CYBERSAFE ONLINE BANKING OTP"
    msg["From"] = "uchizistarrgausi@gmail.com"  # Replace with your email address
    msg["To"] = username

    # Configure your email server details and send the message
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "uchizistarrgausi@gmail.com"  # Replace with your Gmail email address
    smtp_password = "vzwcqwkqzvnpsfjj"  # Replace with your Gmail password

    # Create a secure connection to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)

    return otp


def login(e):
    # Retrieve the entered username and password
    username = username_entry.get()
    password = password_entry.get()

    hashed_password = encrypt_decrypt.password_hash(password)
    # Check if the provided credentials are valid
    if authenticate(username, password):

        global otp
        otp = send_otp()  # Send OTP via email
        messagebox.showinfo("Success", "Check your email for an OTP")
        clear_window()
        add_otp_window()
        # Here, you can add code to navigate to the next page for OTP verification
        # OTP.verify_otp_action(window, otp)
    else:
        messagebox.showerror("Error", "Invalid username or password.")
        # clear_window()
        # welcome_window()


def welcome_window():
    image5 = Image.open("images/log1.png")
    photo5 = ImageTk.PhotoImage(image5)
    image_label5 = Label(window, image=photo5, bg="#ffffff", borderwidth=0)
    image_label5.place(y=90, x=45)
    image_label5.image = photo5

    password_label = Label(window, text="Temp", bg="#ffffff", fg="green", font=("Arial", 12))
    password_label.place(x=150, y=420)


def verify_otp(event):
    obj = tools[1]
    print(obj)
    if otp == obj.get():
        clear_window()
        welcome_window()


def add_otp_window():
    image5 = Image.open("images/otp1.png")
    photo5 = ImageTk.PhotoImage(image5)
    image_label5 = Label(window, image=photo5, bg="#ffffff", borderwidth=0)
    image_label5.place(y=90, x=45)
    image_label5.image = photo5

    username_entry1 = Entry(window, bg="white", font=("Arial", 16), highlightthickness=0, borderwidth=0,
                            foreground="#1e56df")

    image6 = Image.open("images/confirm.png")
    photo6 = ImageTk.PhotoImage(image6)
    image_label6 = Label(window, image=photo6, bg="#ffffff", borderwidth=0, cursor="hand2")
    image_label6.image = photo6
    image_label6.bind("<Button-1>", verify_otp)
    image_label6.place(x=190, y=500)

    username_entry1.place(x=170, y=408)

    tools.extend([image_label5, username_entry1, image_label6])


def authenticate(username, password):
    password = encrypt_decrypt.password_hash(password)
    sql = "SELECT email, password FROM customers WHERE email = %s AND password = %s;"

    try:
        cursor.execute(sql, (username, password))
        result = cursor.fetchone()

        print("Query Result:", result)  # Add this line to see the query result in the console

        valid_username = None
        valid_password = None

        if result:
            valid_username = result[0]
            valid_password = result[1]

        return username == valid_username and password == valid_password

    except Exception as e:
        # Print the error message to the console or log the error for debugging.
        print("An error occurred while executing the SQL query:", e)
        return False





# Create the main window
window = Tk()
window.title("CyberSafe online baking Login")
window.geometry("600x780")
window.overrideredirect(True)
window.configure(background="#ffffff")


def move_window(e):
    window.geometry(f'+{e.x_root}+{e.y_root}')


# Load the image
image = Image.open("images/navbar.png")
image = image.resize((1200, 80))
photo = ImageTk.PhotoImage(image)
image_label = Label(window, image=photo, bg="#FCF8FF")
image_label.image = photo  # Save a reference to the image to prevent garbage collection
image_label.bind("<B1-Motion>", move_window)


def close(e):
    window.destroy()


image2 = Image.open("images/close.png")
photo2 = ImageTk.PhotoImage(image2)
image_label2 = Label(window, image=photo2, bg="#1e56df", borderwidth=0, cursor="hand2")
image_label2.place(y=10, x=530)
image_label2.image = photo2
image_label2.bind("<Button-1>", close)

image3 = Image.open("images/container1.png")
photo3 = ImageTk.PhotoImage(image3)
image_label3 = Label(window, image=photo3, bg="#ffffff", borderwidth=0)
image_label3.place(y=90, x=45)
image_label3.image = photo3

image4 = Image.open("images/sign.png")
photo4 = ImageTk.PhotoImage(image4)
image_label4 = Label(window, image=photo4, bg="#ffffff", borderwidth=0, cursor="hand2")
image_label4.image = photo4
image_label4.bind("<Button-1>", login)

# Create labels for logo
logo_label = Label(window, text="CyberSafe.", bg="#1e56df", fg="#ffffff", font=("Arial", 24))
logo2_label = Label(window, text="FOUNDATION", bg="#1e56df", fg="#ffffff", font=("Arial", 12))

# Create labels for username and password
username_label = Label(window, text="Email", fg="#1e56df", bg="white", font=("Arial", 14))
password_label = Label(window, text="Password", fg="#1e56df",  bg="white", font=("Arial", 14))

# Create entry fields for username and password
username_entry = Entry(window, bg="white", font=("Arial", 16), highlightthickness=0, borderwidth=0,
                       foreground="#1e56df")
password_entry = Entry(window, show="*", bg="white", font=("Arial", 16), highlightthickness=0, borderwidth=0,
                       foreground="#1e56df")

create_account_button = Label(window, cursor="hand2", text="Need an account? SIGN UP", bg="#ffffff", fg="#00aa47",
                              font=("Arial", 12, "bold"))

create_account_button.bind("<Button-1>", create_account)

# Set the layout using the grid manager
image_label.place(x=-5, y=-10)
logo_label.place(x=5, y=5)
logo2_label.place(x=40, y=40)
username_label.place(x=140, y=270)
username_entry.place(x=170, y=320)
password_label.place(x=140, y=370)
password_entry.place(x=170, y=423)
image_label4.place(x=190, y=500)
create_account_button.place(x=190, y=580)

tools = []
tools.extend([image_label4, image_label3, username_entry, password_entry, create_account_button])
print(tools)
# Start the GUI event loop
window.mainloop()
