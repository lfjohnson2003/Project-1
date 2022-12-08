from VoteMenuGUI import *


def main():
    window = Tk()
    window.title('Vote Menu')
    window.geometry('400x350')
    window.resizable(False, False)

    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
