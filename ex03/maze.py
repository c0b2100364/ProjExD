import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""


def main_proc():
    global mx, my
    global cx, cy
    if key =="Up":
        my -= 1
    if key == "Down":
        my += 1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1


    if maze_lst[my][mx] == 0:
        cx, cy = mx*100+50, my*100+50
    else:
        if key =="Up" and key == "Left":
            my += 1
        if key == "Down" and key == "Right":
            my -= 1
    
    if mx == 13 and my == 7:
        mx, my =1, 1


    canv.coords("tori", cx, cy)
    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    maze_lst = mm.make_maze(15, 9)
    #print(maze_lst)
    
    #sta = tk.Label(root, text="スタート", fg = "red")
    #sta.place(x=150, y=150)

    mm.show_maze(canv, maze_lst)  

    tori = tk.PhotoImage(file="fig/3.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canv.create_image(cx, cy, image=tori, tag="tori")

    
    sta = tk.Label(root, text="スタート", fg = "red", font=("", 20))
    sta.place(x=105, y=130)

    gol = tk.Label(root, text = "ゴール", fg = "yellow", font = ("", 20))
    gol.place(x=1310, y=735)

    key =""



    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()

    root.mainloop()