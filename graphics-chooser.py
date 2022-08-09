import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from os import system

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="switch graphics mode")
        self.set_border_width(10)
        self.set_default_size(500, 200)

        self.box = Gtk.Box(spacing = 10)
        self.add(self.box)

        self.button_integrated = Gtk.Button()
        self.button_integrated.set_label("use integrated graphics(battery)")
        self.button_integrated.connect("clicked", self.integrated_clicked)
        self.box.pack_start(self.button_integrated, True, True, 0)

        self.button_dedicated = Gtk.Button()
        self.button_dedicated.set_label("use dedicated graphics(performance)")
        self.button_dedicated.connect("clicked", self.dedicated_clicked)
        self.box.pack_start(self.button_dedicated, True, True, 0)

    def integrated_clicked(self, widget):
        system("supergfxctl -m Integrated")
        system("gnome-session-quit --logout")

    def dedicated_clicked(self, widget):
        system("supergfxctl -m Dedicated")
        system("gnome-session-quit --logout")

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
