import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PySide6.QtCore import QUrl, QByteArray, Qt
from PySide6.QtGui import QTextCursor

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Code Completion GUI")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.prompt_label = QLabel("Enter Prompt:")
        layout.addWidget(self.prompt_label)

        self.prompt_input = QLineEdit()
        layout.addWidget(self.prompt_input)

        self.submit_button = QPushButton("Get Completions")
        self.submit_button.clicked.connect(self.get_completions)
        layout.addWidget(self.submit_button)

        self.completions_label = QLabel("Completions:")
        layout.addWidget(self.completions_label)

        self.completions_output = QLabel()
        self.completions_output.setWordWrap(True)
        layout.addWidget(self.completions_output)

        self.setLayout(layout)

        self.network_manager = QNetworkAccessManager()
        self.network_manager.finished.connect(self.handle_response)

    def get_completions(self):
        prompt = self.prompt_input.text()

        if prompt:
            url = QUrl("http://localhost:5000/complete")
            request = QNetworkRequest(url)
            request.setHeader(QNetworkRequest.ContentTypeHeader, "application/x-www-form-urlencoded")

            data = QByteArray()
            data.append(f"prompt={prompt}")

            self.network_manager.post(request, data)

    def handle_response(self, reply):
        if reply.error() == QNetworkAccessManager.NoError:
            content = reply.readAll().data().decode()
            self.completions_output.setText(content)
        else:
            self.completions_output.setText("Error: Unable to fetch completions")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())