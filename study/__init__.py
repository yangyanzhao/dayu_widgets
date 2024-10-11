import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout
from dayu_widgets import MTheme, MPushButton

if __name__ == '__main__':
    # 创建主循环
    app = QApplication([])

    # 创建窗口
    widget = QWidget()
    # 设置主题
    MTheme().apply(widget)
    # 窗口布局
    layout = QVBoxLayout(widget)
    # 使用控件
    button = MPushButton("默认按钮").primary()
    layout.addWidget(button)
    # 显示窗口
    widget.show()

    sys.exit(app.exec_())
