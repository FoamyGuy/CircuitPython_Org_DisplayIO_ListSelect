# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2021 Tim Cocks for CircuitPython Organization
#
# SPDX-License-Identifier: Unlicense

# SPDX-FileCopyrightText: 2020 Tim C, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
"""
Make green and purple rectangles and a
"Hello World" label.
"""
import time
import displayio
import board
from displayio_listselect import ListSelect

# Make the display context. Change size if you want
display = board.DISPLAY

# Make the display context
main_group = displayio.Group()
display.show(main_group)

items = ["First", "Second", "Third", "Fourth"]

list_select = ListSelect(scale=2, items=items)

main_group.append(list_select)

list_select.anchor_point = (0.5, 0.5)
list_select.anchored_position = (display.width // 2, display.height // 2)

for i in range(3):
    list_select.move_selection_down()
    time.sleep(1)

for i in range(3):
    list_select.move_selection_up()
    time.sleep(1)

list_select.selected_index = 3
while display.running:
    pass
