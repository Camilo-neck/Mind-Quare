import tkinter as tk, threading
import imageio
from PIL import Image, ImageTk
import login

video_name = "Resources/Videos/MIND QUARE.mp4" #This is your video file path
video = imageio.get_reader(video_name)

def stream(label,Inicio):

    for image in video.iter_data():
        frame_image = ImageTk.PhotoImage(Image.fromarray(image))
        label.config(image=frame_image)
        label.image = frame_image
    Inicio.destroy()
    #login.main()

def video_inicio():
    Inicio = tk.Tk()
    sw = Inicio.winfo_screenwidth()
    sh = Inicio.winfo_screenheight()
    x = sw // 3
    y = sh // 4
    Inicio.geometry(f"500x405+{x}+{y}")
    my_label = tk.Label(Inicio)
    my_label.pack()
    thread = threading.Thread(target=stream, args=(my_label,Inicio))
    thread.daemon = 1
    thread.start()
    Inicio.mainloop()

video_inicio()