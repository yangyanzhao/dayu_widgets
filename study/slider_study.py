import asyncio
import functools
import random
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout
from dayu_widgets.qt import MPixmap
from qasync import QEventLoop
from dayu_widgets import MTheme, MFieldMixin, MAvatar, MPushButton, MBadge, MLabel, MToolButton, MComboBox, MMenu


class DemoWidget(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(DemoWidget, self).__init__(parent)
        # 布局
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # 创建一个 MComboBox 实例
        combo_box = MComboBox()
        cities = ["北京", "上海", "广州", "深圳"]
        menu = MMenu(parent=self, exclusive=False)
        menu.set_data(cities)
        combo_box.set_menu(menu)
        # 添加选项
        self.main_layout.addWidget(combo_box)


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
