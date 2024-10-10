# 学习笔记 MLoading控件
import asyncio
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QTextEdit
from qasync import QEventLoop, asyncSlot

from dayu_widgets import dayu_theme, MLoadingWrapper, MTheme


class DemoWidget(QWidget):
    def __init__(self, parent=None):
        super(DemoWidget, self).__init__(parent)
        self.setWindowTitle("MLoading控件学习")
        # 布局
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # 添加一个查询按钮
        self.button = QPushButton("查询数据", self)
        self.button.clicked.connect(self.btn_handle)
        self.main_layout.addWidget(self.button)

        # 添加一个文本框用来显示加载的数据
        self.text_edit = QTextEdit(self)
        self.main_layout.addWidget(self.text_edit)

        # 这里要为显示的控件添加一个loading的wrapper，并且要添加到布局中！
        self.loading_wrapper = MLoadingWrapper(widget=self.text_edit, loading=False, size=64, color=dayu_theme.red)
        self.main_layout.addWidget(self.loading_wrapper)

    @asyncSlot()
    async def btn_handle(self):
        # 开启加载
        self.loading_wrapper.set_dayu_loading(True)
        # 模拟查询耗时2秒
        await asyncio.sleep(2)
        # 结束加载
        self.loading_wrapper.set_dayu_loading(False)
        # 渲染数据
        self.text_edit.setText(
            "陌生人并不在意你的梦想是什么，"
            "他们寻求满足自己的需要和欲望。"
            "在你介入没有明确需求、品牌或目的的生意时，"
            "风险将会累积。"
            "当你去做一项自己喜欢而不是需要去做的生意时，风险在累积。" * 2)


if __name__ == '__main__':
    # 创建主循环
    app = QApplication([])

    # 创建异步事件循环
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    # 创建窗口
    demo_widget = DemoWidget()
    MTheme(theme="light", primary_color=MTheme.yellow).apply(demo_widget)
    # 显示窗口
    demo_widget.show()
    loop.run_forever()
