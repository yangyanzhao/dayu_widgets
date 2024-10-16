## 简介
`MRadioButtonGroup` 用于创建一组互斥的单选按钮。当某个按钮被选中时，会触发 sig_checked_changed 信号。

![img_94.png](img_94.png)
******
## 初始化
  - `radio_button_group=MRadioButtonGroup(orientation=QtCore.Qt.Horizontal)`
    - `orientation`: 布局方向，默认为水平方向 `QtCore.Qt.Horizontal`。
********
## 设置选项
  - `radio_button_group.set_button_list([{"text": "Apple"}, {"text": "Banana"}, {"text": "Pear"}])`
  - `radio_button_group.set_button_list([{"text": "Apple", "checked": True}, {"text": "Banana"}, {"text": "Pear"}]) # 提供默认选中项`
  - `radio_button_group.set_button_list([{"text": "Apple", "checked": True, "icon": MIcon("app-maya.png")}, {"text": "Banana"}, {"text": "Pear"}]) # 提供图标`
******
## 添加选项
  - `radio_button_group.add_button({"text": "Orange"})`
********
## 设置选中按钮
  - `radio_button_group.set_dayu_checked(-1)`
********
## 获取选中按钮索引
  - `index = radio_button_group.get_dayu_checked()`
********
## 双向绑定
  - ```python
    # 注册一个普通属性
    self.register_field("radio_checked", -1)
    # 双向绑定
    self.bind(data_name="radio_checked", widget=radio_button_group, qt_property="dayu_checked",
    signal='sig_checked_changed', callback=lambda: print("触发回调"))

********
## 示例代码

```python
import asyncio
import functools
import random
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout
from dayu_widgets.qt import MIcon
from qasync import QEventLoop
from dayu_widgets import MTheme, MPushButton,MRadioButtonGroup, MFieldMixin, MLabel
class DemoWidget(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(DemoWidget, self).__init__(parent)
        self.setWindowTitle("MLoading控件学习")
        # 布局
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        radio_button_group = MRadioButtonGroup()
        radio_button_group.set_button_list(
            [{"text": "Apple", "checked": True, "icon": MIcon("app-maya.png")}, {"text": "Banana"}, {"text": "Pear"}])
        radio_button_group.add_button({"text": "Orange"})
        # 注册一个普通属性
        self.register_field("radio_checked", -1)
        # 双向绑定
        self.bind(data_name="radio_checked", widget=radio_button_group, qt_property="dayu_checked",
                  signal='sig_checked_changed', callback=lambda: print("触发回调"))
        # 注册一个计算属性,用来显示选中的值
        self.register_field(name="value", getter=functools.partial(lambda: radio_button_group.get_dayu_checked()))
        label = MLabel()
        # 单向绑定
        self.bind(data_name='value', widget=label, qt_property='text')
        button = MPushButton(text="change value", clicked=functools.partial(lambda: self.set_field("radio_checked", random.randint(-1, 2))))
        self.main_layout.addWidget(radio_button_group)
        self.main_layout.addWidget(label)
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
