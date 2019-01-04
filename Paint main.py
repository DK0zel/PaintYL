from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction, QFileDialog
from PyQt5.QtGui import QIcon, QImage, QPainter
from PyQt5.QtCore import Qt, QPoint
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        top = 800
        left = 800
        width = 800
        height = 800
        
        icon = "icons/pain.png"
        
        self.setWindowTitle("Приложение Пейнт")
        self.setGeometry(top, left, width, height)
        self.setWindowIcon(QIcon(icon))
        
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        
        self.drawing = false
        self.brushSize = 2
        self.bC = Qt.black
        
        self.lastPoint = QPoint()
        
        mM = self.menuBar()
        fM = mM.addMenu("Файл")
        bM = mM.addMenu("Размер Кисти")
        bC = mM.addMenu("Цвет Кисти")
        cC = mM.addMenu("Цвет Холста")
        fiM = mM.addMenu("Фигуры")
        
        saveAction = QAction(QIcon("icons/save.png"), "Сохранить", self)
        saveAction.setShortcut("Ctrl+S")
        fM.addAction(saveAction)
        saveAction.triggered.connect(self.save)
        clearAction = QAction(QIcon("icons/save.png"), "Очистить", self)
        clearAction.setShortcut("Ctrl+C")
        fM.addAction(clearAction)
        clearAction.triggered.connect(self.clear)
        circleAction = QAction("Круг", self)
        fiM.addAction(circleAction)
        circleAction.triggered.connect(self.circle)
        rectAction = QAction("Квадрат", self)
        fiM.addAction(rectAction)
        rectAction.triggered.connect(self.rect)
        
        threeAction = QAction(QIcon("icons/threepx.png"), "3 пикс.", self)
        bM.addAction(threeAction)
        threeeAction.triggered.connect(self.three)
        fourAction = QAction(QIcon("icons/fourpx.png"), "4 пикс.", self)
        bM.addAction(fourAction)
        fourAction.triggered.connect(self.four)
        fiveAction = QAction(QIcon("icons/fivepx.png"), "5 пикс.", self)
        bM.addAction(fiveAction)
        fiveAction.triggered.connect(self.five)
        sevenAction = QAction(QIcon("icons/sevenpx.png"), "7 пикс.", self)
        bM.addAction(sevenAction)
        sevenAction.triggered.connect(self.seven)
        nineAction = QAction(QIcon("icons/ninepx.png"), "9 пикс.", self)
        bM.addAction(nineAction)
        nineAction.triggered.connect(self.nine)
        elevenAction = QAction(QIcon("icons/elevenpx.png"), "11 пикс.", self)
        bM.addAction(elevenAction)
        elevenAction.triggered.connect(self.eleven)
        
        blackAction = QAction(QIcon("icons/black.png"), "Чёрный", self)
        blackAction.setShortcut("Ctrl+B")
        bC.addAction(blackAction)
        blackAction.triggered.connect(self.black)
        whiteAction = QAction(QIcon("icons/white.png"), "Белый", self)
        whiteAction.setShortcut("Ctrl+W")
        bC.addAction(whiteAction)
        whiteAction.triggered.connect(self.white)
        redAction = QAction(QIcon("icons/red.png"), "Крассный", self)
        redAction.setShortcut("Ctrl+R")
        bC.addAction(redAction)
        redAction.triggered.connect(self.red)
        greenAction = QAction(QIcon("icons/green.png"), "Зелёный", self)
        greenAction.setShortcut("Ctrl+G")
        bC.addAction(greenAction)
        greenAction.triggered.connect(self.green)        
        blueAction = QAction(QIcon("icons/blue.png"), "Синий", self)
        blueAction.setShortcut("Ctrl+K")
        bC.addAction(blueAction)
        blueAction.triggered.connect(self.blue)        
        yellowAction = QAction(QIcon("icons/yellow.png"), "Жёлтый", self)
        yellowAction.setShortcut("Ctrl+Y")
        bC.addAction(yellowAction)
        yellowAction.triggered.connect(self.yellow)
        
        blackAct = QAction(QIcon("icons/black.png"), "Чёрный", self)
        cC.addAction(blackAct)
        blackAct.triggered.connect(self.blackc)
        redAct = QAction(QIcon("icons/red.png"), "Крассный", self)
        cC.addAction(redAct)
        redAct.triggered.connect(self.redc)
        greenAct = QAction(QIcon("icons/green.png"), "Зелёный", self)
        cC.addAction(greenAct)
        greenAct.triggered.connect(self.greenc)        
        blueAct = QAction(QIcon("icons/blue.png"), "Синий", self)
        cC.addAction(blueAct)
        blueAct.triggered.connect(self.blue)        
        yellowAct = QAction(QIcon("icons/yellow.png"), "Жёлтый", self)
        cC.addAction(yellowAct)
        yellowAct.triggered.connect(self.yellowc)
        
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint =  event.pos()
    
    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton and self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.bC, self.brushSize, Qt.Solidline, QtRoundCap, RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()
            
    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False
            
    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())
        
    def save(self):
        filePath, = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "PNG(*.png);;JPEG(*.jpg *jpeg);;")
        if filePath == "":
            return
        self.image.save(filePath)
        
    def clear(self):
        self.image.fill(Qt.white)
        self.update()
        
    def three(self):
        self.brushSize = 3
        
    def four(self):
        self.brushSize = 4
        
    def five(self):
        self.brushSize = 5
        
    def seven(self):
        self.brushSize = 7
        
    def nine(self):
        self.brushSize = 9
        
    def eleven(self):
        self.brushSize = 11
    
    def black(self):
        self.bC = Qt.black
    
    def white(self):
        self.bC = Qt.white
        
    def red(self):
        self.bC = Qt.red
    
    def green(self):
        self.bC = Qt.green
    
    def blue(self):
        self.bC = Qt.blue
    
    def yellow(self):
        self.bC = Qt.yellow
        
    def blackc(self):
        self.image.fill(Qt.black)
        self.update()
        
    def redc(self):
        self.image.fill(Qt.red)
        self.update()
    
    def greenc(self):
        self.image.fill(Qt.green)
        self.update()
    
    def bluec(self):
        self.image.fill(Qt.blue)
        self.update()
    
    def yellowc(self):
        self.image.fill(Qt.yellow)
        self.update()
    
    def circle(self):
        center = self.lastPoint
        painter.drawEllipse(center, 100, 100) 
        
    def rect(self):
        painter.drawRect(self.lastPoint , 90, 90)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()