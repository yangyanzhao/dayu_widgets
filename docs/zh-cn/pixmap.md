## 简介
`MPixmap` 是一个用于高效管理和处理 `QPixmap` 对象的类，特别适合于需要频繁加载、缩放和缓存图片的应用场景。通过缓存机制，减少重复加载相同图片的开销，提高应用性能。******
## 基础使用
  - `MPixmap("success_line.svg")`![img_40.png](img_40.png)
********
## 自定义颜色
  - `MPixmap("success_line.svg", dayu_theme.success_color)`![img_41.png](img_41.png)
  - `MPixmap("success_line.svg", '#FFc41a')`![img_42.png](img_42.png)
******
## 示例代码

```python
import asyncio
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLabel
from dayu_widgets.qt import MPixmap
from qasync import QEventLoop
from dayu_widgets import MTheme, dayu_theme
class DemoWidget(QWidget):
    def __init__(self, parent=None):
        super(DemoWidget, self).__init__(parent)
        self.setWindowTitle("MPushButton控件学习")
        # 布局
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.sub_layout_1 = QHBoxLayout()
        self.main_layout.addLayout(self.sub_layout_1)
        label1 = QLabel()
        label2 = QLabel()
        label3 = QLabel()
        label1.setPixmap(MPixmap("success_line.svg"))
        label2.setPixmap(MPixmap("success_line.svg", dayu_theme.success_color))
        label3.setPixmap(MPixmap("success_line.svg", '#FFc41a'))
        self.sub_layout_1.addWidget(label1)
        self.sub_layout_1.addWidget(label2)
        self.sub_layout_1.addWidget(label3)
        self.sub_layout_1.addStretch()
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
