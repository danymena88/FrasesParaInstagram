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
        trigger = CronTrigger(year="*", month="*", day_of_week="*", hour="*", minute="56", second="5")
        trigger2 = CronTrigger(year="*", month="*", day="*", hour="*", minute="31", second="15")
        trigger3 = CronTrigger(year="*", month="*", day="*", hour="*", minute="31", second="25")
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
           

        # create frame 1
        self.radiobutton_frame = customtkinter.CTkFrame(self, height=80)
        self.radiobutton_frame.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.title_label = customtkinter.CTkLabel(self.radiobutton_frame, text="Post 1", fg_color="transparent")
        self.title_label.grid(row=1, column=0, columnspan=2, pady=(20,0))
        self.label_post11 = customtkinter.CTkLabel(self.radiobutton_frame, text="Dia: ", fg_color="transparent")
        self.label_post11.grid(row=2, column=0, padx=(20,2), pady=(20,5))
        self.input_post11 = customtkinter.CTkEntry(self.radiobutton_frame)
        self.input_post11.grid(row=2, column=1, padx=(2,20), pady=(30,5))
        self.label_post12 = customtkinter.CTkLabel(self.radiobutton_frame, text="Hora: ", fg_color="transparent")
        self.label_post12.grid(row=3, column=0, padx=(20,2), pady=(10,5))
        self.input_post12 = customtkinter.CTkEntry(self.radiobutton_frame)
        self.input_post12.grid(row=3, column=1, padx=(2,20), pady=(10,5))
        self.label_post13 = customtkinter.CTkLabel(self.radiobutton_frame, text="Hora: ", fg_color="transparent")
        self.label_post13.grid(row=4, column=0, padx=(20,2), pady=(10,5))
        self.input_post13 = customtkinter.CTkEntry(self.radiobutton_frame)
        self.input_post13.grid(row=4, column=1, padx=(2,20), pady=(10,5))
        self.string_input_button = customtkinter.CTkButton(self.radiobutton_frame, text="Guardar", command=self.publicacion)
        self.string_input_button.grid(row=5, column=0, padx=20, pady=(50, 10), columnspan=2)
        self.info_label = customtkinter.CTkLabel(self.radiobutton_frame, text="dia_de_la_semana", fg_color="transparent")
        self.info_label.grid(row=6, column=0, columnspan=2)
        # create frame 2
        self.radiobutton_frame2 = customtkinter.CTkFrame(self, height=80)
        self.radiobutton_frame2.grid(row=0, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.title_labelf2 = customtkinter.CTkLabel(self.radiobutton_frame2, text="Post 1", fg_color="transparent")
        self.title_labelf2.grid(row=1, column=0, columnspan=2, pady=(20,0))
        self.label_post21 = customtkinter.CTkLabel(self.radiobutton_frame2, text="Dia: ", fg_color="transparent")
        self.label_post21.grid(row=2, column=0, padx=(20,2), pady=(20,5))
        self.input_post21 = customtkinter.CTkEntry(self.radiobutton_frame2)
        self.input_post21.grid(row=2, column=1, padx=(2,20), pady=(30,5))
        self.label_post22 = customtkinter.CTkLabel(self.radiobutton_frame2, text="Hora: ", fg_color="transparent")
        self.label_post22.grid(row=3, column=0, padx=(20,2), pady=(10,5))
        self.input_post22 = customtkinter.CTkEntry(self.radiobutton_frame2)
        self.input_post22.grid(row=3, column=1, padx=(2,20), pady=(10,5))
        self.label_post23 = customtkinter.CTkLabel(self.radiobutton_frame2, text="Hora: ", fg_color="transparent")
        self.label_post13.grid(row=4, column=0, padx=(20,2), pady=(10,5))
        self.input_post23 = customtkinter.CTkEntry(self.radiobutton_frame2)
        self.input_post23.grid(row=4, column=1, padx=(2,20), pady=(10,5))
        self.string_input_buttonf2 = customtkinter.CTkButton(self.radiobutton_frame2, text="Guardar", command=self.publicacion)
        self.string_input_buttonf2.grid(row=5, column=0, padx=20, pady=(50, 10), columnspan=2)
        self.info_labelf2 = customtkinter.CTkLabel(self.radiobutton_frame2, text="dia_de_la_semana", fg_color="transparent")
        self.info_labelf2.grid(row=6, column=0, columnspan=2)

        self.frameinfo = customtkinter.CTkFrame(self)
        self.frameinfo.grid(row=1, column=1, rowspan=2, columnspan=3, pady=20, sticky="nsew")
        self.info_labelf4 = customtkinter.CTkLabel(self.frameinfo, text="dia_de_la_semana", fg_color="transparent")
        self.info_labelf4.grid(row=0, column=0)

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





