from PySide6 import QtWidgets


def pdf_error(error):
    if error == OSError:
        message = "Вы не можете изменить pdf документ пока он "
        "открыт. Закройте документ"
    elif error == PermissionError:
        message = "Вы не можете закрыть приложение пока откры pdf " \
                  "документ. Закройте документ"
    error_dialog = QtWidgets.QMessageBox()
    error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
    error_dialog.setText("Открыт pdf документ")
    error_dialog.setInformativeText(message)
    error_dialog.setWindowTitle("Ошибка")
    error_dialog.exec()