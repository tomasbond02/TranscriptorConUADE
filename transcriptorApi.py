#import speech_recognition as sr
import moviepy.editor as mp
import pyttsx3
import whisper
import os

def cortadorMp4(videoName:str, startSeconds: int = None, endSeconds:int = None):
    #en el caso que se quiera delimitar los segundos de transcripcion
    videoFile = mp.VideoFileClip(videoName)
    if(startSeconds is not None and endSeconds is not None ):
        clips = videoFile.subclip(startSeconds,endSeconds)
        clips.write_videofile(videoName)
    videoFile.close()

def convertor_a_mp3(clipVideoName:str, audioClipName:str):
    clip = mp.VideoFileClip(clipVideoName)
    clip.audio.write_audiofile(f'{audioClipName}.mp3')
    clip.close()

def reconocedor(audio:str):
    #utiliza whisper para transcribir el audio de convertor_a_mp3
    audioR = f'{audio}.mp3'
    recognizedText = ""
    model = whisper.load_model("medium")#se puede utilizar tiny, base, small, medium y large siendo que tiny tranquibe videos de 10 seg en menos de un minuto pero es mas propenso a errores y large... tarda mucho pero es casi perfecto
    result = model.transcribe(audioR)
    recognizedText = result["text"]
    return recognizedText

def deleteFile(fileName: str):
    os.remove(fileName)

def speechToText(text):
    #es para q exporte un mp3 con voz de robot estoy haciendo pruebas
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-86)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.save_to_file(text, "opf.mp3")
    engine.runAndWait()