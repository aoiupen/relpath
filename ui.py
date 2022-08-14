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
        self.ctr_layout = QHBoxLayout(self.ctr_widget)

        self.label_target = QLabel("Target path : ")
        self.label_root = QLabel("Root path : ")
        self.label_target.setGeometry(QRect(70, 80, 100, 100))
        self.label_root.setGeometry(QRect(70, 80, 100, 100))
        self.label_target_path = QLabel()
        self.label_root_path = QLabel()

        self.btn_target_path_dialog = QPushButton("...")
        self.btn_root_path_dialog = QPushButton("...")
        self.btn_target_path_dialog.clicked.connect(
            lambda: func.get_target_path(self.window, self))
        self.btn_root_path_dialog.clicked.connect(
            lambda: func.get_root_path(self.window, self))

        self.ctr_layout.addWidget(self.label_target)
        self.ctr_layout.addWidget(self.label_target_path)
        self.ctr_layout.addWidget(self.btn_target_path_dialog)
        self.ctr_layout.addWidget(self.label_root)
        self.ctr_layout.addWidget(self.label_root_path)
        self.ctr_layout.addWidget(self.btn_root_path_dialog)
        
        #
        self.label_rel = QLabel("Relative path : ")
        self.label_rel_path = QLabel("")
        self.ctr_layout.addWidget(self.label_rel)
        self.ctr_layout.addWidget(self.label_rel_path)
