from gui import *
from encode_faces import *
from cluster_faces import *


def start():
    root = Tk()

    app = App(root)
    app.place(relx=0, rely=0, relwidth=1, relheight=1)

    dpath = input("Insert here the directory's path:\n").replace("\\ ", " ")
    if dpath[-1] == " ":
        dpath = dpath[:-1]

    app.draw()

    encode(app, dpath)

    cluster(app)

    root.mainloop()


if __name__ == '__main__':
    start()
