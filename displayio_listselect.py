# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2021 Tim Cocks for CircuitPython Organization
#
# SPDX-License-Identifier: MIT
"""
`displayio_listselect`
================================================================================

ListSelect widget for circuitpython displayio. Display a list of strings with a selection indicator allow user to move selection up and down.


* Author(s): Tim Cocks

Implementation Notes
--------------------

**Hardware:**

* Any displayio supported display.

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/circuitpython/CircuitPython_Org_DisplayIO_ListSelect.git"

# imports
import terminalio
from adafruit_display_text.bitmap_label import Label
from displayio import Group


class ListSelect(Group):
    def __init__(
            self,
            items=None,
            font=terminalio.FONT,
            x=0,
            y=0,
            color=0xffffff,
            background_color=0x000000,
            selected_index=0,
            cursor_char=">",
            *args,
            **kwargs
    ):
        super().__init__(x=x, y=y, scale=1)
        self._label = Label(font, text="", color=color, background_color=background_color, **kwargs)
        self._label.anchor_point = (0, 0)
        self._label.anchored_position = (0, 0)

        self.items = items
        self._selected_index = selected_index
        self.cursor_char = cursor_char

        self.append(self._label)
        self._refresh_label()

    def _refresh_label(self):
        """ Called any time that we need to update the displayed label. """
        _full_str = ""
        for i, item in enumerate(self.items):
            if i == self.selected_index:
                _full_str += self.cursor_char
            else:
                _full_str += " "
            _full_str += item

            if i != len(self.items) - 1:
                _full_str += "\n"

        self._label.text = _full_str

    def move_selection_down(self):
        if self.selected_index + 1 < len(self.items):
            self.selected_index += 1
            self._refresh_label()

    def move_selection_up(self):
        if self.selected_index - 1 >= 0:
            self.selected_index -= 1
            self._refresh_label()

    @property
    def width(self):
        """The widget width, in pixels. (getter only)
        :return: int
        """
        return self._label.bounding_box[2]

    @property
    def height(self):
        """The widget height, in pixels. (getter only)
        :return: int
        """
        return self._label.bounding_box[3]

    @property
    def bounding_box(self):
        return self._label.bounding_box

    def resize(self, new_width, new_height):
        raise NotImplementedError("Label does not support arbitrary sizing, so neither does ListSelect.")

    @property
    def anchor_point(self):
        return self._label.anchor_point

    @anchor_point.setter
    def anchor_point(self, new_anchor_point):
        self._label.anchor_point = new_anchor_point

    @property
    def anchored_position(self):
        return self._label.anchored_position

    @anchored_position.setter
    def anchored_position(self, new_anchored_position):
        self._label.anchored_position = new_anchored_position

    @property
    def selected_index(self):
        return self._selected_index

    @selected_index.setter
    def selected_index(self, new_index):
        self._selected_index = new_index
        self._refresh_label()

    @property
    def selected_item(self):
        return self.items[self._selected_index]
