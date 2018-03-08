import os, sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class dexnetDisplay(QMainWindow):


	def __init__(self):
		super(dexnetDisplay, self).__init__()
		self.initUI()



	def initUI(self):
		#window.setFixedSize(960, 540)
		central_widget = QWidget()
		# Create some widgets
		nameLabel = QLabel("Dex-Net Demo")
		font = QFont("Helvetica Neue", 60, QFont.Bold)
		smallFont = QFont("Helvetica Neue", 20, QFont.Bold)
		#nameLabel.setAlignment(QtCore.Qt.AlignCenter)
		leftBar = QProgressBar()
		leftBar.setOrientation(QtCore.Qt.Vertical)
		style ="""
		        QProgressBar {
		            border: 5px solid #000033;
		            border-radius: 7px;
		        }
		        QProgressBar::chunk {
		        	background-color: #ffcc00;
		        }"""
		leftBar.setStyleSheet(style)
		leftBar.setMaximum(0)
		leftBar.setMaximum(10)
		leftBar.setValue(5)
		leftBar.setTextVisible(False)
		#leftBar.setFixedHeight(400)

		rightBar = QProgressBar()
		rightBar.setOrientation(QtCore.Qt.Vertical)
		rightBar.setStyleSheet(style)
		rightBar.setMaximum(10)
		rightBar.setValue(3)
		rightBar.setTextVisible(False)


		pickBox = QVBoxLayout()
		backPick = QWidget()
		picksPerHour = QLabel("34")
		picksPerHour.setFont(font)
		picksPerHour.setStyleSheet("border: 1px solid #000033; background-color: #000033; color: white")
		labelPicks = QLabel("PICKS PER HOUR")
		labelPicks.setStyleSheet("color: white")
		labelPicks.setFont(smallFont)
		picksPerHour.setAlignment(Qt.AlignHCenter)
		labelPicks.setAlignment(Qt.AlignHCenter)
		backPick.setStyleSheet("border: 1px solid #000033; border-radius: 7px; background-color: #000033;")
		pickBox.addWidget(picksPerHour)
		pickBox.addWidget(labelPicks)
		backPick.setLayout(pickBox)



		weightBox = QVBoxLayout()
		backWeight = QWidget()
		weightDisplay = QLabel("25.67")
		weightDisplay.setFont(font)
		weightDisplay.setStyleSheet("border: 1px solid #000033; background-color: #000033; color: white")
		labelWeight = QLabel("GRAMS")
		labelWeight.setStyleSheet("color: white")
		labelWeight.setFont(smallFont)
		weightDisplay.setAlignment(Qt.AlignHCenter)
		labelWeight.setAlignment(Qt.AlignHCenter)
		backWeight.setStyleSheet("border: 1px solid #000033; border-radius: 7px; background-color: #000033;")
		weightBox.addWidget(weightDisplay)
		weightBox.addWidget(labelWeight)
		backWeight.setLayout(weightBox)


		confidenceBox = QVBoxLayout()
		backConfidence = QWidget()
		confidenceDisplay = QLabel("85.2")
		confidenceDisplay.setFont(font)
		confidenceDisplay.setStyleSheet("border: 1px solid #000033; background-color: #000033; color: white")
		labelConfidence = QLabel("% CONFIDENCE")
		labelConfidence.setStyleSheet("color: white")
		labelConfidence.setFont(smallFont)
		confidenceDisplay.setAlignment(Qt.AlignHCenter)
		labelConfidence.setAlignment(Qt.AlignHCenter)
		backConfidence.setStyleSheet("border: 1px solid #000033; border-radius: 7px; background-color: #000033;")
		confidenceBox.addWidget(confidenceDisplay)
		confidenceBox.addWidget(labelConfidence)
		backConfidence.setLayout(confidenceBox)




		header = QLabel()
		header.setPixmap(QPixmap(os.getcwd() + "/header.png"))
		header.setScaledContents(True)

		image = QLabel()
		image.setPixmap(QPixmap(os.getcwd() + "/camera1.png"))
		image.setScaledContents(True)

		icons = QLabel()
		icons.setPixmap(QPixmap(os.getcwd() + "/icons.png"))



		sensing = QLabel()
		sensing.setPixmap(QPixmap(os.getcwd() + "/sensing.png"))

		pause = QLabel()
		pause.setPixmap(QPixmap(os.getcwd() + "/pause_plain.png"))

		error = QLabel()
		error.setPixmap(QPixmap(os.getcwd() + "/error_off.png"))

		top_layout = QGridLayout()


		top_layout.addWidget(leftBar, 1, 0, Qt.AlignHCenter)
		top_layout.addWidget(rightBar, 1, 2, Qt.AlignHCenter)
		top_layout.addWidget(backPick, 0, 0)
		top_layout.addWidget(backWeight, 2, 0)
		top_layout.addWidget(backConfidence, 0, 2)
		top_layout.addWidget(header, 0, 1, Qt.AlignCenter)
		top_layout.addWidget(image, 1, 1, Qt.AlignCenter)
		top_layout.addWidget(icons, 2, 1, Qt.AlignCenter)
		top_layout.addWidget(sensing, 3, 1, Qt.AlignCenter)
		top_layout.addWidget(pause, 3, 0, Qt.AlignCenter)
		top_layout.addWidget(error, 3, 2, Qt.AlignCenter)

		central_widget.setLayout(top_layout)
		self.setCentralWidget(central_widget)
		self.setFixedSize(1440, 810)
		self.show()


if __name__ == "__main__":
	QApplication.setStyle("Motif")
	app = QApplication(sys.argv) 
	app.setStyleSheet('QMainWindow{background-color: white}')
	ex = dexnetDisplay()
	sys.exit(app.exec_())




