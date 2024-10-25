## 简介
`MFieldMixin` 用于管理数据字段和 UI 组件之间绑定。它允许你将数据字段与 UI 组件的属性进行绑定，并在数据发生变化时自动更新 UI，或者在 UI 组件发生变化时自动更新数据。这个类用于构建数据驱动的用户界面(Vue)。
******
## 注册字段
  - `.register_field(name, getter=None, setter=None, required=False)`
    - `name`: 字段名称。
    - `getter`: 用于获取字段值的函数，默认为 `None`,如果提供了 getter 函数，字段将被视为计算字段（computed field），否则将被视为普通字段（property field）。
    - `setter`: 用于设置字段值的函数，默认为 `None`。
    - `required`: 是否字段是必须的，默认为 `False`,表示该字段是否是必需的。
********
## 绑定字段
  - `.bind(data_name, widget, qt_property, index=None, signal=None, callback=None)`
    - `data_name`: 数据字段的名称。
    - `widget`: UI 组件的实例。
    - `qt_property`: UI 组件的属性名称。
    - `index`: 用于在列表中定位数据的索引。
    - `signal`: 用于监听数据的信号。
    - `callback`: 当数据属性发生变化时调用的回调函数。
******
## 获取字段值
  - `self.field('Computed')`
******
## 设置字段值
  - `self.set_field('Props', f"{random.randint(-100, 100)}")`
******
## 普通属性（即双向绑定）
  - ```python        
    # 注册一个数据属性
    self.register_field(name='Props')
    # 将数据绑定到UI控件上，当数据发生改变，则更新UI,并触发callback回调。当signal信号触发，则更新UI数据到数据属性，因数据属性发生改变，所以也会触发callback回调。
    self.bind(data_name="Props", widget=self.edit_props, qt_property="text",
              signal="sig_delay_text_changed", callback=lambda: print("触发回调函数"))
******
## 计算属性（即单向绑定，将计算的数据结果绑定到UI控件，但UI控件的值无法反向绑定到计算属性上）
  - ```python
    # 注册一个计算属性，不需要setter，因为计算属性都是由其他数据计算出来的，不需要手动设置。
    self.register_field(name='Computed', getter=lambda: self.field('Props') * 2 if self.field('Props') else 0)
    # 将数据绑定到UI控件上，当数据发生改变，则更新UI,并触发callback回调函数。不需要设置signal，因为是单向的，计算属性是自动更新的。
    self.bind(data_name="Computed", widget=self.edit_computed, qt_property="text", callback=lambda: print("触发回调函数1"))
******
## 获取控件的所有的属性
  - ```python
        self.line_edit = MLineEdit().search().small()
        count = self.line_edit.metaObject().propertyCount()
        for i in range(count):
            print(self.line_edit.metaObject().property(i).name())
    ```
******
## 获取控件的属性（过滤掉一些常见属性）
  - ```python
        self.line_edit = MLineEdit().search().small()
        count = self.line_edit.metaObject().propertyCount()
        for i in range(count):
            common_properties = {"objectName", "enabled", "geometry", "size", "pos", "x", "y", "width", "height", "rect",
                             "sizeHint", "minimumSizeHint", "sizePolicy", "minimumSize", "maximumSize", "minimumWidth",
                             "minimumHeight", "maximumWidth", "maximumHeight", "focusPolicy", "focus", "updatesEnabled",
                             "visible", "hidden", "sizeIncrement", "baseSize", "cursor", "mouseTracking",
                             "isActiveWindow", "underMouse", "isFullScreen", "windowOpacity", "windowModified",
                             "acceptDrops", "windowTitle", "windowIcon", "windowIconText", "windowFilePath",
                             "windowFlags", "isTopLevel", "isWindowModified", "isModal", "windowModality", "isEnabled",
                             "isEnabledTo", "isEnabledToParent", "layoutDirection", "isVisible", "isVisibleTo",
                             "isVisibleToParent", "isMinimized", "isMaximized", "isSizeGripEnabled",
                             "autoFillBackground", "styleSheet", "palette", "font", "cursor"}
            # 过滤掉一些常用属性
            prop_name = self.line_edit.metaObject().property(i).name()
            if prop_name not in common_properties:
                print(prop_name)
    ```
******
## 获取控件的所有方法和信号（信号在 `Qt` 中被视为一种特殊的方法。）
  - ```python
    button = QPushButton()
    meta_object = button.metaObject()
    count = meta_object.methodCount()
    for i in range(count):
        method = meta_object.method(i)
        if method.methodType() == QMetaMethod.Signal:
            print(f"Signal: {method.name().data().decode()}")
    ```
******
## 示例代码

```python
import asyncio
import random
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout
from qasync import QEventLoop
from dayu_widgets import MTheme, MPushButton, MFieldMixin, MLineEdit
class DemoWidget(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(DemoWidget, self).__init__(parent)
        # 布局
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        """普通属性的双向绑定示例:"""
        self.button_props = MPushButton("Click Props")
        self.button_props.clicked.connect(self.on_click_props)
        self.main_layout.addWidget(self.button_props)
        self.edit_props = MLineEdit("Props")
        self.main_layout.addWidget(self.edit_props)
        # 注册一个数据属性,通常不需要getter，因为数据属性是绑定在UI控件上的，所以会自动更新。
        self.register_field(name='Props', setter=lambda value: self.set_field('Props', value))
        # 将数据绑定到UI控件上，当数据发生改变，则更新UI,并触发callback回调。当signal信号触发，则更新UI数据到数据属性，因数据属性发生改变，所以也会触发callback回调。
        self.bind(data_name="Props", widget=self.edit_props, qt_property="text",
                  signal="sig_delay_text_changed", callback=lambda: print(f"[普通]触发回调函数{self.field('Props')}"))
        """计算属性的单向绑定示例:"""
        self.button_computed = MPushButton("Click Computed")
        self.button_computed.clicked.connect(self.on_click_computed)
        self.main_layout.addWidget(self.button_computed)
        self.edit_computed = MLineEdit("Computed")
        self.main_layout.addWidget(self.edit_computed)
        # 注册一个计算属性，通常不需要setter，因为计算属性都是由其他数据计算出来的，不需要手动设置。
        self.register_field(name='Computed', getter=lambda: self.field('Props') * 2 if self.field('Props') else 0)
        # 将数据绑定到UI控件上，当数据发生改变，则更新UI,并触发callback回调函数。通常不需要signal，因为计算属性是自动更新的。
        self.bind(data_name="Computed", widget=self.edit_computed, qt_property="text",
                  callback=lambda: print(f"[计算]触发回调函数{self.field('Computed')}"))
    def on_click_props(self):
        print(self.field('Props'))
        self.set_field(name='Props', value=f"{random.randint(-100, 100)}")
    def on_click_computed(self):
        print(self.field('Computed'))
        self.set_field('Props', f"{random.randint(-100, 100)}")
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
