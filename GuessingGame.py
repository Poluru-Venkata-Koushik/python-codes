import tkinter as tk
import random
root = tk.Tk()
root.title("Guessing Game")
root.geometry("500x300")
root.resizable(False, False)
main_head = tk.Label(root, text="choose a number. You have only 3 attempts to do this ;)")
main_head.place(x=100, y=10)
guess = 3
number = random.randint(1, 10)
lab1=tk.Label(root, text="Guesses remaining :{})".format(guess))
lab1.place(x=400,y=70)
button1 = tk.Button(root, text="1")
button1.place(x=100, y=50)

root.mainloop()
