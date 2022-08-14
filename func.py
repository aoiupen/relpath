import os
from typing import Sequence
from PyQt5.QtWidgets import QFileDialog
import main


def get_target_path(window, ui):
    path = str(QFileDialog.getExistingDirectory(window, "Select Directory"))
    ui.label_target_path.setText(path)
    if ui.label_target_path.text() and ui.label_start_path.text():
        get_rel_path(ui, ui.label_target_path.text(), ui.label_start_path.text())

def get_start_path(window, ui):
    path = str(QFileDialog.getExistingDirectory(window, "Select Directory"))    
    ui.label_start_path.setText(path)
    if ui.label_target_path.text() and ui.label_start_path.text():
        get_rel_path(ui, ui.label_target_path.text(), ui.label_start_path.text())

def get_rel_path(ui, label_target_path, label_start_path):
    path = os.path.relpath(label_target_path, label_start_path)
    ui.label_rel_path.setText(path)
    tup_each_path = get_com_path(ui, label_target_path, label_start_path)
    

def get_com_path(ui, path1,path2):
    #dialog : \\ (window)
    #os.path : /
    compath = os.path.commonpath([path1,path2])
    compath = compath.replace("\\","/") #to os.path style
    remain_path1 = path1.lstrip(compath)
    remain_path2 = path2.lstrip(compath)
    
    ui.label_com_path.setText(compath)
    ui.label_each1_path.setText(remain_path1)
    ui.label_each2_path.setText(remain_path2)
    return remain_path1, remain_path2
