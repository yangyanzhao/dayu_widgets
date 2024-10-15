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
## 搜索功能
  - ``
******
## 自定义显示格式
  - ``
******
## 搜索功能
  - ``
******
## 双向绑定
  - ```python
******
## 示例代码

```python