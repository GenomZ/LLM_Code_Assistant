import sys
import requests
import threading
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit

# Assuming your Flask app is correctly set up for threading as discussed previously
from flask_app.app import run_flask_app

class LLMGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.initUI()
        # Start the Flask app in a background thread
        self.flaskThread = threading.Thread(target=run_flask_app, daemon=True)
        self.flaskThread.start()

    def initUI(self):
        self.setWindowTitle('Code Assistant - KB v0.0.1')
        self.setGeometry(100, 100, 600, 400)

        # Input TextEdit
        self.inputTextEdit = QTextEdit(self)
        self.inputTextEdit.setPlaceholderText("Enter your prompt here...")
        self.layout.addWidget(self.inputTextEdit)

        # Button for getting suggestion
        self.btnModelNeoGPT = QPushButton('Get Suggestion from Neo-GPT-125M', self)
        self.btnModelNeoGPT.clicked.connect(lambda: self.getSuggestion("gptneo"))
        self.layout.addWidget(self.btnModelNeoGPT)

        self.btnModelCodeGen = QPushButton('Get Suggestion from CodeGen-350M', self)
        self.btnModelCodeGen.clicked.connect(lambda: self.getSuggestion("codegen"))
        self.layout.addWidget(self.btnModelCodeGen)

        self.btnModelCodeLlama = QPushButton('Get Suggestion from CodeLlama-7b-hf', self)
        self.btnModelCodeLlama.clicked.connect(lambda: self.getSuggestion("codellama"))
        self.layout.addWidget(self.btnModelCodeLlama)

        # Output TextEdit
        self.outputTextEdit = QTextEdit(self)
        self.outputTextEdit.setPlaceholderText("Output will appear here...")
        self.outputTextEdit.setReadOnly(True)  # Make output read-only
        self.layout.addWidget(self.outputTextEdit)

        self.setLayout(self.layout)

    def getSuggestion(self, model):
        prompt = self.inputTextEdit.toPlainText()
        # Here, replace 'your_endpoint_url' with the actual URL of your Flask endpoint
        response = requests.post(f'http://localhost:5000/{model}', json={'prompt': prompt})
        if response.status_code == 200:
            suggestion = response.json()['suggestion']
            self.outputTextEdit.setText(suggestion)
        else:
            self.outputTextEdit.setText('Error getting suggestion')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LLMGUI()
    ex.show()
    sys.exit(app.exec())