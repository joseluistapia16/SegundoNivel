import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QGridLayout,
                             QPushButton, QMessageBox)
from PyQt6.QtGui import QFont


class Formulario(QWidget):
    def __init__(self):
        super().__init__()
        self.start()

    def start(self):
        self.setWindowTitle('Formulario Elegante PyQt6')
        self.resize(300, 150)
        font = QFont('Arial', 12)
        lblName = QLabel("Nombre:")
        lblName.setFont(font)
        self.txtName = QLineEdit()
        self.txtName.setPlaceholderText("Nombre de usuario")

        lblPass = QLabel("Contraseña:")
        lblPass.setFont(font)
        self.txtPass = QLineEdit()
        self.txtPass.setPlaceholderText("Contraseña de usuario")
        self.txtPass.setEchoMode(QLineEdit.EchoMode.Password)

        btnSave = QPushButton("Guardar")
        btnSave.setFont(font)
        btnSave.clicked.connect(self.guardarDatos)

        btnExit = QPushButton("Salir")
        btnExit.setFont(font)
        btnExit.clicked.connect(self.salir)

        grid = QGridLayout()
        grid.addWidget(lblName, 0, 0)
        grid.addWidget(self.txtName, 0, 1)
        grid.addWidget(lblPass, 1, 0)
        grid.addWidget(self.txtPass, 1, 1)
        grid.addWidget(btnSave, 2, 0)
        grid.addWidget(btnExit, 2, 1)
        self.setLayout(grid)

    def guardarDatos(self):
        # Aquí puedes añadir la lógica para guardar los datos
        QMessageBox.information(self, "Información", "Datos guardados", QMessageBox.StandardButton.Ok)

    def salir(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    formulario = Formulario()
    formulario.show()
    sys.exit(app.exec())
