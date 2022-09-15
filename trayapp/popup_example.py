#!/usr/bin/env python3
import sys

from PyQt6 import QtWidgets


def show_popup_window():
    DLG_HEIGHT = 150
    DLG_WIDTH = 400

    dlg = QtWidgets.QDialog()
    dlg.setWindowTitle("HELLO!")
    dlg.setFixedSize(DLG_WIDTH, DLG_HEIGHT)

    print_msg_button = QtWidgets.QPushButton(dlg)
    print_msg_button.setText("Print to console")
    print_msg_button.resize(DLG_WIDTH // 3, DLG_HEIGHT // 3)
    print_msg_button.move(DLG_WIDTH // 2 - DLG_WIDTH // 3, DLG_HEIGHT // 3)
    print_msg_button.clicked.connect(lambda: print("Hello from popup window!"))

    close_button = QtWidgets.QPushButton(dlg)
    close_button.setText("Close")
    close_button.resize(DLG_WIDTH // 3, DLG_HEIGHT // 3)
    close_button.move(DLG_WIDTH // 2 + 10, print_msg_button.y())
    close_button.clicked.connect(dlg.close)

    dlg.exec()
