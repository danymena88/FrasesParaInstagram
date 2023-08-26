from process import imagenYfrase
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # tareas programadas
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
        trigger = CronTrigger(year="*", month="*", day="*", hour="*", minute="42", second="5")
        trigger2 = CronTrigger(year="*", month="*", day="*", hour="*", minute="54", second="5")
        trigger3 = CronTrigger(year="*", month="*", day="*", hour="*", minute="54", second="5")
        self.scheduler.add_job(self.publicacion,trigger=trigger,args=[],name="Tarea1",)
        self.scheduler.add_job(self.publicacion,trigger=trigger2,args=[],name="Tarea2",)
        self.scheduler.add_job(self.publicacion,trigger=trigger3,args=[],name="Tarea3",)

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{875}x{580}")
        self.resizable(False, False)

        # configure grid layout
        self.grid_columnconfigure((0, 1, 2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=3, padx=(0,20), sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(3, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
           

        # create radiobutton frame
        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radiobutton_frame2 = customtkinter.CTkFrame(self)
        self.radiobutton_frame2.grid(row=0, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radiobutton_frame3 = customtkinter.CTkFrame(self)
        self.radiobutton_frame3.grid(row=0, column=3, padx=(20, 40), pady=(20, 0), sticky="nsew")
        self.string_input_button = customtkinter.CTkButton(self.radiobutton_frame, text="Open CTkInputDialog", command=self.publicacion)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.string_input_button2 = customtkinter.CTkButton(self.radiobutton_frame2, text="Open CTkInputDialog", command=self.publicacion)
        self.string_input_button2.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.string_input_button3 = customtkinter.CTkButton(self.radiobutton_frame3, text="Open CTkInputDialog", command=self.publicacion)
        self.string_input_button3.grid(row=2, column=0, padx=20, pady=(10, 10))

        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def publicacion(self):
        imagen1 = imagenYfrase("_DSC9615.png")
        imagen1.imagen(imagen1.texto(imagen1.obtenerFrase()))



if __name__ == "__main__":
    app = App()
    app.mainloop()





