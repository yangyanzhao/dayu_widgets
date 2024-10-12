import asyncio
from PySide2.QtWidgets import QWidget, QApplication
from dayu_widgets.qt import MIcon
from qasync import QEventLoop
from dayu_widgets import MTheme, MFlowLayout, MPushButton
class DemoWidget(QWidget):
    def __init__(self, parent=None):
        super(DemoWidget, self).__init__(parent)
        layout = MFlowLayout()
        self.setLayout(layout)
        for i in range(10):
            self.layout().addWidget(MPushButton(icon=MIcon("add_line.svg")))
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
