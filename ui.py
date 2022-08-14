from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QCheckBox, QPushButton, QFileDialog
from PyQt5.QtCore import Qt, QRect
import func


class MainUi():
    def __init__(self):
        super().__init__()

    def setup_ui(self, MainWindow, app):
        self.app = app
        self.window = MainWindow
        self.window.showMinimized()
        self.window.setWindowTitle("rel path")
        self.ctr_widget = QWidget()
        self.window.setCentralWidget(self.ctr_widget)
        self.ctr_layout = QVBoxLayout(self.ctr_widget)

        self.layout_rel = QHBoxLayout()
        self.layout_target = QHBoxLayout()
        self.layout_root = QHBoxLayout()
        
        self.label_target = QLabel("Target path : ")
        self.label_root = QLabel("Root path : ")
        self.label_target.setFixedWidth(100)
        self.label_root.setFixedWidth(100)
        self.label_target_path = QLabel()
        self.label_root_path = QLabel()

        self.btn_target_path_dialog = QPushButton("...")
        self.btn_root_path_dialog = QPushButton("...")
        self.btn_target_path_dialog.setFixedWidth(30)
        self.btn_root_path_dialog.setFixedWidth(30)
        self.btn_target_path_dialog.clicked.connect(
            lambda: func.get_target_path(self.window, self))
        self.btn_root_path_dialog.clicked.connect(
            lambda: func.get_root_path(self.window, self))

        self.layout_target.addWidget(self.label_target)
        self.layout_target.addWidget(self.label_target_path)
        self.layout_target.addWidget(self.btn_target_path_dialog)
        self.layout_root.addWidget(self.label_root)
        self.layout_root.addWidget(self.label_root_path)
        self.layout_root.addWidget(self.btn_root_path_dialog)
        
        #
        self.label_rel = QLabel("Relative path : ")
        self.label_rel.setFixedWidth(100)
        self.label_rel_path = QLabel("")
        self.layout_rel.addWidget(self.label_rel) 
        self.layout_rel.addWidget(self.label_rel_path) 
        self.ctr_layout.addLayout(self.layout_rel)
        self.ctr_layout.addLayout(self.layout_root)
        self.ctr_layout.addLayout(self.layout_target)
