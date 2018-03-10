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
		font = QFont("Helvetica Neue", 95, QFont.Bold)
		smallFont = QFont("Helvetica Neue", 33, QFont.Bold)
		successFont = QFont("Helvetica Neue", 65, QFont.Bold)
		#nameLabel.setAlignment(QtCore.Qt.AlignCenter)
		leftBar = QProgressBar()
		leftBar.setOrientation(QtCore.Qt.Vertical)
		style ="""
		        QProgressBar {
		            border: 12px solid #000033;
		            border-radius: 12px;
		            width = 20px;
		        }
		        QProgressBar::chunk {
		        	background-color: #ffcc00;
		        }"""
		leftBar.setStyleSheet(style)
		leftBar.setMaximum(0)
		leftBar.setMaximum(10)
		leftBar.setValue(5)
		leftBar.setTextVisible(False)
		#policy = QSizePolicy(QSizePolicy.IgnoreFlag, QSizePolicy.IgnoreFlag)
		#leftBar.setSizePolicy(policy)
		leftBar.setFixedWidth(100)

		#leftBar.setFixedHeight(400)

		rightBar = QProgressBar()
		rightBar.setOrientation(QtCore.Qt.Vertical)
		rightBar.setStyleSheet(style)
		rightBar.setMaximum(10)
		rightBar.setValue(3)
		rightBar.setTextVisible(False)
		rightBar.setFixedWidth(100)


		pickBox = QVBoxLayout()
		backPick = QWidget()
		picksPerHour = QLabel("34")
		picksPerHour.setFont(font)
		picksPerHour.setStyleSheet("border: 1px solid #000033; background-color: #000033; color: white")
		labelPicks = QLabel("PICKS PER HOUR")
		labelPicks.setStyleSheet("color: white")
		labelPicks.setFont(smallFont)
		picksPerHour.setAlignment(Qt.AlignCenter)
		labelPicks.setAlignment(Qt.AlignCenter)
		backPick.setStyleSheet("border: 1px solid #000033; border-radius: 12px; background-color: #000033;")
		pickBox.addWidget(picksPerHour)
		pickBox.addWidget(labelPicks)
		backPick.setLayout(pickBox)



		weightBox = QVBoxLayout()
		backWeight = QWidget()
		weightDisplay = QLabel("25.6")
		weightDisplay.setFont(font)
		weightDisplay.setStyleSheet("border: 1px solid #000033; background-color: #000033; color: white")
		labelWeight = QLabel("GRAMS")
		labelWeight.setStyleSheet("color: white")
		labelWeight.setFont(smallFont)
		weightDisplay.setAlignment(Qt.AlignCenter)
		labelWeight.setAlignment(Qt.AlignCenter)
		backWeight.setStyleSheet("border: 1px solid #000033; border-radius: 12px; background-color: #000033;")
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
		confidenceDisplay.setAlignment(Qt.AlignCenter)
		labelConfidence.setAlignment(Qt.AlignCenter)
		backConfidence.setStyleSheet("border: 1px solid #000033; border-radius: 12px; background-color: #000033;")
		confidenceBox.addWidget(confidenceDisplay, Qt.AlignCenter)
		confidenceBox.addWidget(labelConfidence, Qt.AlignCenter)
		backConfidence.setLayout(confidenceBox)

		successBox = QVBoxLayout()
		backSuccess = QWidget()
		success = QLabel("SUCCESS")
		success.setStyleSheet("border: 0px; color: #000033")
		success.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		success.setAlignment(Qt.AlignCenter)
		backSuccess.setStyleSheet("border: 0px solid #000033; background-color: #ffcc00; border-radius: 12px")

		failure = QLabel("FAILURE")
		failure.setStyleSheet("color: white")
		failure.setAlignment(Qt.AlignCenter)
		failure.setFont(successFont)
		success.setFont(successFont)
		successBox.addWidget(success, Qt.AlignHCenter)
		backSuccess.setLayout(successBox)


		header = QLabel()
		header.setPixmap(QPixmap(os.getcwd() + "/header.png"))
		header.setScaledContents(True)

		imageBox = QVBoxLayout()
		backImage = QWidget()
		image = QLabel()
		image.setPixmap(QPixmap(os.getcwd() + "/camera1.png"))
		#image.keepAspectRatio()
		image.setStyleSheet("border: 10px; color: #000033; border-radius: 12px")
		backImage.setStyleSheet("border: 3px solid #000033; background-color: #000033; border-radius: 8px")
		image.setScaledContents(True)
		imageBox.addWidget(image, Qt.AlignCenter)
		backImage.setLayout(imageBox)

		icons = QLabel()
		icons.setPixmap(QPixmap(os.getcwd() + "/icons.png"))



		sensing = QLabel()
		sensing.setPixmap(QPixmap(os.getcwd() + "/all_off.png"))

		pause = QLabel()
		pause.setPixmap(QPixmap(os.getcwd() + "/pause_action.png"))

		error = QLabel()
		error.setPixmap(QPixmap(os.getcwd() + "/error_on.png"))

		top_layout = QGridLayout()

		top_layout.setColumnStretch(0, 1)
		top_layout.setColumnStretch(1, 2)
		top_layout.setColumnStretch(2, 1)
		top_layout.setRowStretch(0, 1.25)
		top_layout.setRowStretch(1, 1.5)
		top_layout.setRowStretch(2, 7)
		top_layout.setRowStretch(3, 1)
		top_layout.setRowStretch(4, 1)
		top_layout.setRowStretch(5, 1)

		top_layout.addWidget(leftBar, 2, 0, Qt.AlignHCenter)
		top_layout.addWidget(rightBar, 2, 2, Qt.AlignHCenter)
		top_layout.addWidget(backPick, 0, 2, 2, 1)
		top_layout.addWidget(backWeight, 3, 0, 2, 1)
		top_layout.addWidget(backConfidence, 3, 2, 2, 1)
		top_layout.addWidget(backSuccess, 0, 0, 2, 1)
		top_layout.addWidget(header, 0, 1, Qt.AlignCenter)
		top_layout.addWidget(backImage, 1, 1, 3, 1, Qt.AlignCenter)
		top_layout.addWidget(icons, 4, 1, Qt.AlignCenter)
		top_layout.addWidget(sensing, 5, 1, Qt.AlignCenter)
		top_layout.addWidget(pause, 5, 0, Qt.AlignCenter)
		top_layout.addWidget(error, 5, 2, Qt.AlignCenter)

		central_widget.setLayout(top_layout)
		self.setCentralWidget(central_widget)
		self.setFixedSize(1920, 1080)
		self.showFullScreen()


if __name__ == "__main__":
	QApplication.setStyle("Motif")
	app = QApplication(sys.argv) 
	app.setStyleSheet('QMainWindow{background-color: white}')
	ex = dexnetDisplay()
	sys.exit(app.exec_())




