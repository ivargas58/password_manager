from tkinter import*
from tkinter import messagebox
from random import choice, randint, shuffle
#instala una dependencia para esta libreria si estas en vsc pip install pyperclip
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Funcion que ejecuta el boton de generate password 
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)
    
    password_letter = [choice(letters)for _ in range (nr_letters)]
    password_symbols = [choice(symbols)for _ in range (nr_symbols)]
    password_numbers = [choice(numbers)for _ in range (nr_numbers)]
    
    password_list = password_letter + password_symbols + password_numbers
    shuffle(password_list)

    password= "".join(password_list)

    #para hacer prueba
    #print(f'{password}')
    
    #Envia la informacion al input de password
    pass_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
#Funcion que guarda la informacion en el data.txt 
def save():
    #Informacion capturada de los entrys
    website = web_input.get()
    email = user_input.get()
    password = pass_input.get()
    
    #Decicion si uno de los espacion no esta lleno osea len = 0 el numero de valores es 0 envia un messagebox
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Porfavor llenar los espacios en blancos")
    # De lo contrario sigue su curso
    else:
        #Messagebox para que lea la informacion antes de someterla al data.txt
        is_ok= messagebox.askokcancel(title=website, message=f'Confirma tu informacion: \nEmail: {email}\n Password: {password}\n Website: {website}')
        #Si es cierto se somete la informacion
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} |{email} |{password}\n")
                web_input.delete(0,END)
                pass_input.delete(0,END)
        
# ---------------------------- UI SETUP ------------------------------- #
# Window Main
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas (para el logo)
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

# Entries
web_input = Entry(width=35)
web_input.grid(column=1, row=1, columnspan=2, sticky="EW")
web_input.focus()

user_input = Entry(width=35)
user_input.grid(column=1, row=2, columnspan=2, sticky="EW")
user_input.insert(0,"ivan@gmail.com")

pass_input = Entry(width=21)
pass_input.grid(column=1, row=3, sticky="EW")

# Buttons
generate_button = Button(text="Generate Password", command=generate)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

# Window execute
window.mainloop()
