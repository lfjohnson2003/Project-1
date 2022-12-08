from tkinter import *

john = 0
jane = 0


class GUI:
    def __init__(self, window):
        self.window = window

        self.frame_title = Frame(self.window)
        self.label_title = Label(self.frame_title, text='Vote Menu\t')
        self.label_title.pack(side='top', padx=150)
        self.frame_title.pack(anchor='w', pady=10)

        self.frame_check = Frame(self.window)
        self.label_check = Label(self.frame_check, text='Have you already voted?\t')
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_yes = Radiobutton(self.frame_check, text='Yes', variable=self.radio_1, value=1)
        self.radio_no = Radiobutton(self.frame_check, text='No', variable=self.radio_1, value=2)
        self.label_check.pack(side='left', padx=25)
        self.radio_yes.pack(side='left')
        self.radio_no.pack(side='left')
        self.frame_check.pack(anchor='w', pady=5)

        self.frame_candidate = Frame(self.window)
        self.label_candidate = Label(self.frame_candidate, text='Vote for candidate!\t')
        self.radio_2 = IntVar()
        self.radio_2.set(0)
        self.radio_john = Radiobutton(self.frame_candidate, text='John', variable=self.radio_2, value=1)
        self.radio_jane = Radiobutton(self.frame_candidate, text='Jane', variable=self.radio_2, value=2)
        self.label_candidate.pack(side='left', padx=25)
        self.radio_john.pack(side='left')
        self.radio_jane.pack(side='left')
        self.frame_candidate.pack(anchor='w', pady=5)

        self.frame_button = Frame(self.window)
        self.button_vote = Button(self.frame_button, text='VOTE', command=self.vote)
        self.button_vote.pack(anchor='w', pady=15)
        self.frame_button.pack()

        self.frame_result = Frame(self.window)
        self.label_result = Label(self.frame_result)
        self.label_result.pack(pady=10)
        self.frame_result.pack()

        self.frame_button2 = Frame(self.window)
        self.button_result = Button(self.frame_button2, text='SHOW RESULTS', command=self.results)
        self.button_result.pack(anchor='w', pady=15)
        self.frame_button2.pack()

    def vote(self):
        check = self.radio_1.get()
        vote = self.radio_2.get()

        if check == 1:
            self.label_result.config(text='Sorry but you already voted! \n'
                                          'Come back some other time.')
            self.radio_1.set(0)
            self.radio_2.set(0)
        elif check == 2:
            if vote == 1:
                global john
                john += 1
                self.label_result.config(text='You voted for John!')
                self.radio_1.set(0)
                self.radio_2.set(0)
            elif vote == 2:
                global jane
                jane += 1
                self.label_result.config(text='You voted for Jane!')
                self.radio_1.set(0)
                self.radio_2.set(0)
            else:
                self.label_result.config(text='No votes found! Please vote fo a candidate!')
        else:
            self.label_result.config(text='Please select if you have voted already or not!')

    def results(self):
        global john
        global jane
        if john > jane:
            self.label_result.config(text=f'Voting Complete! \n'
                                          f'Total Votes: {john + jane} \n'
                                          f'John wins with {john} votes! \n'
                                          f'Jane lost with {jane} votes!')
            john = 0
            jane = 0
        elif john < jane:
            self.label_result.config(text=f'Voting Complete! \n'
                                          f'Total Votes: {john + jane} \n'
                                          f'Jane wins with {jane} votes! \n'
                                          f'John lost with {john} votes!')
            john = 0
            jane = 0
        elif john == jane and john != 0:
            self.label_result.config(text=f'Voting Complete! \n'
                                          f'Total Votes: {john + jane} \n'
                                          f'No winner! Tied votes!')
            john = 0
            jane = 0
        else:
            self.label_result.config(text='No votes found! Please vote fo a candidate!')
