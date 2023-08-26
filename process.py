from PIL import Image, ImageDraw, ImageFont
import random, requests, json


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

     # get an image
     with Image.open(self.imagen1).convert("RGBA") as base:
        # make a blank image for the text, initialized to transparent text color
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

        # get a font
        fnt = ImageFont.truetype("BebasNeue-Regular.otf", 35)
        # get a drawing context
        d = ImageDraw.Draw(txt)
        if len(text) < 116:
         w, h = d.textsize(text)
         FW = (W-w*2)/1.8
         FH = (H-h)/2.1
        elif len(text) > 115:
           w, h = d.textsize(text)
           FW = (W-w*2)/1.8
           FH = (H-h)/2.3
        elif len(text) > 300:
           w, h = d.textsize(text)
           FW = (W-w*2)/1.8
           FH = (H-h)/2.4

        # draw text, full opacity
        w, h = d.textsize(text)
        d.text((FW,FH), text, font=fnt, fill=(255, 255, 255, 255))

        out = Image.alpha_composite(base, txt)
        
        out2 = out.convert('RGB')
        out2.save("frase.jpg")
        #out.save("img1.png","PNG")


  def texto(self, text):
     if len(text) > 53:
        for i in range(53, 0, -1):
           if text[i] == " ":
                 if (53 - len(text[0:i])) > 1:
                     n = (53 - int(len(text[0:i])))
                     resultado = ((int(n * 0.5)) * " ") + text[0:i] + "\n"
                     text = text[i+1:len(text)]
                     break
                 elif (53 - len(text[0:i])) > 3:
                     print(2)
                     n = (53 - int(len(text[0:i])))
                     resultado = ((int(n * 1.5)) * " ") + text[0:i] + "\n"
                     text = text[i+1:len(text)]
                     break
                 else:
                     n = (53 - int(len(text[0:i])))
                     resultado = text[0:i] + "\n "
                     text = text[i+1:len(text)]
                     break                     
        return resultado + self.texto(text)
     else:
        if (52 - len(text)) < 7:
                 n = int(53 - len(text))
                 text = ((int(n * 1)) * " ") + text
                 return text
        elif (52 - len(text)) > 6:
                 n = int(53 - len(text))
                 text = ((int(n * 1)) * " ") + text
                 return text
        
  def obtenerFrase(self):
      with open('frases.json', encoding='utf-8') as openfile:
                # Reading from json file
                frase = json.load(openfile)
      numero = random.randrange(0, len(frase), 1)
      return frase[numero]
      
        
           
              
        
     
    

 




