import asyncio
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout
from dayu_widgets.qt import MPixmap
from qasync import QEventLoop
from dayu_widgets import MTheme, MFieldMixin, MCard, MLabel, dayu_theme, MMeta


class DemoWidget(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(DemoWidget, self).__init__(parent)
        # 布局
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        for i in range(10):
            meta_card = MMeta(extra=True)
            meta_card.setup_data({
                "title": f"Task {i}",
                "description": "demo pl_0010 Animation \n2019/04/01 - 2019/04/09",
                "avatar": MPixmap("success_line.svg", dayu_theme.success_color),
            })
            self.main_layout.addWidget(meta_card)


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
