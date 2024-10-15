## 简介
`MSlider` 类继承自 `QSlider`，用于创建一个带有当前值显示功能的滑块组件。当用户移动滑块时，会在鼠标位置显示当前值的工具提示。
******
## 初始化
  - `slider = MSlider(orientation=QtCore.Qt.Horizontal)`
    - `orientation`: 布局方向，默认为水平方向 `QtCore.Qt.Horizontal`。
********
## 设置范围
  - `slider.setRange(-100, 100)`
******
## 设置值
  - `slider.setValue(-80)`
******
## 禁用工具提示显示
  - `slider.disable_show_text()`
******
## 双向绑定
  - ```python
    slider = MSlider(orientation=Qt.Horizontal)
    slider.setRange(-100, 100)
    self.register_field("slider", -50)
    # 双向绑定
    self.bind(data_name="slider", widget=slider, qt_property="value", signal="valueChanged", callback=None)
    # 绑定一个计算属性来显示当前值
    label = MLabel(text=str(slider.value()))
    self.register_field("label", getter=functools.partial(lambda: slider.value()))
    self.bind(data_name="label", widget=label, qt_property="text")
******
## 示例代码

```python
import asyncio
import functools
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout
from qasync import QEventLoop
from dayu_widgets import MTheme, MSlider, MFieldMixin, MLabel
class DemoWidget(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(DemoWidget, self).__init__(parent)
        self.setWindowTitle("MPushButton控件学习")
        # 布局
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        slider = MSlider(orientation=Qt.Horizontal)
        slider.setRange(-100, 100)
        self.register_field("slider", -50)
        # 双向绑定
        self.bind(data_name="slider", widget=slider, qt_property="value", signal="valueChanged", callback=None)
        # 绑定一个计算属性来显示当前值
        label = MLabel(text=str(slider.value()))
        self.register_field("label", getter=functools.partial(lambda: slider.value()))
        self.bind(data_name="label", widget=label, qt_property="text")
        self.main_layout.addWidget(slider)
        self.main_layout.addWidget(label)
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
