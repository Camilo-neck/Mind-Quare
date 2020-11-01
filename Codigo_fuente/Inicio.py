import tkinter as tk, threading
import imageio, time
from PIL import Image, ImageTk

video_name = "Resources/Videos/MIND QUARE.mp4" #This is your video file path
video = imageio.get_reader(video_name)

def stream(label,Inicio):

    for image in video.iter_data():
        frame_image = ImageTk.PhotoImage(Image.fromarray(image))
        label.config(image=frame_image)
        label.image = frame_image
    time.sleep(0.001)
    #Inicio.destroy()
    #login.main()

def destruir(Inicio):
    Inicio.destroy()

def video_inicio():
    Inicio = tk.Tk()
    Inicio.title('MindQuare')
    Inicio.iconbitmap("Resources\Images\Logo_Mindquare.ico")
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

if __name__ == '__main__':
    video_inicio()