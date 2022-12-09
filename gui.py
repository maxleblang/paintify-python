import tkinter as tk
from tkinter import font as tkfont
from SpotifyUser import SpotifyUser as su
from PIL import ImageTk, Image
import os
import main

class Gui(tk.Tk):
    """Initializes the frames"""
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Gotham', size=40, weight="bold", slant="italic")
        self.page_font = tkfont.Font(family='Gotham', size=25, weight='bold')
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = 1, pady = 10,)
        container['bg'] = 'green'
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainPage, Login, Gallery, Page2, SelectPlaylist):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainPage")

    """Shows a frame for the given page name"""
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class MainPage(tk.Frame):
    """Initializes the Mainpage frame of the page
        :param parent
        :param controller"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background = 'green')
        self.controller = controller
        controller['bg'] = 'green'
        label = tk.Label(self, text="Paintify", font=controller.title_font)
        label.pack(side= 'top', pady=25)
        label['bg'] = 'green'

        button_Login = tk.Button(self, text="Login",
                            command=lambda: controller.show_frame("Login"), height=2, width=30)
        button_Quit = tk.Button(self, text = "Quit Application",
                            command = controller.destroy, height = 2, width = 30)
        button_Login.pack(pady = 10)
        button_Quit.pack(pady = 10)

class Login(tk.Frame):
    """Initializes the Login frame of the page
        :param parent: a frame/screen"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background = 'green')
        self.controller = controller
        label = tk.Label(self, text="Please Login To Your Spotify Account", font=controller.page_font, pady = 20)
        label['bg'] = 'green'
        label.pack()

        button_Cont = tk.Button(self, text="Sing in With Spotify",
                           command= lambda: auth(), height = 2, width = 30)
        button_Cont.pack(pady = 15)


        button = tk.Button(self, text="Main Screen",
                           command=lambda: controller.show_frame("MainPage"), height = 2, width = 30)
        button.pack(side = 'bottom', pady = 30)

        def auth():
            label = tk.Label(self, bg = 'green', text="Please Enter the URL\nYou Were Redirected to in the Command Line", font=controller.page_font, pady = 30)
            label.pack()
            user = su()
            user.authenticate()
            user.get_playlists()
            label.destroy

            controller.show_frame("Page2")            

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background = 'green')
        self.controller = controller
        label = tk.Label(self, bg = 'green', text="Welcome", font=controller.page_font, pady = 20)
        label.pack()
        label1 = tk.Label(self, bg = 'green', text="Please select one of the Options below:", font=tkfont.Font(family='Gotham', size=15, weight='bold'), pady = 20)
        label1.pack()
        button_Playlist = tk.Button(self, text="Select Playlist",
                            command=lambda: controller.show_frame("SelectPlaylist"), height=2, width=30)
        button_Gallery = tk.Button(self, text = "View Your Gallery",
                            command = lambda: controller.show_frame("Gallery"), height = 2, width = 30)
        button_Playlist.pack(pady = 10)
        button_Gallery.pack(pady = 10)
        button_Return = tk.Button(self, text="Logout",
                            command=lambda: controller.show_frame("Login"), height=2, width=30)
        button_Return.pack(side = 'bottom', pady = 10)


class SelectPlaylist(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background = 'green')
        self.controller = controller
        label = tk.Label(self, text="Playlist Select Page", font=controller.page_font, pady = 20)
        label['bg'] = 'green'
        label.pack()

        button_Return = tk.Button(self, text="View Playlists",
                            command=lambda: view(), height=2, width=30)
        button_Return.pack(side = 'top', pady = 10)

        def view():
            user = su()
            user.authenticate()
            play = user.get_playlists()
            keys = []
            for i in play:
                keys.append(i)

            list = tk.Variable(value=keys)

            listbox = tk.Listbox(self, fg = 'black', bg = 'dark grey', listvariable = list, height=len(keys), selectmode='multiple', justify = 'center')
            listbox.pack(fill='both')
            label_Wait = tk.Label(self, text="You may have to wait a moment after clicking send", font=tkfont.Font(family='Gotham', size=15, weight='bold'), pady = 20, bg = 'green')
            label_Wait.pack(side = 'bottom')

        

            def func1():
                selected_playlists = listbox.curselection()
                playlist_names = [listbox.get(i) for i in selected_playlists]
                playlist = {}
                print(playlist_names[0])
                for i in range(len(playlist_names)):
                    playlist[playlist_names[i]] = play[playlist_names[i]]
                func2(playlist)
                label_new = tk.Label(self, text="Thanks For Waiting\nYou May Now View The Image in Your Gallery", font=controller.page_font, pady = 20, bg = 'green')
                label_new.pack(side = 'bottom')
            def func2(playlist):
                main.main1(playlist)



            button_Send = tk.Button(self, text="Send Playlist",
                            command=lambda: func1(), height=2, width=30)
            button_Send.pack(side = 'right', pady = 10, padx = 25)

            button_Return = tk.Button(self, text="Return",
                            command=lambda: controller.show_frame("Page2"), height=2, width=30)
            button_Return.pack(side = 'left', pady = 10, padx = 25)
    
class Gallery(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = 'green')
        self.controller = controller
        label = tk.Label(self, bg = 'green', text="Gallery of Photos", font=controller.page_font)
        label.pack()
        button_Return = tk.Button(self, text="Return",
                            command=lambda: controller.show_frame("Page2"), height=2, width=25)
        button_Return.pack(side = 'bottom', pady = 10)
        button_Refresh = tk.Button(self, text="Refresh Gallery",
                            command=lambda: gen_gallery(), height=2, width=25)
        button_Refresh.pack(side = 'bottom', pady = 10)

        def gen_gallery():
            path = "C:/EECE 2140/Project/paintify-main/jpgs"
            filename = os.listdir(path)
            print(filename)
            xpos = 115
            ypos = 100
            for f in filename:
                img=Image.open(f'C:\EECE 2140\Project\paintify-main\jpgs\{f}') # read the image file
                img=img.resize((100,100))
                img=ImageTk.PhotoImage(img)
                e1 =tk.Label(self, image = img)
                e1.image = img
                e1.place(x = xpos, y = ypos) # garbage collection 
                if(xpos==1315): # start new line after third column
                    ypos += 150# start wtih next row
                    xpos =115    # start with first column
                else:       # within the same row 
                    xpos += 150 # increase to next column
        gen_gallery()
            
if __name__ == "__main__":
    app = Gui()
    app.mainloop()