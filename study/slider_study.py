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

        combo_box = MComboBox()
        cities = ["上海", "北京", "深圳", "重庆", "广州", '成都', '天津', '武汉', '东莞', '西安', '杭州', '佛山',
                  '南京', '沈阳', '青岛', '济南', '长沙', '哈尔滨', '郑州', '昆明', '大连']
        combo_box.addItems(cities)
        combo_box.setProperty("searchable", True)
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
