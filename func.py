import os
from PyQt5.QtWidgets import QFileDialog
import main


def get_target_path(window, ui):
    path = str(QFileDialog.getExistingDirectory(window, "Select Directory"))
    ui.label_target_path.setText(path)
    if ui.label_target_path.text() and ui.label_root_path.text():
        get_rel_path(ui, ui.label_target_path.text(), ui.label_root_path.text())

def get_root_path(window, ui):
    path = str(QFileDialog.getExistingDirectory(window, "Select Directory"))
    ui.label_root_path.setText(path)
    if ui.label_target_path.text() and ui.label_root_path.text():
        get_rel_path(ui, ui.label_target_path.text(), ui.label_root_path.text())

def get_rel_path(ui, label_target_path, label_root_path):
    path = os.path.relpath(label_target_path, label_root_path)
    ui.label_rel_path.setText(path)
    pass
