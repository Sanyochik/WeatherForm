import customtkinter as ctk


def weatherForm(weatherAPI):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    def clickFunction():
        city = weatherAPI.getWeather(entry.get())
        label_result.configure(text=f"Текущая погода в городе: {city}!")

    root = ctk.CTk()
    root.title("Погода")
    root.geometry("600x400")

    entry = ctk.CTkEntry(root, placeholder_text="Введите город")
    entry.pack(pady=20)

    button = ctk.CTkButton(root, text="Отправить", command=clickFunction)
    button.pack(pady=10)

    label_result = ctk.CTkLabel(root, text="")
    label_result.pack(pady=10)

    root.mainloop()