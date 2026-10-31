import socket
import threading
from customtkinter import *


# HOST = "localhost"
# PORT = 8080
#
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect((HOST, PORT))


win = CTk()
win.geometry("400x350")


menu = CTkFrame(win, width=140)


name_label = CTkLabel(menu, text="Ім'я")
name_label.pack(pady=5)


name_entry = CTkEntry(menu)
name_entry.insert(0, "Учень")
name_entry.pack(padx=10)




def set_theme(val):
  if val == "темна":
      set_appearance_mode("dark")
  else:
      set_appearance_mode("light")




theme_menu = CTkOptionMenu(menu, values=["темна", "світла"], command=set_theme)
theme_menu.pack(side="bottom", pady=10)




def toggle_menu():
  if menu.winfo_ismapped():
      menu.pack_forget()
  else:
      menu.pack(side="left", fill="y")




main_frame = CTkFrame(win, fg_color="transparent")
main_frame.pack(side="right", expand=True, fill="both", padx=5, pady=5)


menu_btn = CTkButton(main_frame, text="☰", width=30, command=toggle_menu)
menu_btn.pack(anchor="w")


chat_box = CTkTextbox(main_frame)
chat_box.pack(expand=True, fill="both", pady=5)




def send_message():
  text = msg_entry.get()
  name = name_entry.get()
  full_text = name + ": " + text

  chat_box.insert("end", "Я: " + text + "\n")
  # sock.sendall(full_text.encode())
  msg_entry.delete(0, "end")

def send_red_message():
  text = msg_entry.get()
  chat_box.insert(index="end", text="[ВАЖЛИВО] Я: " + text + "\n")
  msg_entry.delete(first_index=0, last_index="end")


  #sock.sendall(full_text.encode())
  msg_entry.delete(0, "end")


input_frame = CTkFrame(main_frame, fg_color="transparent")
input_frame.pack(fill="x")


msg_entry = CTkEntry(input_frame, placeholder_text="Повідомлення...")
msg_entry.pack(side="left", expand=True, fill="x", padx=(0, 5))


send_btn = CTkButton(input_frame, text=">", width=40, command=send_message)
send_btn.pack(side="right")

red_btn = CTkButton(input_frame, text="🔥", width=40, fg_color="red", command=send_red_message)
red_btn.pack(side="right", padx=(0, 5))


# def receive():
#    while True:
#        data = sock.recv(1024)
#        chat_box.insert("end", data.decode() + "\n")




# threading.Thread(target=receive, daemon=True).start()
win.mainloop()


