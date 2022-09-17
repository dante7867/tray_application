#!/usr/bin/env python3
import os, subprocess, webbrowser

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from popup_example import show_popup_window


class TrayApp:
    """A class representing tray application"""

    app = QApplication([])
    tray = QSystemTrayIcon()
    menu = QMenu()
    actions = {}


    def __init__(self):
        self.app.setQuitOnLastWindowClosed(False)
        self.tray.setIcon(QIcon("art/icons/pink-pig.png")) #main icon
        self.tray.setVisible(True)
       
        # social media
        social_media_submenu = self.get_social_media_submenu()
        self.menu.addMenu(social_media_submenu)
        self.menu.addSeparator()

        # main menu actions
        self.create_main_menu_actions()
        self.menu.addSeparator()

        # Just a showcase how to create popup
        a = self.create_menu_action(self.menu, "Popup example", show_popup_window) 
        self.menu.addSeparator()

        # Exit button
        a = self.create_menu_action(self.menu, "Exit", self.app.quit) 

        self.tray.activated.connect(self.redraw_menu)
        self.tray.setContextMenu(self.menu)
        self.app.exec()


    def get_social_media_submenu(self):
        submenu = QMenu()
        self.submenu = submenu
        submenu.setTitle("Social Media")
        
        self.create_menu_action(self.submenu, "Instagram", lambda: webbrowser.open_new("https://www.instagram.com/"), "art/icons/brand-instagram.png") 
        self.create_menu_action(self.submenu, "Facebook", lambda: webbrowser.open_new("https://www.facebook.com/"), "art/icons/brand-facebook.png") 
        self.create_menu_action(self.submenu, "TikTok", lambda: webbrowser.open_new("https://www.tiktok.com/"), "art/icons/brand-tiktok.png")

        return submenu


    def create_main_menu_actions(self):
        self.create_menu_action(self.menu, "Start cmd.exe", lambda: os.system("start cmd"), "art/icons/terminal-2.png") 
        self.create_menu_action(self.menu, "Start Notepad", lambda: os.system("start notepad"), "art/icons/notes.png") 
        self.create_menu_action(self.menu, "Start MsPaint", lambda: os.system("start mspaint"), "art/icons/palette.png") 
        self.menu.addSeparator()
        
        documents_path = "Documents"
        self.create_menu_action(self.menu, "Open Documents", lambda: subprocess.Popen(f'explorer {documents_path}'), "art/icons/books.png") 
        self.create_menu_action(self.menu, "Randomize wallpaper", lambda: os.system("python windows-wallpaper-randomizer/randomize_wallpaper.py -r")) 

    
    def create_menu_action(self, menu, name, function, icon_path = None):
        if not name:
            return

        action = QAction(name)
        action.triggered.connect(function)
        if icon_path:
            action.setIcon(QIcon(icon_path))
        menu.addAction(action)
        self.actions[name] = action

        return action


    def redraw_menu(self):
        print("Redrawing menu!")


if __name__ == "__main__":
    app = TrayApp()
