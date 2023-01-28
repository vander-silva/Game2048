#
# from pyprocedures_2028 import procedures
#
import time


def set_new_values_to_cells(cells, definitions, status, wcell):
    import random

    obj_list = []
    for obj in cells:
        if obj.get_value() is None:
            obj_list.append(obj)
    if len(obj_list) >= 2:
        obj_1 = random.choice(obj_list)
        obj_list.remove(obj_1)
        obj_2 = random.choice(obj_list)
        [value1, value2] = random.choices([2, 4], weights=(
            definitions.get_2_probability(), definitions.get_4_probability()), k=2)
        obj_1.set_value(value1)
        obj_2.set_value(value2)
        wcell[obj_1.xy_index].is_new_xy_value = True
        wcell[obj_2.xy_index].is_new_xy_value = True
    elif len(obj_list) == 1:
        obj_1 = random.choice(obj_list)
        [value1] = random.choices([2, 4],
                                  weights=(definitions.get_2_probability(), definitions.get_4_probability()),
                                  k=1)
        obj_1.set_value(value1)
    else:
        status.set_game_over(True)
        for obj in cells:
            obj.find_game_over(status)
        if status.get_game_over():
            print("Game Over...")
    # printBoard(cells)


def find_cell_neighbors(cells):
    for obj in cells:
        obj.find_neighbors(cells)
        # print('[x,y]=', obj.getPosition(), ', [L R U D]=', obj.getNeighborhood())
        obj.find_your_border_set()
        print('leftBorderSet:', obj.is_left_border_cell, '  rightBorderSet:', obj.is_right_border_cell, '  upBorderSet:',
              obj.is_up_border_cell, '  downBorderSet:', obj.is_down_border_cell)


def make_cells_association(cells, navigation, definitions, status):
    for iteraction in range(definitions.get_board_size() - 1):
        for obj in cells:
            # print(obj.getPosition(),'.......',msg.getMsgType())
            obj.start_push_value(navigation)

    for obj in cells:
        # print(obj.getPosition(), '.......', msg.getMsgType())
        obj.start_join_your_neighbor(navigation, status)

    for iteraction in range(definitions.get_board_size() - 1):
        for obj in cells:
            # print(obj.getPosition(),'.......',msg.getMsgType())
            obj.start_push_value(navigation)


def update_graphic_interface(cells, wcell):
    for obj in cells:
        value = obj.get_value()
        if value is None:
            wcell[obj.xy_index].set_text('')
            # print(obj.xyIndex)
        else:
            wcell[obj.xy_index].set_text(value.__str__())
            # print(obj.xyIndex)


def print_board(cells, myfile):
    count = 0
    myfile.write('\n')
    for obj in cells:
        if count <= 3:
            # print('\n' if count == 1 else '', obj.getPosition(), '=',
            myfile.write(
                f'{obj.get_position()}= {obj.get_value() if obj.get_value() is None else "%4d" % (obj.get_value())}    ')
        else:
            myfile.write(
                f'\n{obj.get_position()}= {obj.get_value() if obj.get_value() is None else "%4d" % (obj.get_value())}    ')
            count = 0
        count += 1


def process_the_event(cells, navigation, definitions, status, main_window):
    make_cells_association(cells, navigation, definitions, status)
    main_window.wscore.set_score(status.get_score())
    set_new_values_to_cells(cells, definitions, status, main_window.wcell)
    if status.get_game_over():
        main_window.welcome.set_widget_text('Game Over!!!')
    update_graphic_interface(cells, main_window.wcell)


def reset_cells(cells, wcell):
    for obj in cells:
        obj.set_value(None)
    update_graphic_interface(cells, wcell)
