from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QCheckBox, QPushButton, QFileDialog, QSizePolicy
from PyQt5.QtCore import Qt, QRect,QSize
import os
import func



class MainUi():
    def __init__(self):
        super().__init__()

    def setup_ui(self, MainWindow, app):
        self.app = app
        self.window = MainWindow
        self.window.setWindowTitle("rel path")
        self.ctr_widget = QWidget()
        self.window.setCentralWidget(self.ctr_widget)
        self.ctr_layout = QVBoxLayout(self.ctr_widget)
        self.ctr_layout.setAlignment(Qt.AlignTop)

        self.layout_rel = QHBoxLayout()
        self.layout_target = QHBoxLayout()
        self.layout_start = QHBoxLayout()
        
        self.label_target = QLabel("Target path : ")
        self.label_start = QLabel("Start path : ")
        self.label_target.setFixedWidth(100)
        self.label_start.setFixedWidth(100)
        self.label_target_path = QLabel()
        self.label_start_path = QLabel()

        self.btn_target_path_dialog = QPushButton("...")
        self.btn_start_path_dialog = QPushButton("...")
        self.btn_target_path_dialog.setFixedWidth(30)
        self.btn_start_path_dialog.setFixedWidth(30)
        self.btn_target_path_dialog.clicked.connect(
            lambda: func.get_target_path(self.window, self))
        self.btn_start_path_dialog.clicked.connect(
            lambda: func.get_start_path(self.window, self))

        self.layout_target.addWidget(self.label_target)
        self.layout_target.addWidget(self.label_target_path)
        self.layout_target.addWidget(self.btn_target_path_dialog)
        self.layout_start.addWidget(self.label_start)
        self.layout_start.addWidget(self.label_start_path)
        self.layout_start.addWidget(self.btn_start_path_dialog)
        
        #
        self.label_rel = QLabel("Relative path : ")
        self.label_rel.setFixedWidth(100)
        self.label_rel_path = QLabel("")
        self.layout_rel.addWidget(self.label_rel) 
        self.layout_rel.addWidget(self.label_rel_path) 
        self.ctr_layout.addLayout(self.layout_rel)
        self.ctr_layout.addLayout(self.layout_start)
        self.ctr_layout.addLayout(self.layout_target)
        
        #
        self.btn = QPushButton("btn")
        self.hidden = True
        self.btn.clicked.connect(self.hide)
        self.ctr_layout.addWidget(self.btn)
        self.lineedit = QLineEdit()
        self.lineedit.hide()
        self.ctr_layout.addWidget(self.lineedit)

        self.layout_com_path = QHBoxLayout()   
        self.layout_each_path1 =QHBoxLayout()   
        self.layout_each_path2 = QHBoxLayout() 
        
        self.label_com = QLabel("Common Path : ")
        self.label_each1 = QLabel("Start Path : ")
        self.label_each2 = QLabel("Target Path : ")
        
        self.label_com_path = QLabel()
        self.label_each1_path = QLabel()
        self.label_each2_path = QLabel()
        
        self.layout_com_path.addWidget(self.label_com)
        self.layout_com_path.addWidget(self.label_com_path)
        self.layout_each_path1.addWidget(self.label_each1)
        self.layout_each_path1.addWidget(self.label_each1_path)
        self.layout_each_path2.addWidget(self.label_each2)
        self.layout_each_path2.addWidget(self.label_each2_path)
        
        self.ctr_layout.addLayout(self.layout_com_path)
        self.ctr_layout.addLayout(self.layout_each_path1)
        self.ctr_layout.addLayout(self.layout_each_path2)
        
        

        
    def hide(self):
        if self.hidden:
            print(1)
            self.hidden = False
            self.lineedit.show()
            #self.label_start_path.setText('<font color="blue">{a}</font><font color="red"> World</font><font color="green">!</font>'.format(a="1"))

        else:
            self.lineedit.hide()
            self.hidden = True
            
    
