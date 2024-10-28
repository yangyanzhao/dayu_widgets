import asyncio
from PySide2 import QtCore
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout
from qasync import QEventLoop
from dayu_widgets import MTheme, MMenuTabWidget, dayu_theme, MLabel
class DemoWidget(QWidget):
    def __init__(self, parent=None):
        super(DemoWidget, self).__init__(parent)
        layout = QVBoxLayout()
        self.setLayout(layout)
        menu_tab_widget = MMenuTabWidget(orientation=QtCore.Qt.Horizontal)  # orientation导航组件方向
        data_dict = {
            "text": "Home",
            "svg": "home_line.svg",
            "tooltip": "Go to home page",
            "clicked": lambda: print("Home"),
            "children": [
                {
                    "text": "Home",
                    "svg": "home_line.svg",
                    "tooltip": "Go to home page",
                    "clicked": lambda: print("Home"),
                }
            ],
        }
        # 添加导航菜单项及其ID
        menu_tab_widget.add_menu(data_dict, 0)
        menu_tab_widget.add_menu(data_dict, 1)
        # 设置菜单大小
        menu_tab_widget.set_dayu_size(dayu_theme.medium)
        layout.addWidget(menu_tab_widget)
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
