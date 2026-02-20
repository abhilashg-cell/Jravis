import pywhatkit as kit
import datetime
from Brain.personality import jarvis_speak
from os import getcwd

now = datetime.datetime.now()
hour = now.hour
minute = now.minute

def clear_file():
    with open(f"{getcwd()}\\input.txt","w") as file:
        file.truncate(0)
        
anubhav = "+919606348280"

def send_msg_wa():
    jarvis_speak("To whom shall I send the message?")
    output_text = ""
    while True:
        with open("input.txt","r") as file:
            input_text = file.read().lower() 
        if input_text != output_text:
            output_text = input_text
            if output_text.startswith("send to") or output_text.startswith("send tu"):
                output_text.replace("send to","")
                output_text.replace("send tu","")
                if "anubhav" in output_text:
                    jarvis_speak("What is the content of the message?")
                    while True:
                       with open("input.txt","r") as file:
                          input_text = file.read().lower() 
                          if input_text != output_text:
                              output_text = input_text
                              if output_text.startswith("message is"):
                                  message =  output_text.replace("message is","")
                                  kit.sendwhatmsg(anubhav,message,hour,minute+1)
                                  jarvis_speak("Message sent successfully.", mood="success")
                                 

