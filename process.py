from PIL import Image, ImageDraw, ImageFont
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow
import random, json, requests, httplib2, os, time

ig_user_id = 17841460287206000
access_token2 = "EAAJqZAFveq7YBO0CWewsilzEldEVUN75O7pcDSPIZBK7R8yuwtihWZBzYEm6QA78n45UXFqsmUyZBPeymzPQEZA0ZA9T78cKGx90jDZClZBespSvRlCnAWAe45E7cNOmZCYXTMzDvuZBY33AS6yPYZBgIu2fKsAlTZCOczaIouZCoRy0W2XxokiPy1Mdi1B4FFl5p05iIYLJvAhx3z6RpC6mVixieAf6scv5R2kEZD"



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
      with open('frases.json', encoding='utf-8') as openfile:
                # Reading from json file
                frase = json.load(openfile)
      numero = random.randrange(0, len(frase), 1)
      return frase[numero]
  


  def publicar(self,image_url, caption):
            post_url = "https://graph.facebook.com/v17.0/%s/media" % (ig_user_id)
            param = dict()
            param["access_token"] = access_token2
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
                    "access_token": access_token2,
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
  


    # Start the OAuth flow to retrieve credentials
  def authorize_credentials(self):
        CLIENT_SECRET = 'client_secret.json'
        SCOPE = 'https://www.googleapis.com/auth/photoslibrary'
        STORAGE = Storage('credentials.storage')
        # Fetch credentials from storage
        credentials = STORAGE.get()
        # If the credentials doesn't exist in the storage location then run the flow
        if credentials is None or credentials.invalid:
            flow = flow_from_clientsecrets(CLIENT_SECRET, scope=SCOPE)
            http = httplib2.Http()
            credentials = run_flow(flow, STORAGE, http=http)
        return credentials

  def get_access_token(self):
        credentials = self.authorize_credentials()
        access_token = credentials.access_token
        return access_token

  def getPhotoUrl(self, access_token, photo_id):
        # Set the headers for the request
        headers = {
            "Authorization": "Bearer " + access_token,
            "Content-type": "application/json"
        }

        # Set the URL for the request
        url = "https://photoslibrary.googleapis.com/v1/mediaItems/" + photo_id

        # Send the GET request
        response = requests.get(url, headers=headers)

        # Parse the response as JSON
        response_json = response.json()

        # Get the URL of the photo from the response
        photo_url = response_json["baseUrl"]
        return photo_url

  def uploadPhoto(self, caption):
        access_token = self.get_access_token()
        # Set up the request headers
        headers = {
            'Authorization': 'Bearer %s' % access_token,
            'Content-type': 'application/octet-stream',
            'X-Goog-Upload-Content-Type': 'image/jpeg',
            'X-Goog-Upload-Protocol': 'raw'
        }

        image_path = 'foto/frase.jpg'
        # Read the binary data from file
        with open(image_path, 'rb') as f:
            image_data = f.read()

        # Send the POST request to get the upload token
        response = requests.post('https://photoslibrary.googleapis.com/v1/uploads',
                                headers=headers, data=image_data)

        # Check if the request was successful and get the upload token
        if response.status_code == requests.codes.ok:
            upload_token = response.text
            headers = {
                'Authorization': 'Bearer %s' % access_token,
                'Content-type': 'application/json'
            }
            payload = {
                "newMediaItems": [
                        {
                            "simpleMediaItem": {
                                "fileName": os.path.basename(image_path),
                                "uploadToken": upload_token
                            }
                        }
                    ]
                }
            # Send the POST request to get the upload token
            response = requests.post('https://photoslibrary.googleapis.com/v1/mediaItems:batchCreate',
                                    headers=headers, json=payload)   
            json_response = response.json()
            photo_id = json_response['newMediaItemResults'][0]['mediaItem']['id']
            #If you want to get public url for anyone can see 
            photo_url = self.getPhotoUrl(access_token, photo_id)
            print("mediaItems full response = ",json_response,'\n\n\n',"public url = ", photo_url)
            self.publicar(photo_url,caption)
        else:
            response.raise_for_status()
      
        
           
              
        
     
    








