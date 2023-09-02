from process import imagenYfrase
from apscheduler.schedulers.background import BackgroundScheduler
from PIL import Image
from pystray import MenuItem as item
import customtkinter, pickle, os, pystray

with open("theme.pickle", "rb") as file:
            theme = pickle.load(file)
customtkinter.set_appearance_mode(theme)  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
current_path = os.path.dirname(os.path.realpath(__file__))
                        

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.obtenerSwitches()
        self.listaTareas = ["","","","","","","","",""]

        # configure window
        self.title("Frases para Instagram - Codeffee")
        self.geometry(f"{1054}x{640}")
        self.resizable(False, False)

        # configure grid layout
        self.grid_columnconfigure((0, 1, 2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=3, padx=(0,20), sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(1, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Frases\npara Instagram", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.my_image = customtkinter.CTkImage(light_image=Image.open(current_path + "/customtkinter/assets/icons/logo-codeffee.png"), dark_image=Image.open(current_path + "/customtkinter/assets/icons/logo-codeffee.png"), size=(150, 95))
        self.logo_image = customtkinter.CTkButton(self.sidebar_frame, image=self.my_image, fg_color=('transparent'), text="", command=self.creadoPor)
        self.logo_image.grid(row=1, column=0, padx=10, pady=(0, 0))
        textoParaLabel = "Dia: de lunes a Domingo\nLunes = 0 hasta Domingo = 6\nEjemplo: 0-3,5\n'De lunes a jueves más el sábado'\n\nHora: de 0 a 23\nEjemplo: 8,14,17\n'Se publicará a las 8am\n2pm y 5pm'\n\nMinuto: de 0 a 59\nIgual puedes utilizar\nmúltiples valores\n\nEn todos los campos\nse puede utilizar '*'\nque equivale a 'TODOS'\nEjemplo: Dia=*\n'Significa de Lun-Dom'"
        self.label_instrucciones = customtkinter.CTkLabel(self.sidebar_frame, text=textoParaLabel, fg_color="transparent", text_color=("gray50","gray40"))
        self.label_instrucciones.grid(row=2, column=0, padx=10, pady=(0, 50), rowspan=3)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Tema:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
           

        # create frame 1
        self.radiobutton_frame = customtkinter.CTkFrame(self, height=80)
        self.radiobutton_frame.grid(row=0, column=1, padx=(20, 20), pady=(10, 0))
        self.title_label = customtkinter.CTkLabel(self.radiobutton_frame, text="Post 1", fg_color="transparent", text_color="#9e40f6", font=("", 20))
        self.title_label.grid(row=1, column=0, columnspan=2, pady=(20,0))
        self.label_post11 = customtkinter.CTkLabel(self.radiobutton_frame, text="Dia: ", fg_color="transparent")
        self.label_post11.grid(row=2, column=0, padx=(20,2), pady=(10,5))
        self.input_post11 = customtkinter.CTkEntry(self.radiobutton_frame)
        self.input_post11.grid(row=2, column=1, padx=(2,20), pady=(10,5))
        self.label_post12 = customtkinter.CTkLabel(self.radiobutton_frame, text="Hora: ", fg_color="transparent")
        self.label_post12.grid(row=3, column=0, padx=(20,2), pady=(10,5))
        self.input_post12 = customtkinter.CTkEntry(self.radiobutton_frame)
        self.input_post12.grid(row=3, column=1, padx=(2,20), pady=(10,5))
        self.label_post13 = customtkinter.CTkLabel(self.radiobutton_frame, text="Minuto: ", fg_color="transparent")
        self.label_post13.grid(row=4, column=0, padx=(20,2), pady=(10,5))
        self.input_post13 = customtkinter.CTkEntry(self.radiobutton_frame)
        self.input_post13.grid(row=4, column=1, padx=(2,20), pady=(10,5))
        self.switch_var = customtkinter.StringVar(value=self.switch1)
        self.switch = customtkinter.CTkSwitch(self.radiobutton_frame, text="Activar", variable=self.switch_var, onvalue="on", offvalue="off", command=self.cambio1)
        self.switch.grid(row=5, column=0, columnspan=2, pady=(25,0))
        self.info_label = customtkinter.CTkLabel(self.radiobutton_frame, text="Info de la tarea", fg_color="transparent")
        self.info_label.grid(row=6, column=0, columnspan=2, pady=(25,0))

        # create frame 2
        self.radiobutton_frame2 = customtkinter.CTkFrame(self, height=80)
        self.radiobutton_frame2.grid(row=0, column=2, padx=(20, 20), pady=(10, 0))
        self.title_labef2 = customtkinter.CTkLabel(self.radiobutton_frame2, text="Post 2", fg_color="transparent", text_color="#9e40f6", font=("", 20))
        self.title_labef2.grid(row=1, column=0, columnspan=2, pady=(20,0))
        self.label_post21 = customtkinter.CTkLabel(self.radiobutton_frame2, text="Dia: ", fg_color="transparent")
        self.label_post21.grid(row=2, column=0, padx=(20,2), pady=(10,5))
        self.input_post21 = customtkinter.CTkEntry(self.radiobutton_frame2)
        self.input_post21.grid(row=2, column=1, padx=(2,20), pady=(10,5))
        self.label_post22 = customtkinter.CTkLabel(self.radiobutton_frame2, text="Hora: ", fg_color="transparent")
        self.label_post22.grid(row=3, column=0, padx=(20,2), pady=(10,5))
        self.input_post22 = customtkinter.CTkEntry(self.radiobutton_frame2)
        self.input_post22.grid(row=3, column=1, padx=(2,20), pady=(10,5))
        self.label_post23 = customtkinter.CTkLabel(self.radiobutton_frame2, text="Minuto: ", fg_color="transparent")
        self.label_post23.grid(row=4, column=0, padx=(20,2), pady=(10,5))
        self.input_post23 = customtkinter.CTkEntry(self.radiobutton_frame2)
        self.input_post23.grid(row=4, column=1, padx=(2,20), pady=(10,5))
        self.switch_var2 = customtkinter.StringVar(value=self.switch2)
        self.switch2 = customtkinter.CTkSwitch(self.radiobutton_frame2, text="Activar", variable=self.switch_var2, onvalue="on", offvalue="off", command=self.cambio2)
        self.switch2.grid(row=5, column=0, columnspan=2, pady=(25,0))
        self.info_labelf2 = customtkinter.CTkLabel(self.radiobutton_frame2, text="Info de la tarea", fg_color="transparent")
        self.info_labelf2.grid(row=6, column=0, columnspan=2, pady=(25,0))

        # create frame 3
        self.radiobutton_frame3 = customtkinter.CTkFrame(self, height=80)
        self.radiobutton_frame3.grid(row=0, column=3, padx=(20, 20), pady=(10, 0))
        self.title_labef3 = customtkinter.CTkLabel(self.radiobutton_frame3, text="Post 3", fg_color="transparent", text_color="#9e40f6", font=("", 20))
        self.title_labef3.grid(row=1, column=0, columnspan=2, pady=(20,0))
        self.label_post31 = customtkinter.CTkLabel(self.radiobutton_frame3, text="Dia: ", fg_color="transparent")
        self.label_post31.grid(row=2, column=0, padx=(20,2), pady=(10,5))
        self.input_post31 = customtkinter.CTkEntry(self.radiobutton_frame3)
        self.input_post31.grid(row=2, column=1, padx=(2,20), pady=(10,5))
        self.label_post32 = customtkinter.CTkLabel(self.radiobutton_frame3, text="Hora: ", fg_color="transparent")
        self.label_post32.grid(row=3, column=0, padx=(20,2), pady=(10,5))
        self.input_post32 = customtkinter.CTkEntry(self.radiobutton_frame3)
        self.input_post32.grid(row=3, column=1, padx=(2,20), pady=(10,5))
        self.label_post33 = customtkinter.CTkLabel(self.radiobutton_frame3, text="Minuto: ", fg_color="transparent")
        self.label_post33.grid(row=4, column=0, padx=(20,2), pady=(10,5))
        self.input_post33 = customtkinter.CTkEntry(self.radiobutton_frame3)
        self.input_post33.grid(row=4, column=1, padx=(2,20), pady=(10,5))
        self.switch_var3 = customtkinter.StringVar(value=self.switch3)
        self.switch3 = customtkinter.CTkSwitch(self.radiobutton_frame3, text="Activar", variable=self.switch_var3, onvalue="on", offvalue="off", command=self.cambio3)
        self.switch3.grid(row=5, column=0, columnspan=2, pady=(25,0))
        self.info_labelf3 = customtkinter.CTkLabel(self.radiobutton_frame3, text="Info de la tarea", fg_color="transparent")
        self.info_labelf3.grid(row=6, column=0, columnspan=2, pady=(25,0))


        self.frameinfo = customtkinter.CTkFrame(self, corner_radius=15)
        self.frameinfo.grid(row=1, column=1, rowspan=2, columnspan=3, pady=(20,20), sticky="nsew")
        self.string_input_buttonf3 = customtkinter.CTkButton(self.frameinfo, text="Guardar", width=200, command=self.guardar)
        self.string_input_buttonf3.grid(row=0, column=0, padx=300, pady=(20,10), columnspan=3)
        self.info_label42 = customtkinter.CTkLabel(self.frameinfo, font=("",12), fg_color="transparent", width=560, text_color="#9e40f6", justify="center")
        self.info_label42.grid(row=1, column=0, padx=25, pady=(5,15), columnspan=3)
        self.textbox = customtkinter.CTkTextbox(self.frameinfo, height=130, corner_radius=15)
        self.textbox.grid(row=2, column=0, columnspan=3, padx=(7,0), pady=(5,5), sticky="nsew")
        self.textbox_input_buttonf31 = customtkinter.CTkButton(self.frameinfo, text="Guardar Texto", width=200, command=self.guardarTexto)
        self.textbox_input_buttonf31.grid(row=3, column=0, pady=(5,5))
        self.textbox_input_buttonf32 = customtkinter.CTkButton(self.frameinfo, text="Borrar Texto", width=200, command=self.borrarTexto)
        self.textbox_input_buttonf32.grid(row=3, column=1, pady=(5,5))
        self.textbox_input_buttonf33 = customtkinter.CTkButton(self.frameinfo, text="Publicar", width=200, command=self.publicacion)
        self.textbox_input_buttonf33.grid(row=3, column=2, pady=(5,5))

        self.obtenerTareas()
        if self.switch.get() == "off":
             self.cambio1()
        if self.switch2.get() == "off":
             self.cambio2()
        if self.switch3.get() == "off":
             self.cambio3()

        # set default values
        self.appearance_mode_optionemenu.set(theme)



    def obtenerTareas(self):
        try:
             with open("tareas.pickle", "rb") as file:
                  self.listaTareas = pickle.load(file)
        except:
             print("")
          # tareas programadas
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
        texto = ""
        if  self.listaTareas[0] != "" and self.listaTareas[1] != "" and self.listaTareas[2] != "" and self.switch.get()=="on":
              try:
                       self.scheduler.add_job(self.publicacion,'cron', day_of_week=self.listaTareas[0], hour=self.listaTareas[1], minute=self.listaTareas[2], id='Tarea1', name='Tarea1')
                       input1 = customtkinter.StringVar(value=self.listaTareas[0])
                       input2 = customtkinter.StringVar(value=self.listaTareas[1])
                       input3 = customtkinter.StringVar(value=self.listaTareas[2])
                       self.input_post11.configure(textvariable=input1)
                       self.input_post12.configure(textvariable=input2)
                       self.input_post13.configure(textvariable=input3)
                       self.info_label.configure(text_color="#9e40f6")
                       texto = "Dia/s: " + self.listaTareas[0] + ", Hora: " + self.listaTareas[1] + ", Min: " + self.listaTareas[2]
                       if len(texto) > 37:
                            self.info_label.configure(text=texto[0:37])
                       else:
                            self.info_label.configure(text=texto)
              except:
                       self.info_label.configure(text_color="red")
                       self.info_label.configure(text="Error en uno o más campos")
              
        if  self.listaTareas[3] != "" and self.listaTareas[4] != "" and self.listaTareas[5] != "" and self.switch2.get()=="on":
              try:
                   self.scheduler.add_job(self.publicacion,'cron', day_of_week=self.listaTareas[3], hour=self.listaTareas[4], minute=self.listaTareas[5], id='Tarea2', name='Tarea2')
                   input4 = customtkinter.StringVar(value=self.listaTareas[3])
                   input5 = customtkinter.StringVar(value=self.listaTareas[4])
                   input6 = customtkinter.StringVar(value=self.listaTareas[5])
                   self.input_post21.configure(textvariable=input4)
                   self.input_post22.configure(textvariable=input5)
                   self.input_post23.configure(textvariable=input6)
                   self.info_labelf2.configure(text_color="#9e40f6")
                   texto = "Dia/s: " + self.listaTareas[3] + ", Hora: " + self.listaTareas[4] + ", Min: " + self.listaTareas[5]
                   if len(texto) > 37:
                            self.info_labelf2.configure(text=texto[0:37])
                   else:
                            self.info_labelf2.configure(text=texto)
              except:
                       self.info_labelf2.configure(text_color="red")
                       self.info_labelf2.configure(text="Error en uno o más campos")

        if  self.listaTareas[6] != "" and self.listaTareas[7] != "" and self.listaTareas[8] != "" and self.switch3.get()=="on":
              try:
                   self.scheduler.add_job(self.publicacion,'cron', day_of_week=self.listaTareas[6], hour=self.listaTareas[7], minute=self.listaTareas[8], id='Tarea3', name='Tarea3')
                   input7 = customtkinter.StringVar(value=self.listaTareas[6])
                   input8 = customtkinter.StringVar(value=self.listaTareas[7])
                   input9 = customtkinter.StringVar(value=self.listaTareas[8])
                   self.input_post31.configure(textvariable=input7)
                   self.input_post32.configure(textvariable=input8)
                   self.input_post33.configure(textvariable=input9)
                   self.info_labelf3.configure(text_color="#9e40f6")
                   texto = "Dia/s: " + self.listaTareas[6] + ", Hora: " + self.listaTareas[7] + ", Min: " + self.listaTareas[8]
                   if len(texto) > 37:
                            self.info_labelf3.configure(text=texto[0:37])
                   else:
                            self.info_labelf3.configure(text=texto)
              except:
                       self.info_labelf3.configure(text_color="red")
                       self.info_labelf3.configure(text="Error en uno o más campos")
        textoTarea1 = str(self.scheduler.get_job('Tarea1'))
        textoTarea2 = str(self.scheduler.get_job('Tarea2'))
        textoTarea3 = str(self.scheduler.get_job('Tarea3'))
        texto = textoTarea1[0:-37] + "\n" + textoTarea2[0:-37] + "\n" + textoTarea3[0:-37]
        self.info_label42.configure(text=texto)
        self.textbox.delete("0.0","end")
        self.textbox.insert("0.0", self.listaTareas[9][0:-1])
        self.scheduler.print_jobs()

    def obtenerSwitches(self):
         with open("switches.pickle", "rb") as file:
            self.switches = pickle.load(file)
         self.switch1 = self.switches[0]
         self.switch2 = self.switches[1]
         self.switch3 = self.switches[2]
    
    def guardarSwitches(self):
         with open("switches.pickle", "wb") as file:
            pickle.dump(self.switches, file, pickle.HIGHEST_PROTOCOL)
         

    def cambio1(self):
         if self.switch.get() == "on":
              self.input_post11.configure(state="normal")
              self.input_post12.configure(state="normal")
              self.input_post13.configure(state="normal")
              self.radiobutton_frame.configure(fg_color=("gray86","gray17"))
              self.info_label.configure(text="Info de la tarea")
              self.switches[0] = self.switch.get()
              self.guardarSwitches()
              self.obtenerTareas()
                   
         else:
              try:
                   self.scheduler.remove_job("Tarea1")
                   textoTarea1 = str(self.scheduler.get_job('Tarea1'))
                   textoTarea2 = str(self.scheduler.get_job('Tarea2'))
                   textoTarea3 = str(self.scheduler.get_job('Tarea3'))
                   texto = textoTarea1[0:-37] + "\n" + textoTarea2[0:-37] + "\n" + textoTarea3[0:-37]
                   self.info_label42.configure(text=texto)
              except:
                   print("")
              self.info_label.configure(text_color=("gray10", "#DCE4EE"))
              self.info_label.configure(text="Desactivada")
              self.radiobutton_frame.configure(fg_color="transparent")
              input1 = customtkinter.StringVar(value="")
              input2 = customtkinter.StringVar(value="")
              input3 = customtkinter.StringVar(value="")
              self.input_post11.configure(textvariable=input1)
              self.input_post12.configure(textvariable=input2)
              self.input_post13.configure(textvariable=input3)
              self.input_post11.configure(state="disabled")
              self.input_post12.configure(state="disabled")
              self.input_post13.configure(state="disabled")
              self.switches[0] = self.switch.get()
              self.listaTareas[0] = ""
              self.listaTareas[1] = ""
              self.listaTareas[2] = ""
              self.guardarSwitches()


    def cambio2(self):
         if self.switch2.get() == "on":
              self.input_post21.configure(state="normal")
              self.input_post22.configure(state="normal")
              self.input_post23.configure(state="normal")
              self.radiobutton_frame2.configure(fg_color=("gray86","gray17"))
              self.info_labelf2.configure(text="Info de la tarea")
              self.switches[1] = self.switch2.get()
              self.guardarSwitches()
              self.obtenerTareas()
                   
         else:
              try:
                   self.scheduler.remove_job("Tarea2")
                   textoTarea1 = str(self.scheduler.get_job('Tarea1'))
                   textoTarea2 = str(self.scheduler.get_job('Tarea2'))
                   textoTarea3 = str(self.scheduler.get_job('Tarea3'))
                   texto = textoTarea1[0:-37] + "\n" + textoTarea2[0:-37] + "\n" + textoTarea3[0:-37]
                   self.info_label42.configure(text=texto)
              except:
                   print("")
              self.info_labelf2.configure(text_color=("gray10", "#DCE4EE"))
              self.info_labelf2.configure(text="Desactivada")
              self.radiobutton_frame2.configure(fg_color="transparent")
              input1 = customtkinter.StringVar(value="")
              input2 = customtkinter.StringVar(value="")
              input3 = customtkinter.StringVar(value="")
              self.input_post21.configure(textvariable=input1)
              self.input_post22.configure(textvariable=input2)
              self.input_post23.configure(textvariable=input3)
              self.input_post21.configure(state="disabled")
              self.input_post22.configure(state="disabled")
              self.input_post23.configure(state="disabled")
              self.switches[1] = self.switch2.get()
              self.listaTareas[3] = ""
              self.listaTareas[4]= ""
              self.listaTareas[5]= ""
              self.guardarSwitches()


    def cambio3(self):
         if self.switch3.get() == "on":
              self.input_post31.configure(state="normal")
              self.input_post32.configure(state="normal")
              self.input_post33.configure(state="normal")
              self.radiobutton_frame3.configure(fg_color=("gray86","gray17"))
              self.info_labelf3.configure(text="Info de la tarea")
              self.switches[2] = self.switch3.get()
              self.guardarSwitches()
              self.obtenerTareas()
                   
         else:
              try:
                   self.scheduler.remove_job("Tarea3")
                   textoTarea1 = str(self.scheduler.get_job('Tarea1'))
                   textoTarea2 = str(self.scheduler.get_job('Tarea2'))
                   textoTarea3 = str(self.scheduler.get_job('Tarea3'))
                   texto = textoTarea1[0:-37] + "\n" + textoTarea2[0:-37] + "\n" + textoTarea3[0:-37]
                   self.info_label42.configure(text=texto)
              except:
                   print("")
              self.info_labelf3.configure(text_color=("gray10", "#DCE4EE"))
              self.info_labelf3.configure(text="Desactivada")
              self.radiobutton_frame3.configure(fg_color="transparent")
              input1 = customtkinter.StringVar(value="")
              input2 = customtkinter.StringVar(value="")
              input3 = customtkinter.StringVar(value="")
              self.input_post31.configure(textvariable=input1)
              self.input_post32.configure(textvariable=input2)
              self.input_post33.configure(textvariable=input3)
              self.input_post31.configure(state="disabled")
              self.input_post32.configure(state="disabled")
              self.input_post33.configure(state="disabled")
              self.switches[2] = self.switch3.get()
              self.listaTareas[6]= ""
              self.listaTareas[7]= ""
              self.listaTareas[8]= ""
              self.guardarSwitches()
        

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
        with open("theme.pickle", "wb") as file:
            pickle.dump(new_appearance_mode, file, pickle.HIGHEST_PROTOCOL)

    def publicacion(self):
        imagen1 = imagenYfrase("plantilla.png")
        imagen1.imagen(imagen1.texto(imagen1.obtenerFrase()))
        imagen1.uploadPhoto(self.textbox.get("0.0","end"))

    def guardar(self):          
        if self.switch.get() == "on":
             self.guardar1()
        if self.switch2.get() == "on":
             self.guardar2()
        if self.switch3.get() == "on":
             self.guardar3()
        with open("tareas.pickle", "wb") as file:
            pickle.dump(self.listaTareas, file, pickle.HIGHEST_PROTOCOL)
        self.obtenerTareas()
    
    def guardar1(self):
        try:
             self.scheduler.remove_job("Tarea1")
        except:
             print("")
        input1 = self.input_post11.get()
        input2 = self.input_post12.get()
        input3 = self.input_post13.get()
        if input1 != "" and input2 != "" and input3 != "":                
                  self.listaTareas[0] = input1
                  self.listaTareas[1] = input2
                  self.listaTareas[2] = input3                         
        else:
             self.info_label.configure(text_color="red")
             self.info_label.configure(text="Campo vacio...")
             self.listaTareas[0] = ""
             self.listaTareas[1] = ""
             self.listaTareas[2] = ""
             
        
    def guardar2(self):
        try:
             self.scheduler.remove_job("Tarea2")
        except:
             print("")
        input1 = self.input_post21.get()
        input2 = self.input_post22.get()
        input3 = self.input_post23.get()
        if input1 != "" and input2 != "" and input3 != "":                
                  self.listaTareas[3] = input1
                  self.listaTareas[4] = input2
                  self.listaTareas[5] = input3
                                          
        else:
             self.info_labelf2.configure(text_color="red")
             self.info_labelf2.configure(text="Campo vacio...")
             self.listaTareas[3] = ""
             self.listaTareas[4] = ""
             self.listaTareas[5] = ""
             
        

    def guardar3(self):
        try:
             self.scheduler.remove_job("Tarea3")
        except:
             print("")
        input1 = self.input_post31.get()
        input2 = self.input_post32.get()
        input3 = self.input_post33.get()
        if input1 != "" and input2 != "" and input3 != "":                
                  self.listaTareas[6] = input1
                  self.listaTareas[7] = input2
                  self.listaTareas[8] = input3
                       
        else:
             self.info_labelf3.configure(text_color="red")
             self.info_labelf3.configure(text="Campo vacio...")
             self.listaTareas[6] = ""
             self.listaTareas[7] = ""
             self.listaTareas[8] = ""


    def guardarTexto(self):
          self.listaTareas[9] = self.textbox.get("0.0","end")
          with open("tareas.pickle", "wb") as file:
            pickle.dump(self.listaTareas, file, pickle.HIGHEST_PROTOCOL)

    def borrarTexto(self):
          self.textbox.delete("0.0","end")
          

    def creadoPor(self):
          import webbrowser
          webbrowser.open("https://github.com/danymena88/FrasesParaInstagram")
             
    
    # Define a function for quit the window


def quit_window(icon, item):
     icon.stop()
     app.destroy()

     # Define a function to show the window again


def show_window(icon, item):
     icon.stop()
     app.deiconify()

     # Hide the window and show on the system taskbar


def hide_window():
     app.withdraw()
     image = Image.open(
          current_path + "/customtkinter/assets/icons/Daco_4979581.png")
     menu = (item('Restaurar', show_window), item('Finalizar', quit_window))
     icon = pystray.Icon("name", image, "Frases para Instagram", menu)
     icon.run()



         
if __name__ == "__main__":
    app = App()
    app.protocol('WM_DELETE_WINDOW', hide_window)
    app.mainloop()





