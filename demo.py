#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

import sys

if 'PyQt5' in sys.modules:
    # PyQt5
    from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QPushButton
    from PyQt5.QtCore import QTimer, QRect, Qt, Signal as pyqtSignal
    from PyQt5.QtGui import (QClipboard, QPainter, QFont, QBrush, QColor,
                            QPen, QPixmap, QImage, QContextMenuEvent)

else:
    # PySide2
    from PySide2.QtWidgets import QApplication, QWidget, QTabWidget, QPushButton
    from PySide2.QtCore import QTimer, QRect, Qt, Signal as pyqtSignal
    from PySide2.QtGui import (QClipboard, QPainter, QFont, QBrush, QColor,
                            QPen, QPixmap, QImage, QContextMenuEvent)

from py3qterm import TerminalWidget
from py3qterm.procinfo import ProcessInfo


class TabbedTerminal(QTabWidget):

    def __init__(self, parent=None):
        super(TabbedTerminal, self).__init__(parent)
        self.proc_info = ProcessInfo()
        self.setTabPosition(QTabWidget.South)
        # self._new_button = QPushButton(self)
        # self._new_button.setText("New")
        # self._new_button.clicked.connect(self.new_terminal)
        # self.setCornerWidget(self._new_button)
        # self.setTabsClosable(True)
        # self.setMovable(True)
        self.setWindowTitle("Terminal")
        self.resize(800, 600)
        self._terms = []
        self.tabCloseRequested[int].connect(self._on_close_request)
        self.currentChanged[int].connect(self._on_current_changed)
        QTimer.singleShot(0, self.new_terminal)  # create lazy on idle
        self.startTimer(100)

    def _on_close_request(self, idx):
        term = self.widget(idx)
        term.stop()

    def _on_current_changed(self, idx):
        term = self.widget(idx)
        self._update_title(term)

    def new_terminal(self):
        term = TerminalWidget(self)
        term.session_closed.connect(self._on_session_closed)
        self.addTab(term, "Terminal")
        self._terms.append(term)
        self.setCurrentWidget(term)
        term.setFocus()

    def timerEvent(self, event):
        self._update_title(self.currentWidget())

    def _update_title(self, term):
        if term is None:
            self.setWindowTitle("Terminal")
            return
        idx = self.indexOf(term)
        pid = term.pid()
        self.proc_info.update()
        child_pids = [pid] + self.proc_info.all_children(pid)
        for pid in reversed(child_pids):
            cwd = self.proc_info.cwd(pid)
            if cwd:
                break
        try:
            cmd = self.proc_info.commands[pid]
            title = "%s: %s" % (os.path.basename(cwd), cmd)
        except:
            title = "Terminal"
        self.setTabText(idx, title)
        self.setWindowTitle(title)

    def _on_session_closed(self):
        term = self.sender()
        try:
            self._terms.remove(term)
        except:
            pass
        self.removeTab(self.indexOf(term))
        widget = self.currentWidget()
        if widget:
            widget.setFocus()
        if self.count() == 0:
            self.new_terminal()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TabbedTerminal()
    win.show()
    app.exec_()
