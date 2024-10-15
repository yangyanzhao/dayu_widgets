import asyncio
from PySide2.QtCore import QTime
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout
from qasync import QEventLoop
from dayu_widgets import MTheme, MFieldMixin, MTimeEdit


class DemoWidget(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(DemoWidget, self).__init__(parent)
        self.setWindowTitle("MPushButton控件学习")
        # 布局
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        time_edit = MTimeEdit(time=QTime.currentTime()).large()
        time_edit.setTimeRange(QTime(10, 10, 10, 10), QTime(10, 10, 10, 10))
        time_edit.setTime(QTime(10, 10, 10, 10))
        time_edit.setDisplayFormat("HH:mm:ss")
        self.main_layout.addWidget(time_edit)
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
