## 简介
`MIcon` 是一个用于高效加载和管理图标的工具类，支持 SVG 和其他常见图标格式。通过缓存机制减少重复加载相同图标时的性能开销，并且可以自定义图标的颜色。
******
## 基础图标
  - `MIcon('icon.svg')`![img_12.png](img_12.png)
********
## 自定义颜色
  - `MIcon('icon.svg', color='#FF0000')`![img_13.png](img_13.png)
******
## 自定义图标
  - [阿里巴巴适量图标库](https://www.iconfont.cn/)
  - 下载后，为了使颜色能够动态受控，需要将颜色设置为`#555555`。
    - ![img_136.png](img_136.png)
  - 如果是已经下载好的svg文件，直接修改文件即可，设置`fill="#555555"`。
    - ![img_137.png](img_137.png)
## 显示图标
- 如果只需要显示图标而不需要自定义大小，可以直接使用 QIcon 配合 QPushButton 或 QAction 等来显示图标。
```python
button = QPushButton()
button.setIcon(MIcon("cloud_fill.svg"))
```
## 配合QLabel显示图标
```python
self.label = QLabel(self)
self.label.setPixmap(pixmap)
```
## 独立显示图标
```python
svg_widget = QSvgWidget(icons['操作成功.svg'])
svg_widget.setFixedSize(QSize(32, 32))
```
## 示例代码

```python
import asyncio
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton
from dayu_widgets.qt import MIcon
from qasync import QEventLoop
from dayu_widgets import MTheme
class DemoWidget(QWidget):
    def __init__(self, parent=None):
        super(DemoWidget, self).__init__(parent)
        layout = QVBoxLayout(self)
        self.setLayout(layout)
        button1 = QPushButton()
        button2 = QPushButton()
        button1.setIcon(MIcon("cloud_fill.svg"))
        button2.setIcon(MIcon(path="cloud_fill.svg", color="red"))
        self.layout().addWidget(button1)
        self.layout().addWidget(button2)
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
