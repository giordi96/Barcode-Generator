#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication
from gui import BGGui

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = BGGui()
    gui.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print("Closing Window")
