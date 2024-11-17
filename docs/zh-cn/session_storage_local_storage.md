## 简介
`DataSessionStorage` 和 `DataLocalStorage`
这一篇特地用来讲一讲数据的双向绑定，旨在让兄弟们可以更好的面向数据编程。这里就涉及到了两件事：1.数据的临时存放和持久化存放，2.数据与空间的双向绑定关系。
******

## 工具类

1.新建一个文件data_class.py
内容如下

```python
from PySide2.QtWidgets import QWidget
from dayu_widgets import MFieldMixin
from tinydb import TinyDB, Query


# 作为数据SessionStorage存储类
class DataSessionStorage(MFieldMixin):
    def __init__(self):
        super(DataSessionStorage, self).__init__()

    def widget_bind_value(self, widget: QWidget, field_name: str, widget_property: str,
                          widget_signal: str = None, callback=None):
        """
        控件数据绑定数据，双向绑定
        :param widget: 绑定控件
        :param field_name: 字段名称（用户自定义，取名儿不要冲突）
        :param widget_property: 控件属性名称（不知道属性的，可以用后边的方法进行遍历）
        :param widget_signal: 控件的数据改变信号（不知道信号的，可以用后边的方法进行遍历），如果不传，则时单项绑定，数据绑定到控件，但是控件自身数据改变不会通过信号回传到本地数据中。
        :param callback: 数据发生改变时的主动回调，一般不传入。
        """
        data_session_storage.register_field(name=field_name)
        data_session_storage.bind(data_name=field_name, widget=widget, qt_property=widget_property,
                                  signal=widget_signal, callback=callback)


# 作为数据LocalStorage存储类,与tinydb配合使用
class DataLocalStorage(MFieldMixin):
    def __init__(self):
        super(DataLocalStorage, self).__init__()
        # 数据库句柄(不知道tinydb的童鞋可以网上看看用法)
        self.tiny_db = TinyDB(path='json_db.json', ensure_ascii=False, encoding='utf-8')
        # 表
        self.table_local_storage = self.tiny_db.table('LocalStorage')

    def widget_bind_value(self, widget: QWidget, field_name: str, widget_property: str,
                          widget_signal: str, callback=None):
        """
        控件数据绑定数据，用来记住数据回显，使控件有记忆力。
        :param widget: 绑定控件
        :param field_name: 字段名称（用户自定义，取名儿不要冲突）
        :param widget_property: 控件属性名称（不知道属性的，可以用后边的方法进行遍历）
        :param widget_signal: 控件的数据改变信号（不知道信号的，可以用后边的方法进行遍历）
        :param callback: 数据发生改变时的主动回调，一般不传入。
        :return:
        """
        # 注册属性
        self.register_field(name=field_name)
        # 尝试获取配置
        field_data = self.table_local_storage.get(cond=Query()[field_name].exists())
        # 设置读取值
        if field_data and field_data[field_name]:
            self.set_field(name=field_name, value=field_data[field_name])
        else:
            self.set_field(name=field_name, value=widget.property(widget_property))
        # 绑定
        if callback:
            self.bind(data_name=field_name, widget=widget, qt_property=widget_property, signal=widget_signal,
                      callback=lambda: (self.table_local_storage.upsert(document={field_name: self.field(field_name)},
                                                                        cond=Query()[field_name].exists()), callback()))
        else:
            self.bind(data_name=field_name, widget=widget, qt_property=widget_property, signal=widget_signal,
                      callback=lambda: self.table_local_storage.upsert(document={field_name: self.field(field_name)},
                                                                       cond=Query()[field_name].exists()))


# 开局直接实例化这两个类，作为全局使用。
data_session_storage = DataSessionStorage()
data_local_storage = DataLocalStorage()

```

******

## 使用示例

`DataSessionStorage`是临时存储的数据绑定，重启后重置。
`DataLocalStorage`是持久化存储的数据绑定，会存储到本地，重启后会回显。

```python
data_local_storage.widget_bind_value(widget=widget,
                                     field_name=field_name,
                                     widget_property=widget_property,
                                     widget_signal=widget_signal)
m_spin_box_thumbs_up_number = MSpinBox()
m_spin_box_thumbs_up_number.setRange(1, 100)
m_spin_box_thumbs_up_number.setValue(20)
data_local_storage.widget_bind_value(widget=m_spin_box_thumbs_up_number,
                                     field_name="thumbs_up_number",
                                     widget_property="value", widget_signal="valueChanged")
layout.addWidget(m_spin_box_thumbs_up_number)
friend_edit = MLineEdit()
friend_edit.setPlaceholderText("请输入名称")
friend_edit.set_prefix_widget(MToolButton().svg(path=icons['微信好友.svg']).icon_only())
friend_edit.set_delay_duration(millisecond=2000)  # 延迟时间（毫秒）
data_local_storage.widget_bind_value(widget=friend_edit,
                                     field_name="wx_friend_chat_assistant",
                                     widget_property="text",
                                     widget_signal="textChanged")
combo_box.set_formatter(formatter_show)  # 设置级联显示格式
combo_box.set_menu(menu)
# 双向绑定
data_local_storage.widget_bind_value(widget=combo_box, field_name="prompt_menu_select",
                                     widget_property="value", widget_signal="sig_value_changed")
v_layout.addWidget(combo_box)
```

******

## 获取控件的属性、方法、信号示例

```python
import asyncio
from PySide2.QtCore import QMetaMethod
from PySide2.QtWidgets import QApplication, QPushButton
from qasync import QEventLoop

if __name__ == '__main__':
    # 创建主循环
    app = QApplication([])
    # 创建异步事件循环
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    # 创建窗口
    button = QPushButton()
    # 遍历所有属性
    property_count = button.metaObject().propertyCount()
    for i in range(property_count):
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
        prop_name = button.metaObject().property(i).name()
        if prop_name not in common_properties:
            print(f"Property: {prop_name}")
    # 遍历所有方法和信号
    meta_object = button.metaObject()
    count = meta_object.methodCount()
    for i in range(count):
        method = meta_object.method(i)
        if method.methodType() == QMetaMethod.Signal:
            print(f"Signal: {method.name().data().decode()}")
        elif method.methodType() == QMetaMethod.Method:
            print(f"Method: {method.name().data().decode()}")
    # 获取属性
    button.setProperty("text", "Hello World!")
    button_property = button.property("text")
    print(button_property)
    # 设置属性
    # 显示窗口
    button.show()
    loop.run_forever()
```