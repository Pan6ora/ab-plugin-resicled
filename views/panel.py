
from PySide2 import QtCore
from PySide2.QtWidgets import (
    QCheckBox, QFileDialog, QHBoxLayout, QMessageBox, QPushButton, QToolBar,
    QStyle, QVBoxLayout, QTabWidget
)
from .PresentationTab import PresentationTab
from .inputTab import InputTab
from .dismantlingTab import DismantlingTab
from .shreddingTab import ShreddingTab


class ResicledTab(QTabWidget):
    def __init__(self, parent=None):
        super(ResicledTab, self).__init__(parent)
        self.tabs = dict([('index1',1),('index2',2),('index3',3)])
		# button = QPushButton("button 1")
		# self.addTab(button, "tab button 1")
		# Initialisation des tabs
        #presentationTab = PresentationTab()
        self.tabwidget = QTabWidget()
        self.tabs = {
            "Presentation": PresentationTab(self),
            "Input": InputTab(self),
            "Dismantling": DismantlingTab(self),
            "Shredding": ShreddingTab(self),
            "Mixed": QPushButton("button 5"),
            "HotSpots": QPushButton("button 6"),
            "Guidelines": QPushButton("button 7"),
            "Rapport": QPushButton("button 8"),
            "Pdf": QPushButton("button 9"),
            "Recyclability Rates": QPushButton("button 10"),
		}
        for tab_name, tab_obj in self.tabs.items():
            self.tabwidget.addTab(tab_obj, tab_name)
            # coleur arriere plan #daf7a6;
            tab_obj.setStyleSheet("background-color:  #9bbb59;")
            
        #display tab in layout   
        self.layout = QVBoxLayout()
        self.layout.setAlignment(QtCore.Qt.AlignTop)
        self.layout.addWidget(self.tabwidget)
        self.setLayout(self.layout)
	
