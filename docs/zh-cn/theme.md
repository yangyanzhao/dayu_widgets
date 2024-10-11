## 简介
`MTheme` 类用于管理应用程序的主题样式，包括颜色、字体大小和其他样式属性。它支持多种颜色方案，并且可以根据不同的主题（如深色或浅色）自动调整样式
******
## 初始化主题
  - `theme = MTheme(theme="light", primary_color="#1890ff")`
********
## 设置主题
  - `theme.set_theme("light") # 设置浅色主题`
  - `theme.set_theme("dark") # 设置深色主题`
******
## 设置主色调
  - `theme.set_primary_color("#f5222d") # 设置主色调`
  - `theme.set_primary_color(MTheme.blue) # 设置主色调`
******
## 应用样式到控件
  - `theme.apply(widget) # 应用样式到控件`
******
## 装饰器应用样式
  - ```python
    @theme.deco
    class MyWidget(QtWidgets.QWidget):
        def __init__(self, parent=None):
            super(MyWidget, self).__init__(parent)
    ```
******
## 主色调颜色
  - blue
  - purple
  - cyan
  - green
  - magenta
  - pink
  - red
  - orange
  - yellow
  - volcano
  - geekblue
  - lime
  - gold
  - female_color
  - male_color
******
## 字体
  - ```python
    theme.font_family  # 字体家族
    theme.font_size_base  # 基础字体大小
    theme.font_size_large  # 较大字体大小
    theme.font_size_small  # 较小字体大小
    ```
******
## 圆角
  - ```python
    theme.border_radius_large  # 较大的圆角半径
    theme.border_radius_base  # 基础圆角半径
    theme.border_radius_small  # 较小的圆角半径
    ...
    ```
******

## 示例代码

```python
import sys
from PySide2.QtWidgets import QPushButton, QWidget, QApplication, QVBoxLayout
from dayu_widgets import MTheme
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建窗口
    window = QWidget()
    # 初始化主题
    theme = MTheme(theme="dark", primary_color="#1890ff")
    # 应用主题样式
    theme.apply(window)
    # 设置布局
    layout = QVBoxLayout(window)
    button = QPushButton("Click Me")
    layout.addWidget(button)
    # 显示窗口
    window.show()
    sys.exit(app.exec_())
