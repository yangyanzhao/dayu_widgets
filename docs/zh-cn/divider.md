## 简介
`MDivider` 是一个基于 `QtWidgets.QWidget` 的自定义分割线组件，适用于需要在界面中分隔不同内容的场景。该组件支持水平和垂直方向的分割线，并且可以在分割线上添加文本，文本可以居中、左对齐或右对齐。

![img_133.png](img_133.png)
******
## 初始化
  - `divider = MDivider(text="This is a divider", parent=None)`
  - `text: 分割线上的文本，默认为空字符串。`
  - `orientation: 分割线的方向，默认为 QtCore.Qt.Horizontal。`
  - `alignment: 文本的对齐方式，默认为 QtCore.Qt.AlignCenter。`
********
## 快捷方式
  - `horizontal_divider = MDivider.center("Center Text")`
  - `left_aligned_divider = MDivider.left("Left Text")`
  - `right_aligned_divider = MDivider.right("Right Text")`
  - `vertical_divider = MDivider.vertical()`
******
## 设置分割线上的文本
  - `set_dayu_text(value)`
******
## 获取当前的文本
  - `get_dayu_text()`
******
## 示例代码

```python
from Qt import QtWidgets
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
class DividerExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(DividerExample, self).__init__(parent)
        self.setWindowTitle("Examples for MDivider")
        self._init_ui()
    def _init_ui(self):
        div1 = MDivider()
        div2 = MDivider("With Text")
        div3 = MDivider.left("Left Text")
        div4 = MDivider.center("Center Text")
        div5 = MDivider.right("Right Text")
        div6 = MDivider.vertical()
        div7 = MDivider.vertical()
        div8 = MDivider.left("orientation=Qt.Vertical")
        label1 = MLabel("Maya").strong()
        label2 = MLabel("Nuke").underline()
        label3 = MLabel("Houdini").mark()
        sub_lay = QtWidgets.QHBoxLayout()
        sub_lay.addWidget(label1)
        sub_lay.addWidget(div6)
        sub_lay.addWidget(label2)
        sub_lay.addWidget(div7)
        sub_lay.addWidget(label3)
        sub_lay.addStretch()

        some_text = (
            "Steven Paul Jobs was an American entrepreneur and business magnate."
        )
        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MLabel(some_text))
        main_lay.addWidget(div1)
        main_lay.addWidget(MLabel(some_text))
        main_lay.addWidget(div2)
        main_lay.addWidget(MLabel(some_text))
        main_lay.addWidget(div3)
        main_lay.addWidget(MLabel(some_text))
        main_lay.addWidget(div4)
        main_lay.addWidget(MLabel(some_text))
        main_lay.addWidget(div5)
        main_lay.addLayout(sub_lay)
        main_lay.addWidget(div8)
        main_lay.addStretch()
        self.setLayout(main_lay)
    def computed_text(self):
        return "Clicked: " + str(self.field("count"))
    def slot_change_divider_text(self):
        self.set_field("count", self.field("count") + 1)
if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application
    with application() as app:
        test = DividerExample()
        dayu_theme.apply(test)
        test.show()
```