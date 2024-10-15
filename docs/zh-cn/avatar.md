## 简介
`MAvatar` 类继承自 `QLabel`，用于创建一个带有大小属性的头像组件。
![img_87.png](img_87.png)
******
## 初始化
  - `avatar = MAvatar()`
********
## 设置头像
  - `avatar.set_dayu_image(MPixmap("app-nuke.png"))`
******
## 设置控件大小
  - `avatar.huge()  # 设置为巨大尺寸`
  - `avatar.large()  # 设置为大尺寸`
  - `avatar.medium()  # 设置为中尺寸`
  - `avatar.small()  # 设置为小尺寸`
  - `avatar.tiny()  # 设置为微小尺寸`
******
## 双向绑定
  - ```python
    avatar = MAvatar()
    avatar.set_dayu_image(MPixmap("app-nuke.png"))
    self.main_layout.addWidget(avatar)
    # 双向绑定数据
    self.register_field("image", None)
    self.bind("image", avatar, "dayu_image")
    # 弄个按钮来切换头像
    button = MPushButton(text="Change Avatar Image").primary()
    button.clicked.connect(functools.partial(lambda: self.set_field("image", random.choice([None, MPixmap("app-nuke.png"),MPixmap("close_line.png"),MPixmap("float.png")]))))
    self.main_layout.addWidget(button)
******
## 示例代码

```python
import asyncio
import functools
import random
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout
from dayu_widgets.qt import MPixmap
from qasync import QEventLoop
from dayu_widgets import MTheme, MFieldMixin, MAvatar, MPushButton
class DemoWidget(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(DemoWidget, self).__init__(parent)
        self.setWindowTitle("MPushButton控件学习")
        # 布局
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        avatar = MAvatar()
        avatar.set_dayu_image(MPixmap("app-nuke.png"))
        self.main_layout.addWidget(avatar)
        # 双向绑定数据
        self.register_field("image", None)
        self.bind("image", avatar, "dayu_image")
        # 弄个按钮来切换头像
        button = MPushButton(text="Change Avatar Image").primary()
        button.clicked.connect(functools.partial(lambda: self.set_field("image", random.choice([None, MPixmap("app-nuke.png"),MPixmap("close_line.png"),MPixmap("float.png")]))))
        self.main_layout.addWidget(button)
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