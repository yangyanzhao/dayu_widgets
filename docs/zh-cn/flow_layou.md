![zms1.gif](zms1.gif)
## 简介
`MFlowLayout` 是一个自定义的布局管理器，用于实现流式布局。它可以自动将控件水平排列，并根据需要自动换行。这种布局方式非常适合于需要动态调整布局的应用场景，例如文件浏览器或网格视图。
******
## 初始化
  - `layout = MFlowLayout()`
********
## 控件间距
  - `layout.setSpacing(30)`
******
## 清空布局
  - `layout.clear()`
******
## 添加控件
  - `layout.addWidget(widget)`
  - `layout.insertWidget(index, widget)`
******
## 移除控件
  - `layout.takeAt(index)`
******
## 获取控件数量
  - `layout.count()`
******
## 获取指定位置的控件
  - `layout.itemAt(index)`
******
## 示例代码

```python
import asyncio
from PySide2.QtWidgets import QWidget, QApplication
from dayu_widgets.qt import MIcon
from qasync import QEventLoop
from dayu_widgets import MTheme, MFlowLayout, MPushButton
class DemoWidget(QWidget):
    def __init__(self, parent=None):
        super(DemoWidget, self).__init__(parent)
        layout = MFlowLayout()
        self.setLayout(layout)
        for i in range(10):
            self.layout().addWidget(MPushButton(icon=MIcon("add_line.svg")))
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
