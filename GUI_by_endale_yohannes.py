from tkinter import *
class gui:
    def __init__(self):
        window = Tk()
        button = Button(window,text = 'OK',bg = 'yellow',command = self.click)
        button.pack()
        button = Button(window, text='cancel', bg='yellow', command=self.clicrk)
        button.pack()
        window.mainloop()

    def click(self):
        print('I\'m clicked')
    def clicrk(self):
        print('I\'m  not clicked')

gui()
