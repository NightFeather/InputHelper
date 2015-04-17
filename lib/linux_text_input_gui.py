#!/usr/bin/env python
from gi.repository import Gtk as Gtk, Gdk as Gdk

class SimpleTextInput:
    def print_text(self):
        buffer = self.textInput.get_buffer()
        print(buffer.get_text())

    def destroy(self, widget, data=None):
        if self.print_text_flag == False:
            self.print_text()
        Gtk.main_quit()

    def on_key_press(self, widget, event):
        keyname = event.keyval
        if event.state and keyname == Gdk.KEY_Escape or keyname == Gdk.KEY_Return:
            self.print_text()
            self.print_text_flag = True
            self.destroy(self, widget)
        if keyname == Gdk.KEY_Return:
            Gtk.main_quit()

    def __init__(self):
        # create a new window
        self.print_text_flag = False
        window = Gtk.Window(Gtk.WindowType.TOPLEVEL)
        window.set_type_hint(Gdk.WindowTypeHint.DIALOG)
        window.set_title("Input Helper")
        window.set_default_size(300, 60)
        window.set_position(Gtk.WindowPosition.CENTER_ON_PARENT)
        window.connect("destroy", self.destroy)
        #window.set_border_width(10)
        self.textInput = Gtk.Entry()
        self.textInput.set_tooltip_text("Press Ctrl-Enter or Enter to insert string")
        self.textInput.connect("key-press-event", self.on_key_press)
        window.add(self.textInput)
        window.show_all()

    def main(self):
        Gtk.main()


if __name__ == "__main__":
    txt = SimpleTextInput()
    txt.main()
