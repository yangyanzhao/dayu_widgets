import asyncio

from PySide2 import QtCore
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout
from dayu_widgets.qt import MIcon
from qasync import QEventLoop
from dayu_widgets import MTheme, MPage, MCheckBox


class DemoWidget(QWidget):
    def __init__(self, parent=None):
        super(DemoWidget, self).__init__(parent)
        layout = QVBoxLayout()
        self.setLayout(layout)
        check_box1 = MCheckBox("A")
        # 设置为选中状态
        check_box1.setChecked(True)
        # 设置三态模式
        check_box1.setTristate(True)
        check_box2 = MCheckBox("B")
        # 设置为选中状态
        check_box2.setCheckState(QtCore.Qt.Checked)
        check_box3 = MCheckBox("C")
        # 设置为未选中状态
        check_box3.setCheckState(QtCore.Qt.Unchecked)
        check_box4 = MCheckBox("D")
        # 设置为半选中状态
        check_box4.setCheckState(QtCore.Qt.PartiallyChecked)
        check_box5 = MCheckBox("E")
        # 禁用复选框
        check_box5.setEnabled(False)
        check_box6 = MCheckBox("F")
        check_box6.setIcon(MIcon("app-maya.png"))
        layout.addWidget(check_box1)
        layout.addWidget(check_box2)
        layout.addWidget(check_box3)
        layout.addWidget(check_box4)
        layout.addWidget(check_box5)
        layout.addWidget(check_box6)


if __name__ == '__main__':
    # 创建主循环
    app = QApplication([])
    # 创建异步事件循环
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    # 创建窗口
    demo_widget = DemoWidget()
    MTheme("dark").apply(demo_widget)
    # 显示窗口
    demo_widget.show()
    loop.run_forever()
