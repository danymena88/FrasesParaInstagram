from PIL import Image, ImageDraw, ImageFont
import requests, json


""" class publicacion(object):
  def __init__(self, model, color, company, speed_limit):
    self.color = color
    self.company = company
    self.speed_limit = speed_limit
    self.model = model

  def start(self):
    print("started")

  def stop(self):
    print("stopped")

  def accelarate(self):
    print("accelarating...")
    "accelarator functionality here"

  def change_gear(self, gear_type):
    print("gear changed")
    " gear related functionality here"





def publicar():
            with open("data.pickle", "rb") as f:
                data = pickle.load(f)
            while True:
                with open("semana.pickle", "rb") as f:
                    lista = pickle.load(f)
                numero = random.randrange(0, len(data) + 1, 1)
                if numero in lista:
                    self.label4.configure(
                        text="La frase ya ha sido usada... escogiendo otra"
                    )
                else:
                    lista.append(numero)
                    self.label4.configure(
                        text="Frases ya publicadas: %s" % (str(lista))
                    )
                    with open("semana.pickle", "wb") as f:
                        pickle.dump(lista, f, pickle.HIGHEST_PROTOCOL)
                    break
            with open("key.pickle", "rb") as f:
                access_token = pickle.load(f)
            ig_user_id = "17841455189847505"
            image_url = data[numero][1]
            numeroDeFrase = random.randrange(1, 102, 1)
            frase = requests.get(
                "https://api-generator.retool.com/zMQmrc/frases/%s" % (numeroDeFrase)
            )
            frase = frase.json()
            caption = (
                frase["frase"]
                + "\nHaz tus pedidos por DM 🛒🔥\nMás estilos en nuestra tienda online\n.\n.\nContamos con envío a domicilio a todo El Salvador 🇸🇻\n📩Pedidos por DM\n🛒 o en nuestra tienda online (link en BIO)\n#elsalvador #crazysocks #tiendaenlinea #watushop #sivar #mysocks #mystyle"
            )
            post_url = "https://graph.facebook.com/v17.0/%s/media" % (ig_user_id)
            param = dict()
            param["access_token"] = access_token
            param["caption"] = caption
            param["image_url"] = image_url
            response = requests.post(post_url, params=param)
            response = response.json()

            if "id" in response:
                creation_id = response["id"]
                second_url = "https://graph.facebook.com/v17.0/%s/media_publish" % (
                    ig_user_id
                )
                second_param = dict()
                second_param = {
                    "access_token": access_token,
                    "creation_id": creation_id,
                }
                response = requests.post(second_url, params=second_param)
                response = response.json()
                t = time.localtime()
                current_time = time.strftime("%H:%M:%S", t)
                self.label4.configure(text="Imagen publicada! %s" % (str(current_time)))
            else:
                t = time.localtime()
                current_time = time.strftime("%H:%M:%S", t)
                self.label4.configure(
                    text="Error: No fue posible publicar %s" % (str(current_time))
                )

"""
class imagenYfrase(object):
  def __init__(self, imagen1):
    self.imagen1 = imagen1

  def imagen(self, text):
     W, H = (800,800)
     texto = text
     # get an image
     with Image.open(self.imagen1).convert("RGBA") as base:
        # make a blank image for the text, initialized to transparent text color
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

        # get a font
        fnt = ImageFont.truetype("BebasNeue-Regular.otf", 35)
        # get a drawing context
        d = ImageDraw.Draw(txt)

        # draw text, full opacity
        w, h = d.textsize(texto)
        d.text(((W-w*2)/2,(H-h)/2), texto, font=fnt, fill=(255, 255, 255, 255))

        out = Image.alpha_composite(base, txt)
        out.show()


  def texto(self, text):
     if len(text) > 52:
        for i in range(52, 0, -1):
           if text[i] == " ":
                 if (53 - len(text[0:i])) > 1:
                     n = (53 - int(len(text[0:i])))
                     resultado = (int(n * 0.8) * " ") + text[0:i] + "\n"
                     text = text[i+1:len(text)]
                     break
        return resultado + self.texto(text)
     else:
        if (52 - len(text)) > 1:
                 n = int(52 - len(text))
                 text = (int(n*0.8) * " ") + text
                 return text
           
              
        
     
    

 




