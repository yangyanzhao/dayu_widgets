## 简介
MCheckBoxGroup 是一个自定义的复选框组组件，支持水平或垂直布局，并提供了选择所有、取消选择所有和反选的功能。此外，它还支持数据绑定和信号槽机制。
******
## 初始化
  - `check_box_group = MCheckBoxGroup(orientation=QtCore.Qt.Horizontal)`
    - `orientation`: 布局方向，默认为水平方向 `QtCore.Qt.Horizontal`。
********
## 设置选项
  - ```python
    self.app_data = [
            {"text": "Maya", "icon": MIcon("app-maya.png")},
            {"text": "Nuke", "icon": MIcon("app-nuke.png")},
            {"text": "Houdini", "icon": MIcon("app-houdini.png")},
        ]
    check_box_group.set_button_list(self.app_data)
    ```
    ![img_57.png](img_57.png)
  - ```python
    self.data_list = ["北京", "上海", "广州", "深圳", "郑州", "石家庄"]
    # 设置选项
    check_box_group.set_button_list(self.data_list)
    ```
    ![img_58.png](img_58.png)
********
## 添加选项
  - ```python
    data_dict = {"text": "Photoshop", "icon": MIcon("app-photoshop.png")}
    check_box_group.add_button(data_dict=data_dict)
    ```
******
## 设置初始选中状态
  - `check_box_group.set_dayu_checked(["Nuke", "Photoshop"])`
******
## 获取当前选中状态
  - `checked_items = check_box_group.get_dayu_checked()`
******
## 选中元素发生变化触发信号
  - `checkbox_group.sig_checked_changed.connect(self.on_checked_changed)`
******
## 双向绑定
  - ```python
    self.data_list = ["北京", "上海", "广州", "深圳", "郑州", "石家庄"]
    radio_group_b = MCheckBoxGroup()
    # 设置选项
    radio_group_b.set_button_list(self.data_list)
    # 注册数据属性
    self.register_field("checked_list", ["北京", "郑州"])  # 已选中的数据
    # 进行双向绑定
    self.bind(data_name="checked_list", widget=radio_group_b, qt_property="dayu_checked", signal="sig_checked_changed")
    button = MPushButton(text="Change Value")
    button.clicked.connect(functools.partial(lambda: self.set_field("checked_list", self.data_list[random.randint(0, len(self.data_list)):len(self.data_list)])))
    ```
        
## 上下文菜单
  - 右键点击 `MCheckBoxGroup` 会弹出上下文菜单，提供以下选项：![img_56.png](img_56.png)
    - Select All: 选择所有复选框
    - Select None: 取消选择所有复选框
    - Select Invert: 反选所有复选框
******
## 自定义全选、取消、反选按钮
  - ```python
    # 自定义全选、取消全选、反选
    button_all = MPushButton(text="全选")
    button_none = MPushButton(text="取消")
    button_invert = MPushButton(text="反选")
    button_all.clicked.connect(functools.partial(check_box_group._slot_set_select, True))
    button_none.clicked.connect(functools.partial(check_box_group._slot_set_select, False))
    button_invert.clicked.connect(functools.partial(check_box_group._slot_set_select, None))
    ```
******
## 示例代码

```python
import asyncio
import functools
import random
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout
from dayu_widgets.qt import MIcon
from qasync import QEventLoop
from dayu_widgets import MTheme, MCheckBoxGroup, MPushButton, MFieldMixin
class DemoWidget(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(DemoWidget, self).__init__(parent)
        layout = QVBoxLayout()
        self.setLayout(layout)
        # 组
        check_box_group = MCheckBoxGroup()
        self.app_data = [
            {"text": "Maya", "icon": MIcon("app-maya.png")},
            {"text": "Nuke", "icon": MIcon("app-nuke.png")},
            {"text": "Houdini", "icon": MIcon("app-houdini.png")},
        ]
        check_box_group.set_button_list(self.app_data)
        data_dict = {"text": "Photoshop", "icon": MIcon("app-photoshop.png")}
        check_box_group.add_button(data_dict=data_dict)
        check_box_group.set_dayu_checked(["Nuke", "Photoshop"])
        layout.addWidget(check_box_group)
        check_box_group.sig_checked_changed.connect(lambda: print("变哈"))
        self.data_list = ["北京", "上海", "广州", "深圳", "郑州", "石家庄"]
        radio_group_b = MCheckBoxGroup()
        # 设置选项
        radio_group_b.set_button_list(self.data_list)
        # 注册数据属性
        self.register_field("checked_app", ["北京", "郑州"])
        # 进行双向绑定
        self.bind(data_name="checked_app", widget=radio_group_b, qt_property="dayu_checked",
                  signal="sig_checked_changed")
        layout.addWidget(radio_group_b)
        button = MPushButton(text="Change Value")
        button.clicked.connect(self.slot_button_clicked)
        layout.addWidget(button)
        # 自定义全选、取消全选、反选
        button_all = MPushButton(text="全选")
        button_none = MPushButton(text="取消")
        button_invert = MPushButton(text="反选")
        button_all.clicked.connect(functools.partial(check_box_group._slot_set_select, True))
        button_none.clicked.connect(functools.partial(check_box_group._slot_set_select, False))
        button_invert.clicked.connect(functools.partial(check_box_group._slot_set_select, None))
        layout.addWidget(button_all)
        layout.addWidget(button_none)
        layout.addWidget(button_invert)
        pass
    def slot_button_clicked(self):
        start = random.randint(0, len(self.data_list))
        end = random.randint(start, len(self.data_list))
        self.set_field("checked_app", self.data_list[start:end])
        pass
if __name__ == '__main__':
    # 创建主循环
    app = QApplication([])
    # 创建异步事件循环
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    # 创建窗口
    demo_widget = DemoWidget()
    MTheme("dark").apply(demo_widget)
    # 显示窗口
    demo_widget.show()
    loop.run_forever()
