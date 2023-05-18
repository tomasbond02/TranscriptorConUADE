from transcriptorApi import *

'''Para utilizar el programa hay que instalar 3 cosas
    1- anaconda ya que torch (importante para el programa) no funciona en otros env
    2- chocolatey para instalar ffmpeg que tambien es importante
    3- recomiendo hacer un env en anaconda con todos los requerimientos para tener todo junto
'''


recognizedText = ''
videoName = 'video1.mp4'#nombre del video a transcribir
audioClipName = 'audioConvertido' 
audio = 'audioConvertido'
startSeconds = '' #en que segundo quiero q empiece a transcribir
endSeconds = '' #en que segundo quiero q deje de transcribir
audioSec = mp.VideoFileClip(videoName)

if startSeconds == '':
    startSeconds = 0
if endSeconds == '':
    endSeconds = audioSec.duration

cortadorMp4(videoName, startSeconds, endSeconds)
convertor_a_mp3(videoName, audioClipName)
recognizedText, traduccionIngles = reconocedor(audio)
print(recognizedText)
print(traduccionIngles)
text_file = open('transcripcion.txt','w')#exporta un txt con la transcripcion
text_file.write(recognizedText)
text_file.close()
text_traduction = open('traduction.txt', 'w')
text_traduction.write(traduccionIngles)
text_traduction.close()