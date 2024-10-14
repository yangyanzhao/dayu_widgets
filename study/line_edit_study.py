import asyncio
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLineEdit
from dayu_widgets.qt import MIcon
from qasync import QEventLoop
from dayu_widgets import MTheme, MLineEdit, dayu_theme


class DemoWidget(QWidget):
    def __init__(self, parent=None):
        super(DemoWidget, self).__init__(parent)
        layout = QVBoxLayout(self)
        self.setLayout(layout)
        line_edit = MLineEdit().medium()
        line_edit.set_delay_duration(2000)
        layout.addWidget(line_edit)


if __name__ == '__main__':
    # 创建主循环
    app = QApplication([])

    # 创建异步事件循环
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    # 创建窗口
    demo_widget = DemoWidget()
    MTheme().apply(demo_widget)
    # 显示窗口
    demo_widget.show()

    loop.run_forever()
