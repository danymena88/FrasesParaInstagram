from PIL import Image, ImageDraw, ImageFont
import random, json, imgbbpy

try:
      with open('apis.json', encoding='utf-8') as openfile:
                # Reading from json file
                apis = json.load(openfile)
except:
      print("Error: Falta el archivo apis.json")
access_tokenImgbb = apis[2]


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
        out2.save("foto/frase.jpg")


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
      try:
           with open('frases.json', encoding='utf-8') as openfile:
                # Reading from json file
                frase = json.load(openfile)
                numero = random.randrange(0, len(frase), 1)
                return frase[numero]
      except:
           print("Error: falta el archivo frases.json")
           return ""
  

  def uploadPhoto(self):
                 client = imgbbpy.SyncClient(access_tokenImgbb)
                 image = client.upload(file='foto/frase.jpg', expiration= 180)
                 print(image.url)
                 return image.url
      
        
           
              
        
     
    








