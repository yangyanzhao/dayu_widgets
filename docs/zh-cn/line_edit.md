## 简介
`MLineEdit` 是一个自定义的 `QLineEdit` 控件，提供了多种功能和样式设置，如延迟文本更改信号、前缀和后缀小部件支持、文件选择按钮等。
******
## 初始化
  - `line_edit = MLineEdit()`
  - `line_edit = MLineEdit(text="手机号")`![img_60.png](img_60.png)
  - `line_edit.setPlaceholderText("medium size")`![img_61.png](img_61.png)
********
## 控件大小
  - `MLineEdit().large()`
  - `MLineEdit().medium()`
  - `MLineEdit().small()`
  - `MLineEdit().tiny()`
******
## 延迟文本更改信号
  - ```python
    line_edit.set_delay_duration(millisecond=2000) # 延迟时间（毫秒）
    line_edit.sig_delay_text_changed.connect(lambda text: print("text changed:", text))
    ```
    - UI输入后触发信号，延迟2秒。输入是持续过程，防止触发过于频繁。
    
******
## 获取和设置前缀小部件
  - ```python
    label = MLabel(text="User").mark().secondary()
    label.setAlignment(Qt.AlignCenter)
    label.setFixedWidth(40)
    line_edit.set_prefix_widget(label)
    ```
    ![img_70.png](img_70.png)
  - `line_edit.set_prefix_widget(MToolButton().svg("user_line.svg").icon_only())`

    ![img_59.png](img_59.png)
  - `prefix_widget = line_edit.get_prefix_widget()`
******
## 获取和设置后缀小部件
  - ```python
    push_button = MPushButton(text="Go").primary()
    push_button.setFixedWidth(40)
    line_edit.set_suffix_widget(push_button)
    ```
    ![img_71.png](img_71.png)
  - `line_edit.set_suffix_widget(MToolButton().svg("search_line.svg").icon_only())`

    ![img_62.png](img_62.png)
  - `suffix_widget = line_edit.get_suffix_widget()`
******
## 密码模式
  - `line_edit = MLineEdit().medium().password()`![img_69.png](img_69.png)
******
## 搜索模式
  - `line_edit = MLineEdit().medium().search()`![img_63.png](img_63.png)
******
## 错误模式
  - `line_edit = MLineEdit().medium().error()`![img_64.png](img_64.png)
******
## 搜索引擎按钮
  - ```python
    line_edit = MLineEdit().medium().search_engine()
    line_edit.returnPressed.connect(lambda: print())
  ![img_65.png](img_65.png)
******
## 文件选择按钮
  - `line_edit = MLineEdit().medium().file()`![img_66.png](img_66.png)
******
## 保存文件按钮
  - `line_edit = MLineEdit().medium().save_file()`![img_67.png](img_67.png)
******
## 文件夹选择按钮
  - `line_edit = MLineEdit().medium().folder()`![img_68.png](img_68.png)
******
## ComboBox模式
  - ```python
    line_edit = MLineEdit()
    combobox = MComboBox()
    option_menu = MMenu()
    option_menu.set_separator("|")
    option_menu.set_data([r"http://", r"https://"])
    combobox.set_menu(option_menu)
    combobox.set_value("http://")
    combobox.setFixedWidth(80)
    line_edit.set_prefix_widget(combobox)
    ```
    ![img_72.png](img_72.png)
******
## 双向绑定
  ```python
    # 数据绑定(账号)
    self.lineEdit_3.set_delay_duration(millisecond=2000)  # 延迟时间（毫秒
    widget_bind_value(parent=self, widget=self.lineEdit_3, field_name="login_username",widget_property="text", widget_signal="textChanged")
  ```
******
## 示例代码

```python
import asyncio
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout
from qasync import QEventLoop
from dayu_widgets import MTheme, MLineEdit, MToolButton
class DemoWidget(QWidget):
    def __init__(self, parent=None):
        super(DemoWidget, self).__init__(parent)
        layout = QVBoxLayout(self)
        self.setLayout(layout)
        line_edit = MLineEdit().medium().password()
        # 延迟文本更改信号
        line_edit.set_delay_duration(millisecond=2000)
        line_edit.sig_delay_text_changed.connect(lambda text: print("text changed:", text))
        # 设置前缀小部件
        line_edit.set_prefix_widget(MToolButton().svg("user_line.svg").icon_only())
        line_edit.set_suffix_widget(MToolButton().svg("search_line.svg").icon_only())
        layout.addWidget(line_edit)
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
