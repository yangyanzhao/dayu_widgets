## 安装
- ```python
  pip install PySide2
  ```
- ```python
  pip install qasync
  ```
- ```python
  pip install dayu_widgets
  ```
- ```python
  pip install dayu_widgets_tag
  ```

******
## 导入控件
```python
from dayu_widgets import MTheme, MPushButton
```
## 实例化窗口
```python
# 创建窗口
widget = QWidget()
```
## 设置主题
```python
# 设置主题
MTheme().apply(widget)
```
## 使用控件
```python
button = MPushButton("默认按钮").primary()
layout.addWidget(button)
```
## 完整示例
```python
import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout
from dayu_widgets import MTheme, MPushButton
if __name__ == '__main__':
    # 创建主循环
    app = QApplication([])

    # 创建窗口
    widget = QWidget()
    # 设置主题
    MTheme().apply(widget)
    # 窗口布局
    layout = QVBoxLayout(widget)
    # 使用控件
    button = MPushButton("默认按钮").primary()
    layout.addWidget(button)
    # 显示窗口
    widget.show()

    sys.exit(app.exec_())
