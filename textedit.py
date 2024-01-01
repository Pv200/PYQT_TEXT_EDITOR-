import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        
        self.init_ui()

    def init_ui(self):
        
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

       
        menubar = self.menuBar()

        
        file_menu = menubar.addMenu('File')

        
        open_action = QAction('Open', self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        
        save_action = QAction('Save', self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        
        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Simple Text Editor')
        self.show()

    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Text File", "", "Text Files (*.txt);;All Files (*)", options=options)
        #CONCEPT OF FILE HANDLING
        if file_name:
            with open(file_name, 'r') as file:
                content = file.read()
                self.text_edit.setPlainText(content)

    def save_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Text File", "", "Text Files (*.txt);;All Files (*)", options=options)

        if file_name:
            with open(file_name, 'w') as file:
                content = self.text_edit.toPlainText()
                file.write(content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = TextEditor()
    sys.exit(app.exec_())
