from controllers.MainController import MainController
import customtkinter as form
form.set_appearance_mode("dark")
form.set_default_color_theme("green")

hubform = form.CTk()
hubform.title("Hub")
hubform.geometry("600x400")

buttonweather = form.CTkButton(hubform, text="Узнать температуру", command=MainController.weather)
buttonweather.pack(pady=10)

hubform.mainloop()