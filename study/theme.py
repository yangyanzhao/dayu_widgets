import sys
from PySide2.QtWidgets import QPushButton, QWidget, QApplication, QVBoxLayout
from dayu_widgets import MTheme

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建窗口
    window = QWidget()
    # 初始化主题
    theme = MTheme(theme="light", primary_color=MTheme.blue)
    # 应用主题样式
    theme.apply(window)
    # 设置布局
    layout = QVBoxLayout(window)
    button = QPushButton("Click Me")
    layout.addWidget(button)
    # 显示窗口
    window.show()
    sys.exit(app.exec_())
