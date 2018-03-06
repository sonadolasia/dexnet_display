import os, sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *


QApplication.setStyle("Motif")
app = QApplication(sys.argv) 
window = QWidget()
window.setFixedSize(1366, 800)
window.setWindowTitle("Hello World")
window.show()
# Create some widgets
nameLabel = QLabel("Dex-Net Demo")
#nameLabel.setAlignment(QtCore.Qt.AlignCenter)
leftBar = QProgressBar()
leftBar.setOrientation(QtCore.Qt.Vertical)
style ="""
        QProgressBar {
            border: 5px solid grey;
            border-radius: 10px;
            text-align: center;
        }

        QProgressBar::chunk {
            width: 100 px;
        }"""
leftBar.setStyleSheet(style)
leftBar.setMaximum(0)
leftBar.setMaximum(10)
leftBar.setValue(5)
leftBar.setFixedHeight(400)

rightBar = QProgressBar()
rightBar.setOrientation(QtCore.Qt.Vertical)
rightBar.setStyleSheet(style)
rightBar.setMaximum(10)
rightBar.setValue(3)
rightBar.setFixedHeight(400)


picksPerHour = QLCDNumber(2)
picksPerHour.display(34)
picksPerHour.setSegmentStyle(QtGui.QLCDNumber.Flat)
# QLCDColoring = """{
#    background-color:rgb(0, 170, 255);
#    }"""
# picksPerHour.setStyleSheet(QLCDColoring)
palette = picksPerHour.palette()
picksPerHour.setFixedSize(100, 100)

# foreground color
palette.setColor(palette.WindowText, QtGui.QColor(19, 19, 63))
# background color
palette.setColor(palette.Background, QtGui.QColor(0, 0, 0))
# "light" border
palette.setColor(palette.Light, QtGui.QColor(255, 199, 0))
# "dark" border
palette.setColor(palette.Dark, QtGui.QColor(255, 199, 0))

# set the palette
picksPerHour.setPalette(palette)
labelPicks = QLabel("PICKS PER HOUR")

weightDisplay = QLCDNumber(5)
weightDisplay.display(25.67)
weightDisplay.setSegmentStyle(QtGui.QLCDNumber.Flat)
weightDisplay.setFixedSize(100, 75)
#weightDisplay.setStyleSheet(QLCDColoring)
weightDisplay.setPalette(palette)

labelWeight = QLabel("GRAMS")

confidenceDisplay = QLCDNumber(4)
confidenceDisplay.display(85.2)
confidenceDisplay.setPalette(palette)
confidenceDisplay.setSegmentStyle(QtGui.QLCDNumber.Flat)
confidenceDisplay.setFixedSize(120, 100)

labelConfidence = QLabel("% CONFIDENCE")



header = QLabel()
header.setPixmap(QPixmap(os.getcwd() + "/header.png"))

image = QLabel()
image.setPixmap(QPixmap(os.getcwd() + "/camera.png"))

icons = QLabel()
icons.setPixmap(QPixmap(os.getcwd() + "/icons.png"))

button = QPushButton("hi");
button.setText("Planning");
button.setFixedHeight(80);
button.setFixedWidth(80);
#Set Starting point of region 5 pixels inside , make region width & height
#values same and less than button size so that we obtain a pure-round shape
region = QRegion((QRect(button.x()+5,button.y()+5,80,80)),QRegion.Ellipse)
button.setMask(region);


button1 = QLabel()
button1.setPixmap(QPixmap(os.getcwd() + "/suction.png"))
button1.setFixedHeight(100)

# Put the widgets in a layout:
layout = QGridLayout(window)
# layout.setColumnStretch(0, 1)
# layout.setColumnStretch(1, 1)
# layout.setColumnStretch(2, 1)
# layout.setRowStretch(0, 1)
# layout.setRowStretch(1, 1)
# layout.setRowStretch(2, 1)
# layout.setRowStretch(3, 1)
# layout.setRowStretch(4, 1)


layout.addWidget(leftBar, 2, 0, Qt.AlignCenter)
layout.addWidget(rightBar, 2, 2, Qt.AlignCenter)
layout.addWidget(picksPerHour, 0, 0, Qt.AlignCenter)
layout.addWidget(labelPicks, 1, 0, Qt.AlignCenter)
layout.addWidget(header, 0, 1, Qt.AlignCenter)
layout.addWidget(image, 2, 1, Qt.AlignCenter)
layout.addWidget(icons, 3, 1, Qt.AlignCenter)
layout.addWidget(weightDisplay, 3, 0, Qt.AlignCenter)
layout.addWidget(labelWeight, 4, 0, Qt.AlignCenter)
layout.addWidget(confidenceDisplay, 0, 2, Qt.AlignCenter)
layout.addWidget(labelConfidence, 1, 2, Qt.AlignCenter)
layout.addWidget(button, 4, 1)
layout.addWidget(button1, 4, 2)
rowLabel = layout.rowCount()
print(rowLabel)
sys.exit(app.exec_())