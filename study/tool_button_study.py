import asyncio
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout
from qasync import QEventLoop
from dayu_widgets import MTheme, MToolButton
class DemoWidget(QWidget):
    def __init__(self, parent=None):
        super(DemoWidget, self).__init__(parent)
        # 布局
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.sub_layout_1 = QHBoxLayout()
        self.main_layout.addLayout(self.sub_layout_1)
        # 设置图标
        tool_button = MToolButton()
        self.sub_layout_1.addWidget(tool_button.svg("add_line.svg"))
        # 设置大小
        tool_button2 = MToolButton().large()
        tool_button2.setText("注册")
        self.sub_layout_1.addWidget(tool_button2)
        # 设置大小
        tool_button1 = MToolButton().svg("add_line.svg").large()
        self.sub_layout_1.addWidget(tool_button1)
        # 设置文字
        button_login = MToolButton().svg("user_line.svg")
        button_login.setText("Login")
        # 设置样式
        button_login.text_beside_icon()
        # 按钮提示
        button_login.setToolTip("登录")
        self.sub_layout_1.addWidget(button_login)
        # 启用/禁用
        tool_button3 = MToolButton().svg("add_line.svg").large()
        tool_button3.setEnabled(False)
        self.sub_layout_1.addWidget(tool_button3)
        # 设置可选
        tool_button4 = MToolButton().svg("add_line.svg").large()
        tool_button4.setCheckable(True)
        self.sub_layout_1.addWidget(tool_button4)
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
