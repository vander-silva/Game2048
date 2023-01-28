from tkinter import *
import tkinter.font as tkFont
import time


class WidgetFrame:
    def __init__(self, toplevel):
        self.objFrame = Frame(toplevel)
        self.objFrame.pack()

    def get_objframe(self):
        return self.objFrame


class WidgetButtonStart:
    def __init__(self, toplevel, button_text1, button_text2=''):
        self.widget = Button(toplevel,
                             text=button_text1,
                             bg='lightblue',
                             fg="red",
                             height=1,  # lines of text
                             width=len(button_text1),  # letters
                             padx=10,  # vertical space for left and right borders
                             pady=5,  # horizontal space for left and right borders
                             font=tkFont.Font(size=13, font='bold'))
        # self.widget.bind('<Button-1>', self.start_the_game)  # <button-1> = the left one
        # self.widget.bind('<Button-2>', self.start_the_game)  # <button-2> = the middle one (if it exits)
        # self.widget.bind('<Button-3>', self.start_the_game)  # <button-3> = the right one
        self.widget.pack(side=LEFT)
        self.buttonText1 = button_text1
        self.buttonText2 = button_text2 if button_text2 != '' else button_text1

    def start_the_game(self):
        ''' change the color when a button is pressed'''
        if self.widget['bg'] == 'lightblue':
            self.widget['bg'] = 'lightgreen'
        else:
            self.widget['bg'] = 'lightblue'
        # Alternating between text 1 and 2
        if self.widget['text'] == self.buttonText1:
            self.widget['text'] = self.buttonText2
        else:
            self.widget['text'] = self.buttonText1


class WidgetButtonRestart:
    def __init__(self, toplevel, button_text1, button_text2=''):
        self.widget = Button(toplevel,
                             text=button_text1,
                             bg='lightblue',
                             fg="red",
                             height=1,  # lines of text
                             width=len(button_text1),  # letters
                             padx=10,  # vertical space for left and right borders
                             pady=5,  # horizontal space for left and right borders
                             font=tkFont.Font(size=13, font='bold'))
        self.widget.bind('<Button-1>', self.restart_the_game)  # <button-1> = the left one
        self.widget.bind('<Button-2>', self.restart_the_game)  # <button-2> = the middle one (if it exits)
        self.widget.bind('<Button-3>', self.restart_the_game)  # <button-3> = the right one
        self.widget.pack(side=LEFT)
        self.buttonText1 = button_text1
        self.buttonText2 = button_text2 if button_text2 != '' else button_text1

    def restart_the_game(self, event):
        ''' change the color when a button is pressed'''
        if self.widget['bg'] == 'lightblue':
            self.widget['bg'] = 'lightgreen'
        else:
            self.widget['bg'] = 'lightblue'
        # Alternating between text 1 and 2
        if self.widget['text'] == self.buttonText1:
            self.widget['text'] = self.buttonText2
        else:
            self.widget['text'] = self.buttonText1


class WidgetLabel:
    def __init__(self, toplevel, label_text, label_width, label_height, label_side=LEFT):
        self.widget = Label(toplevel,
                            text=label_text,
                            # text="Hello. Welcome to your 2048 Game!!!",
                            fg="white",
                            font=tkFont.Font(size=15),
                            # bg="black",
                            bg="#34A2FE",
                            width=label_width,
                            # width=80,
                            height=label_height
                            # height=2
                            )
        self.widget.pack(side=label_side)

    def set_widget_text(self, text):
        self.widget['text'] = text


class WidgetScoreLabel:
    def __init__(self, toplevel, label_text, label_width, label_height, label_side=LEFT):
        self.widget = Label(toplevel,
                            text=label_text,
                            # text="Hello. Welcome to your 2048 Game!!!",
                            fg="white",
                            font=tkFont.Font(size=15),
                            # bg="black",
                            bg="#34A2FE",
                            width=label_width,
                            # width=80,
                            height=label_height
                            # height=2
                            )
        self.widget.pack(side=label_side)

    def set_score(self, score: int):
        self.widget['text'] = f'Score: {score.__str__()}'

    def reset_score(self):
        self.widget['text'] = f'Score: 0'


class WidgetCellLabel:
    def __init__(self, toplevel, label_text, label_width, label_height, label_side=LEFT):
        self.widget = Label(toplevel,
                            text=label_text,
                            # text="Hello. Welcome to your 2048 Game!!!",
                            fg="#79776C",
                            font=tkFont.Font(size=36, weight='bold'),
                            # bg="black",
                            bg="#CDC1B4",  # https://htmlcolorcodes.com/
                            padx=1,  # vertical space for left and right borders
                            pady=1,  # horizontal space for left and right borders
                            width=label_width,
                            borderwidth=1,
                            relief='ridge',
                            # width=80,
                            height=label_height
                            # height=2
                            )
        self.widget.pack(side=label_side)
        self.is_new_xy_value = False

    def set_text(self, wtext):
        self.widget['text'] = wtext
        if self.widget['text'] == '':
            # self.widget['bg'] = '#DED7B4'  # https://htmlcolorcodes.com/
            self.widget['bg'] = '#CDC1B4'  # https://htmlcolorcodes.com/
        elif self.widget['text'] == '2':
            self.widget['bg'] = '#FBF6DD'  # https://htmlcolorcodes.com/
            self.widget['fg'] = '#746B63'  # https://htmlcolorcodes.com/
        elif self.widget['text'] == '4':
            self.widget['bg'] = '#EEE4DA'  # https://htmlcolorcodes.com/
            self.widget['fg'] = '#746B63'  # https://htmlcolorcodes.com/
        elif self.widget['text'] == '8':
            self.widget['bg'] = '#F2B179'  # https://htmlcolorcodes.com/
            self.widget['fg'] = '#F9F6F2'  # https://htmlcolorcodes.com/
        elif self.widget['text'] == '16':
            self.widget['bg'] = '#F59563'  # https://htmlcolorcodes.com/
            self.widget['fg'] = '#F9F6F2'  # https://htmlcolorcodes.com/
        elif self.widget['text'] == '32':
            self.widget['bg'] = '#F67C5F'  # https://htmlcolorcodes.com/
            self.widget['fg'] = '#F9F6F2'  # https://htmlcolorcodes.com/
        elif self.widget['text'] == '64':
            self.widget['bg'] = '#F65E3B'  # https://htmlcolorcodes.com/
            self.widget['fg'] = '#F9F6F2'  # https://htmlcolorcodes.com/
        elif self.widget['text'] == '128':
            self.widget['bg'] = '#EDCF72'  # https://htmlcolorcodes.com/
            self.widget['fg'] = '#F9F6F2'  # https://htmlcolorcodes.com/
        elif self.widget['text'] == '256':
            self.widget['bg'] = '#EDCC61'  # https://htmlcolorcodes.com/
            self.widget['fg'] = '#F9F6F2'  # https://htmlcolorcodes.com/
        elif self.widget['text'] == '512':
            self.widget['bg'] = '#EDC850'  # https://htmlcolorcodes.com/
            self.widget['fg'] = '#F9F6F2'  # https://htmlcolorcodes.com/
        elif self.widget['text'] == '1024':
            self.widget['bg'] = '#534109'  # https://htmlcolorcodes.com/
            self.widget['fg'] = '#F9F6F2'  # https://htmlcolorcodes.com/
        elif self.widget['text'] == '2048':
            self.widget['bg'] = '#534109'  # https://htmlcolorcodes.com/
            self.widget['fg'] = '#F9F6F2'  # https://htmlcolorcodes.com/
        elif self.widget['text'] == '4096':
            self.widget['bg'] = '#534109'  # https://htmlcolorcodes.com/
            self.widget['fg'] = '#F9F6F2'  # https://htmlcolorcodes.com/
        if self.is_new_xy_value:
            self.is_new_xy_value = False
            self.widget['bg'] = '#CBFFD4'

    def get_bg_color(self):
        return self.widget['bg']

    def set_bg_color(self, color):
        self.widget['bg'] = color


class WidgetBlankLabel:
    def __init__(self, toplevel, label_width, label_height):
        self.widget = Label(toplevel,
                            text='',
                            width=label_width,
                            height=label_height
                            )
        self.widget.pack()

    def set_widget_text(self, text):
        self.widget['text'] = text


class MainWindow:
    def __init__(self, rootlevel, definitions):
        self.frameWelcome = WidgetFrame(rootlevel)
        self.frameUpBlank = WidgetFrame(rootlevel)
        self.wcell = []
        self.frameBoard = []
        self.wcellText = []
        for line in range(definitions.get_board_size()):
            self.frameBoard.append(WidgetFrame(rootlevel))
            for column in range(definitions.get_board_size()):
                # self.wcellText.append(f'{line.__str__()}{column.__str__()}')
                self.wcellText.append('')
                self.wcell.append(WidgetCellLabel(self.frameBoard[line].get_objframe(), '', 4, 2))
                self.wcell[len(self.wcell) - 1].widget['text'] = self.wcellText[len(self.wcell) - 1]
        self.frameDownBlank = WidgetFrame(rootlevel)
        self.frameButtons = WidgetFrame(rootlevel)
        self.frameBottomBlank = WidgetFrame(rootlevel)
        self.welcome = WidgetLabel(self.frameWelcome.get_objframe(), 'Game 2048 - By Vanderlei A. Silva, 2020!!!', 80, 2)
        WidgetBlankLabel(self.frameUpBlank.get_objframe(), 0, 1)
        WidgetBlankLabel(self.frameDownBlank.get_objframe(), 0, 1)
        self.buttonStart = WidgetButtonStart(self.frameButtons.get_objframe(), 'Start the Game!', 'Stop')
        self.buttonRestart = WidgetButtonRestart(self.frameButtons.get_objframe(), 'Restart')
        WidgetBlankLabel(self.frameBottomBlank.get_objframe(), 0, 1)
        self.wscore = WidgetScoreLabel(self.frameBottomBlank.get_objframe(), 'Score: 0', 80, 2)
        self.myFile = open('out.2048', 'w')
        self.myFile.write('\n')
        self.keyPress = ''
