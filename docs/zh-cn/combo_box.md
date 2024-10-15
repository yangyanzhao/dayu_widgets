## 简介
`MComboBox` 是一个增强版的 `QComboBox` 组件，提供了多种功能，包括搜索功能、自定义显示格式、多种尺寸以及与自定义菜单的集成
******
## 初始化
  - `combo_box = MComboBox()`
********
## 添加选项
  - `combo_box.addItems(["Option 1", "Option 2", "Option 3"])`
********
## 设置控件大小
  - `combo_box.huge()  # 设置为巨大尺寸`
  - `combo_box.large()  # 设置为大尺寸`
  - `combo_box.medium()  # 设置为中尺寸`
  - `combo_box.small()  # 设置为小尺寸`
  - `combo_box.tiny()  # 设置为微小尺寸`
******
## 集成`MMenu`菜单
  - ```python
    combo_box = MComboBox()
    cities = ["北京", "上海", "广州", "深圳"]
    menu = MMenu(parent=self)
    menu.set_data(cities)
    combo_box.set_menu(menu)
    ```
******
## 集成`MMenu`菜单(支持多选)
  - `menu = MMenu(parent=self, exclusive=False)`
******
## 集成`MMenu`菜单(动态选项)
  - ```python
    def dynamic_get_city():
        cities = ["上海", "北京", "深圳", "重庆", "广州", '成都', '天津', '武汉', '东莞', '西安', '杭州', '佛山',
                  '南京', '沈阳', '青岛', '济南', '长沙', '哈尔滨', '郑州', '昆明', '大连']
        start = random.randint(1, len(cities))
        end = random.randint(start, len(cities))
        return cities[start:end]
    combo_box = MComboBox()
    menu = MMenu(parent=self, exclusive=False)
    menu.set_load_callback(functools.partial(lambda: dynamic_get_city()))
    combo_box.set_menu(menu)
    ```
******
## 集成`MMenu`菜单(级联)
  - ```python
    combo_box = MComboBox()
    menu = MMenu(cascader=True, parent=self)  # cascader是否级联
    a = [
        {
            "children": [{"value": "故宫", "label": "故宫"},{"value": "天坛", "label": "天坛"},{"value": "王府井", "label": "王府井"}],
            "value": "北京",
            "label": "北京",
        },
        {
            "children": [{"value": "故宫", "label": "故宫"}],
            "value": "东京",
            "label": "东京",
        },
        {
            "children": [
                {
                    "children": [{"value": "夫子庙", "label": "夫子庙"}],
                    "value": "南京",
                    "label": "南京",
                },
               {
                    "children": [{"value": "拙政园", "label": "拙政园"},{"value": "狮子林", "label": "狮子林"}],
                    "value": "苏州",
                    "label": "苏州",
               },
            ],    
            "value": "江苏",
            "label": "江苏",
        },
    ]
    menu.set_data(a)
    combo_box.set_formatter(lambda x: " / ".join(x))  # 设置级联显示格式
    combo_box.set_menu(menu)
******
## 集成`MMenu`菜单(自定义显示)
  - ```python
    combo_box = MComboBox()
    menu = MMenu(exclusive=False, parent=self)  # cascader是否级联
    cities = ["上海", "北京", "深圳", "重庆", "广州", '成都', '天津', '武汉', '东莞', '西安', '杭州', '佛山',
    '南京', '沈阳', '青岛', '济南', '长沙', '哈尔滨', '郑州', '昆明', '大连']
    menu.set_data(cities)
    combo_box.set_formatter(lambda x: " & ".join(x))  # 设置级联显示格式
    combo_box.set_menu(menu)
    ```
******
## 搜索功能
  - ```python
    combo_box = MComboBox()
    cities = ["上海", "北京", "深圳", "重庆", "广州", '成都', '天津', '武汉', '东莞', '西安', '杭州', '佛山',
              '南京', '沈阳', '青岛', '济南', '长沙', '哈尔滨', '郑州', '昆明', '大连']
    combo_box.addItems(cities)
    combo_box.setProperty("searchable", True)
    ```
******
## 示例代码

```python
import random
from Qt import QtWidgets
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.menu import MMenu
class ComboBoxExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(ComboBoxExample, self).__init__(parent)
        self._init_ui()
    def _init_ui(self):
        cities = ["北京", "上海", "广州", "深圳"]
        self.register_field("button1_selected", "北京")
        menu1 = MMenu(parent=self)
        menu1.set_data(cities)
        size_list = [
            ("Large", dayu_theme.large),
            ("Medium", dayu_theme.medium),
            ("Small", dayu_theme.small),
        ]
        size_lay = QtWidgets.QHBoxLayout()
        for label, size in size_list:
            combo_box = MComboBox()
            combo_box.set_dayu_size(size)
            combo_box.set_menu(menu1)
            size_lay.addWidget(combo_box)
            self.bind(
                "button1_selected", combo_box, "value", signal="sig_value_changed"
            )
        self.register_field("button2_selected", ["北京"])
        menu2 = MMenu(exclusive=False, parent=self)
        menu2.set_data(cities)
        select2 = MComboBox()
        select2.set_menu(menu2)
        self.bind("button2_selected", select2, "value", signal="sig_value_changed")
        def dynamic_get_city():
            data = cities + ["郑州", "石家庄"]
            start = random.randint(0, len(data))
            end = random.randint(start, len(data))
            return data[start:end]
        self.register_field("button3_selected", "")
        menu3 = MMenu(parent=self)
        menu3.set_load_callback(dynamic_get_city)
        select3 = MComboBox()
        select3.set_menu(menu3)
        self.bind("button3_selected", select3, "value", signal="sig_value_changed")
        a = [
            {
                "children": [
                    {"value": "\u6545\u5bab", "label": "\u6545\u5bab"},
                    {"value": "\u5929\u575b", "label": "\u5929\u575b"},
                    {"value": "\u738b\u5e9c\u4e95", "label": "\u738b\u5e9c\u4e95"},
                ],
                "value": "\u5317\u4eac",
                "label": "\u5317\u4eac",
            },
            {
                "children": [
                    {"value": "\u6545\u5bab", "label": "\u6545\u5bab"},
                ],
                "value": "\u4e1c\u4eac",
                "label": "\u4e1c\u4eac",
            },
            {
                "children": [
                    {
                        "children": [
                            {
                                "value": "\u592b\u5b50\u5e99",
                                "label": "\u592b\u5b50\u5e99",
                            }
                        ],
                        "value": "\u5357\u4eac",
                        "label": "\u5357\u4eac",
                    },
                    {
                        "children": [
                            {
                                "value": "\u62d9\u653f\u56ed",
                                "label": "\u62d9\u653f\u56ed",
                            },
                            {
                                "value": "\u72ee\u5b50\u6797",
                                "label": "\u72ee\u5b50\u6797",
                            },
                        ],
                        "value": "\u82cf\u5dde",
                        "label": "\u82cf\u5dde",
                    },
                ],
                "value": "\u6c5f\u82cf",
                "label": "\u6c5f\u82cf",
            },
        ]
        self.register_field("button4_selected", "")
        menu4 = MMenu(cascader=True, parent=self)
        menu4.set_data(a)
        select4 = MComboBox()
        select4.set_menu(menu4)
        select4.set_formatter(lambda x: " / ".join(x))
        self.bind("button4_selected", select4, "value", signal="sig_value_changed")
        select4.set_value("北京/故宫")
        self.register_field("button5_selected", "")
        menu5 = MMenu(exclusive=False, parent=self)
        menu5.set_data(cities)
        select5 = MComboBox()
        select5.set_menu(menu5)
        select5.set_formatter(lambda x: " & ".join(x))
        self.bind("button5_selected", select5, "value", signal="sig_value_changed")
        sub_lay1 = QtWidgets.QHBoxLayout()
        sub_lay1.addWidget(MLabel("普通单选各种尺寸"))
        sub_lay1.addLayout(size_lay)
        sub_lay1.addStretch()
        sub_lay2 = QtWidgets.QHBoxLayout()
        sub_lay2.addWidget(MLabel("多选"))
        sub_lay2.addWidget(select2)
        sub_lay2.addStretch()
        sub_lay3 = QtWidgets.QHBoxLayout()
        sub_lay3.addWidget(MLabel("动态生成选项"))
        sub_lay3.addWidget(select3)
        sub_lay3.addStretch()
        sub_lay4 = QtWidgets.QHBoxLayout()
        sub_lay4.addWidget(MLabel("级联选择"))
        sub_lay4.addWidget(select4)
        sub_lay4.addStretch()
        sub_lay5 = QtWidgets.QHBoxLayout()
        sub_lay5.addWidget(MLabel("自定义显示"))
        sub_lay5.addWidget(select5)
        sub_lay5.addStretch()
        sub_lay6 = QtWidgets.QHBoxLayout()
        combo = MComboBox()
        items = cities + ["北戴河"]
        items += ["a" * i for i in range(20)]
        combo.addItems(items)
        combo.setProperty("searchable", True)
        sub_lay6.addWidget(MLabel("搜索补全"))
        sub_lay6.addWidget(combo)
        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("Select"))
        main_lay.addLayout(sub_lay1)
        main_lay.addLayout(sub_lay2)
        main_lay.addLayout(sub_lay3)
        main_lay.addWidget(MDivider("自定义格式"))
        main_lay.addLayout(sub_lay4)
        main_lay.addLayout(sub_lay5)
        main_lay.addLayout(sub_lay6)
        main_lay.addStretch()
        self.setLayout(main_lay)
if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application
    with application() as app:
        test = ComboBoxExample()
        dayu_theme.apply(test)
        test.show()
