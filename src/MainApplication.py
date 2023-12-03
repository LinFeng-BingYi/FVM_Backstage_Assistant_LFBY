#!/usr/bin/env python3

from PySide6.QtWidgets import QApplication

from src.AppImplement.FormFiles.EditCardPlacingConfigForm import WidgetEditCardPlacingConfig


if __name__ == '__main__':
    app = QApplication([])
    myMainWindow = WidgetEditCardPlacingConfig()
    myMainWindow.show()
    app.exec()
