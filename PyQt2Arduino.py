from PyQt5 import QtCore, QtWidgets, QtSerialPort, QtGui
from PyQt5.uic import loadUi
from time import sleep

import logging

class CustomLogging():

    def setup_custom_logger(self, logfile):
        formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
        handler = logging.FileHandler('PyQt2Arduino.log', mode='a')
        handler.setFormatter(formatter)
        screen_handler = logging.StreamHandler(stream=sys.stdout)
        screen_handler.setFormatter(formatter)
        logger = logging.getLogger(logfile)
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
        logger.addHandler(screen_handler)
        return logger

class Widget(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        loadUi('PyQt2ArduinoGUI/PyQt2Arduino-GUI.ui', self)

        # --------> LOG Settings <------- #
        self.log_lineEdit.setPlaceholderText(QtCore.QDir.currentPath() + 'PyQt2Arduiono.log')
        logfile = CustomLogging
        self.logger = logfile.setup_custom_logger(self, 'PyQt2Arduino')
        # ------------------------------- #

        # --> Port Open/Close command <-- #
        self.connect_btn.clicked.connect(self.connectToPort)
        self.disconnect_btn.clicked.connect(self.disconnectFromPort)
        # ------------------------------- #

        # --> Display command <-- #
        self.lcd_ConnBtn.clicked.connect(lambda: self.mode_con_discon("lcd"))
        self.lcd_DisconnBtn.clicked.connect(lambda: self.mode_con_discon("close"))
        self.lcd_SendBtn.clicked.connect(self.send)
        # ----------------------- #

        # --> Light command <-- #
        self.light_StartBtn.clicked.connect(lambda: self.mode_con_discon("light"))
        self.light_StopBtn.clicked.connect(lambda: self.mode_con_discon("close"))
        # --------------------- #

        # --> Temp  command <-- #
        self.temp_StartBtn.clicked.connect(lambda: self.mode_con_discon("temp"))
        self.temp_StopBtn.clicked.connect(lambda: self.mode_con_discon("close"))
        # --------------------- #

        # --> Temp  command <-- #
        self.start_sonar.clicked.connect(lambda: self.mode_con_discon("distance"))
        self.stop_sonar.clicked.connect(lambda: self.mode_con_discon("close"))
        # --------------------- #

        # --> List all ports <-- #
        for info in QtSerialPort.QSerialPortInfo.availablePorts():
            self.ports_comboBox.addItem(info.portName())
        # --------------------- #

        # --> List all baudrates <-- #
        for baudrate in QtSerialPort.QSerialPortInfo.standardBaudRates():
            self.baudrate_comboBox.addItem(str(baudrate), baudrate)
        # -------------------------- #

        # --> List all databits <-- #
        databits = [
            ('5', QtSerialPort.QSerialPort.Data5),
            ('6', QtSerialPort.QSerialPort.Data6),
            ('7', QtSerialPort.QSerialPort.Data7),
            ('8', QtSerialPort.QSerialPort.Data8)
        ]
        for text, databit in databits:
            self.databit_comboBox.addItem(text, databit)
        # -------------------------- #

        paritybits = [
            ('None', QtSerialPort.QSerialPort.NoParity),
            ('Even', QtSerialPort.QSerialPort.EvenParity),
            ('Odd', QtSerialPort.QSerialPort.OddParity),
            ('Mark', QtSerialPort.QSerialPort.MarkParity),
            ('Space', QtSerialPort.QSerialPort.SpaceParity)
        ]
        for text, paritybit in paritybits:
            self.paritybit_comboBox.addItem(text, paritybit)
        # -------------------------- #

        stopbits = [
            ('1', QtSerialPort.QSerialPort.OneStop),
            ('1.5', QtSerialPort.QSerialPort.OneAndHalfStop),
            ('2', QtSerialPort.QSerialPort.TwoStop)
        ]
        for text, stopbit in stopbits:
            self.stopbits_comboBox.addItem(text, stopbit)
        # -------------------------- #

        flowcontrol_list = [
            ('None', QtSerialPort.QSerialPort.NoFlowControl),
            ('Hardware', QtSerialPort.QSerialPort.FlowControl),
        ]
        for text, flowcontrol in flowcontrol_list:
            self.flowcontrol_comboBox.addItem(text, flowcontrol)
        # ------------------------------------ #

        self.clear_btn.clicked.connect(self.clearConsole)
        self.consoleSend_btn.clicked.connect(self.send)
        self.serial = QtSerialPort.QSerialPort(readyRead=self.receive)

    @QtCore.pyqtSlot()
    def clearConsole(self):
        self.readConsole.clear()

    @QtCore.pyqtSlot()
    def mode_con_discon(self, value):
        self.serial.write(value.encode())
        sleep(0.2)

    @QtCore.pyqtSlot()
    def receive(self):
        while self.serial.canReadLine():
            text = self.serial.readLine().data().decode()
            text = text.rstrip('\r\n')

            if text.startswith('Lux'):
                self.lux_label.setText(text)
            elif text.startswith('T:'):
                self.temp_label.setText(text)
            elif text.startswith('Distance:'):
                text = text.replace("Distance: ", "")
                text = int(text)
                self.ultrasonicSlider.setValue(text)
                self.ultrasonic_label.setText(str(text) + " cm")

            self.writeOnConsoleAndLog(str(text))

    @QtCore.pyqtSlot()
    def send(self):
        self.serial.write(self.lcd_lineEdit.text().encode())
        self.lcd_lineEdit.setText("")
        send_command = self.sendConsole.text()
        self.serial.write(send_command.encode())
        self.writeOnConsoleAndLog(send_command)
        self.sendConsole.setText("")



    @QtCore.pyqtSlot()
    def connectToPort(self):
        if self.default_checkBox.isChecked():
            self.serial.setPortName(self.ports_comboBox.currentText())
            self.serial.setBaudRate(QtSerialPort.QSerialPort.Baud9600)
            self.serial.setDataBits(QtSerialPort.QSerialPort.Data8)
            self.serial.setParity(QtSerialPort.QSerialPort.NoParity)
            self.serial.setStopBits(QtSerialPort.QSerialPort.OneStop)
            self.serial.setFlowControl(QtSerialPort.QSerialPort.NoFlowControl)
        else:
            self.serial.setPortName(self.ports_comboBox.currentText())
            self.serial.setBaudRate(self.baudrate_comboBox.currentData())
            self.serial.setDataBits(self.databit_comboBox.currentData())
            self.serial.setParity(self.paritybit_comboBox.currentData())
            self.serial.setStopBits(self.stopbits_comboBox.currentData())
            self.serial.setFlowControl(self.flowcontrol_comboBox.currentData())

        self.serial.open(QtCore.QIODevice.ReadWrite)

        if self.serial.isOpen():
            QtWidgets.QMessageBox.information(self, "Connect", "Connected!")
            self.writeOnConsoleAndLog("Connected!")
            self.writeOnConsoleAndLog("PORT: " + str(self.serial.portName()))
            self.writeOnConsoleAndLog("BAUDRATE: " + str(self.serial.baudRate()))
            self.writeOnConsoleAndLog("DATABITS: " + str(self.serial.dataBits()))
            self.writeOnConsoleAndLog("PARITY: " + str(self.serial.parity()))
            self.writeOnConsoleAndLog("STOPBITS: " + str(self.serial.stopBits()))
            self.writeOnConsoleAndLog("FLOWCONTROL: " + str(self.serial.flowControl()))

        else:
            QtWidgets.QMessageBox.critical(self, "Connect", "Can not establish a connection")
            self.writeOnConsoleAndLog("Can not establish a connection")


    @QtCore.pyqtSlot()
    def disconnectFromPort(self):
        self.serial.close()
        QtWidgets.QMessageBox.information(self, "Disconnect", "Disconnected!")
        self.writeOnConsoleAndLog("Disconnected!")

    def writeOnConsoleAndLog(self, command):
        self.logger.info(command)
        self.readConsole.moveCursor(QtGui.QTextCursor.End)
        self.readConsole.insertPlainText(command + '\n')


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())