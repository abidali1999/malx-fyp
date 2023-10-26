from PyQt5 import QtCore, QtGui, QtWidgets


class PushButton(QtWidgets.QPushButton):
    def __init__(self, parent=None,enable_border=False):
        self.border='2px solid black' if enable_border else 'none'
        super().__init__(parent)
        self._animation = QtCore.QVariantAnimation(
            startValue=QtGui.QColor("#4CAF50"),
            endValue=QtGui.QColor("#EEEEEE"),
            valueChanged=self._on_value_changed,
            duration=400,
        )
        self._update_stylesheet(QtGui.QColor("#EEEEEE"), QtGui.QColor("black"))
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def _on_value_changed(self, color):
        foreground = (
            QtGui.QColor("black")
            if self._animation.direction() == QtCore.QAbstractAnimation.Forward
            else QtGui.QColor("#EEEEEE")
        )
        self._update_stylesheet(color, foreground)

    def _update_stylesheet(self, background, foreground):

        self.setStyleSheet(
            """
        QPushButton{
            background-color: %s;
            border: none;
            color: %s;
            text-align: center;
            border: %s;
            font-size:14px;
            font-weight:bold;
            line-height:40px;
            text-align:center;
            
        }
        """
            % (background.name(), foreground.name(),self.border)
        )
            # border: 2px solid #4CAF50;
            # padding: 16px 32px;
# 
# font-size: 16px;
            # margin: 4px 2px;
# 
    def enterEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Forward)
        self._animation.start()
        super().leaveEvent(event)