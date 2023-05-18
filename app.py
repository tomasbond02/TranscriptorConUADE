from transcriptorApi import *
from flask import Flask, request, jsonify
from datetime import datetime

#intento de api :-)
#utilizo postman para esto

app = Flask("api")
app.config['UPLOAD_FOLDER'] = '/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
ALLOWED_EXTENSIONS = {'mp4'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return '''
        <html>  
        <head>  
            <title>upload</title>
        </head>  
        <body>  
            <form action = "/convert" method = "post" enctype="multipart/form-data">  
                <input type="file" name="file" />  
                <input type = "submit" value="Upload">  
            </form>  
        </body>  
        </html>  
    '''

@app.route("/img", methods=["GET", "POST"]) 
def get_img():
    r = request.files.get("file1")
    with open("n.png", "wb") as fp: 
        for itm in r: fp.write(itm) 
        return "done"



@app.route("/convert", methods=['POST'])
def main():
    hash  = datetime.timestamp(datetime.now())

    if 'video' not in request.files and request.files['video'].filename == '' and allowed_file(request.files['video'].filename):
        response = jsonify('Envía un archivo en formato MP4 para convertir.')
        response.status_code = 400
        return response
    
    file = request.files['video']
    
    recognizedText = ''
    videoName = f'{hash}-newVideo.mp4'
    audioClipName = f'{hash}-audioConvertido'
    startSeconds = request.args.get('startSeconds')
    endSeconds = request.args.get('endSeconds')
    audio = audioClipName

    with open(videoName, "wb") as fp: 
        for itm in file: fp.write(itm) 

    try:
        cortadorMp4(videoName, startSeconds, endSeconds)
        convertor_a_mp3(videoName, audioClipName)
        recognizedText = reconocedor(audio)
        
    except Exception as e:
        print(e)
        response = jsonify('Ocurrió un error procesando su video. Intente más tarde.')
        response.status_code = 400
        return response
    finally:
        try:
            deleteFile(videoName)
            deleteFile(f'{audioClipName}.mp3')
        except Exception as e:
            print(e)
            
    return jsonify(recognizedText) 