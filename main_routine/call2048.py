from graphic_user_interface.gui_classes import *
from keyboard.kbd_inputs import *
from engine_2048.eng_classes import *
from engine_2048.eng_procedures import *


class Call2048:
    """ Doc String Game 2048 """

    def __init__(self, board_size=4):
        self.definitions = GameDefinitions(board_size)
        self.status = GameStatus()
        self.navigation = UserNavigation()
        self.cells = [GameCell(xy_index, self.definitions.get_board_size()) for xy_index in
                      range(self.definitions.get_board_size() ** 2)]
        find_cell_neighbors(self.cells)
        self.rootlevel = Tk()
        self.mainWindow = MainWindow(self.rootlevel, self.definitions)
        self.event_loop()

    def event_loop(self):
        # Button Events
        self.mainWindow.buttonStart.widget.bind('<Button-1>', self.button_start_event)
        self.mainWindow.buttonRestart.widget.bind('<Button-1>', self.button_restart_event)
        # Keyboard Arrows Events
        self.rootlevel.bind('<Left>', self.left_event)
        self.rootlevel.bind('<Right>', self.right_event)
        self.rootlevel.bind('<Up>', self.up_event)
        self.rootlevel.bind('<Down>', self.down_event)
        # RELEASE events:
        self.rootlevel.bind('<KeyRelease>', self.update_graphic_interface_release)
        self.mainWindow.buttonStart.widget.bind('<ButtonRelease>', self.update_graphic_interface_release)
        self.mainWindow.buttonRestart.widget.bind('<ButtonRelease>', self.update_graphic_interface_release)
        # MainLoop
        self.rootlevel.mainloop()

    def left_event(self, event):
        if self.mainWindow.buttonStart.widget['text'] == 'Stop':
            key_press = 'left'
            self.navigation.set_keypress(key_press)
            process_the_event(self.cells, self.navigation, self.definitions, self.status, self.mainWindow)

    def right_event(self, event):
        if self.mainWindow.buttonStart.widget['text'] == 'Stop':
            key_press = 'right'
            self.navigation.set_keypress(key_press)
            process_the_event(self.cells, self.navigation, self.definitions, self.status, self.mainWindow)

    def up_event(self, event):
        if self.mainWindow.buttonStart.widget['text'] == 'Stop':
            key_press = 'up'
            self.navigation.set_keypress(key_press)
            process_the_event(self.cells, self.navigation, self.definitions, self.status, self.mainWindow)

    def down_event(self, event):
        if self.mainWindow.buttonStart.widget['text'] == 'Stop':
            key_press = 'down'
            self.navigation.set_keypress(key_press)
            process_the_event(self.cells, self.navigation, self.definitions, self.status, self.mainWindow)

    def button_start_event(self, event):
        if self.mainWindow.buttonStart.widget['text'] == 'Start the Game!':
            set_new_values_to_cells(self.cells, self.definitions, self.status, self.mainWindow.wcell)
            update_graphic_interface(self.cells, self.mainWindow.wcell)
        self.mainWindow.buttonStart.start_the_game()

    def button_restart_event(self, event):
        reset_cells(self.cells, self.mainWindow.wcell)
        self.mainWindow.buttonStart.widget['text'] = 'Stop'
        self.mainWindow.welcome.set_widget_text('Game 2048 - By Vanderlei A. Silva, 2020!!!')
        self.status.reset_score()
        self.mainWindow.wscore.set_score(self.status.get_score())
        set_new_values_to_cells(self.cells, self.definitions, self.status, self.mainWindow.wcell)
        update_graphic_interface(self.cells, self.mainWindow.wcell)

    def update_graphic_interface_release(self, event):
        for obj in self.cells:
            value = obj.get_value()
            if value is None:
                self.mainWindow.wcell[obj.xy_index].set_text('')
            else:
                self.mainWindow.wcell[obj.xy_index].set_text(value.__str__())
        time.sleep(0.2)
