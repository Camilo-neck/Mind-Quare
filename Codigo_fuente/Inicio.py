import tkinter as tk, threading
import imageio
from PIL import Image, ImageTk
from time import sleep

import logging

import login


video_name = "Resources/Videos/MIND QUARE.mp4" #This is your video file path
video = imageio.get_reader(video_name)

class ventana():

    def __init__(self):

        self.Inicio = tk.Tk()

        self.sw = self.Inicio.winfo_screenwidth()
        self.sh = self.Inicio.winfo_screenheight()
        self.x = self.sw // 3
        self.y = self.sh // 4
        self.Inicio.geometry(f"500x405+{self.x}+{self.y}")
        self.Inicio.resizable(width=False, height=False)
        self.my_label = tk.Label(self.Inicio)
        self.my_label.pack()

        thread = threading.Thread(target=self.stream, args=(self.my_label,self.Inicio))
        thread.start()
  
        self.Inicio.mainloop()

    def stream(self,label,Inicio):

        for image in video.iter_data():
            frame_image = ImageTk.PhotoImage(Image.fromarray(image))
            label.config(image=frame_image)
            label.image = frame_image
            sleep(0.008)      

def main():
    ventana()
    login.Aplicacion()

if __name__=="__main__":
    main()