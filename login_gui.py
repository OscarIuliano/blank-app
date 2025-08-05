import tkinter as tk
from tkinter import messagebox
from auth import crea_tabella_utenti, registra, login

# Crea DB se non esiste
crea_tabella_utenti()

def apri_chat(username):
    finestra_login.destroy()
    finestra_chat = tk.Tk()
    finestra_chat.title("Chat - Benvenuto " + username)
    finestra_chat.geometry("400x300")
    tk.Label(finestra_chat, text=f"Sei loggato come {username}", font=("Helvetica", 14)).pack(pady=20)
    tk.Label(finestra_chat, text="(Qui andrà l'interfaccia della chat)", fg="gray").pack()
    finestra_chat.mainloop()

def effettua_login():
    username = entry_user.get()
    password = entry_pass.get()
    if login(username, password):
        apri_chat(username)
    else:
        messagebox.showerror("Errore", "Credenziali errate.")

def effettua_registrazione():
    username = entry_user.get()
    password = entry_pass.get()
    if registra(username, password):
        messagebox.showinfo("Registrazione", "Utente registrato con successo!")
    else:
        messagebox.showwarning("Errore", "Utente già esistente.")

# === UI ===
finestra_login = tk.Tk()
finestra_login.title("Login - Messaggistica")
finestra_login.geometry("300x200")

tk.Label(finestra_login, text="Username").pack(pady=5)
entry_user = tk.Entry(finestra_login)
entry_user.pack()

tk.Label(finestra_login, text="Password").pack(pady=5)
entry_pass = tk.Entry(finestra_login, show="*")
entry_pass.pack()

tk.Button(finestra_login, text="Login", command=effettua_login).pack(pady=10)
tk.Button(finestra_login, text="Registrati", command=effettua_registrazione).pack()

finestra_login.mainloop()
