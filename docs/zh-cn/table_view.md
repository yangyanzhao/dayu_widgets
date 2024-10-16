## 简介
`MTableView` 是一个基于 `QtWidgets.QTableView` 的自定义表格视图类，用于展示数据，并提供了丰富的功能如上下文菜单、无数据时的自定义显示、列头状态保存与加载等。
******
## 初始化
  - `list_view = MListView(size=dayu_theme.small)  # 设置尺寸size`
********
## 设置header
  - ```python
    header_list = [{
            "label": "Name",
            "key": "name",
            "checkable": True,  # 是否支持勾选
            "searchable": True,  # 是否支持搜索
            "editable": True,  # 是否支持编辑
            "draggable": True,  # 是否支持拖拽
            "droppable": True,  # 是否支持拖放
            "width": 100,  # 宽度
            "font": lambda x, y: {"underline": True},  # 字体样式
            "icon": "user_fill.svg",  # 显示图标
        }]
    list_view.set_header_list(header_list)
    ```
******
## 设置数据
  - ```python
    data_list = [
            {"name": "John Brown"},
            {"name": "John"},
            {"name": "Brown"},
            {"name": "Lily"},
    ]
    # 设置数据模型
    model = MTableModel()
    model.set_header_list(header_list)
    model.set_data_list(data_list)
    list_view.setModel(model)
    ```
******
## 设置数据(支持搜索)
  - ```python
    data_list = [
            {"name": "John Brown"},
            {"name": "John"},
            {"name": "Brown"},
            {"name": "Lily"},
    ]
    # 设置数据模型
    model = MTableModel()
    model.set_header_list(header_list)
    model.set_data_list(data_list)  
    # 支持搜索
    model_sort = MSortFilterModel()
    model_sort.setSourceModel(model)
    model_sort.set_header_list(header_list) 
    list_view.setModel(model_sort)  
    line_edit = MLineEdit().search().small()
    line_edit.textChanged.connect(model_sort.set_search_pattern)
    ```
******
## 设置右键回调
  - ```python
    # 右键信号回调
    def on_context_menu(event: ItemViewMenuEvent):
        print(event.selection)
    # 支持右键信号
    list_view.enable_context_menu(True)
    list_view.sig_context_menu.connect(on_context_menu)
    ```
## 示例代码

```python
import asyncio
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout
from dayu_widgets.utils import ItemViewMenuEvent
from qasync import QEventLoop
from dayu_widgets import MTheme, MFieldMixin, dayu_theme, MListView, MTableModel, MSortFilterModel, MLineEdit
class DemoWidget(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(DemoWidget, self).__init__(parent)
        layout = QVBoxLayout()
        self.setLayout(layout)
        # 实例化
        list_view = MListView(size=dayu_theme.small)
        header_list = [{
            "label": "Name",
            "key": "name",
            "checkable": True,  # 是否支持勾选
            "searchable": True,  # 是否支持搜索
            "editable": True,  # 是否支持编辑
            "draggable": True,  # 是否支持拖拽
            "droppable": True,  # 是否支持拖放
            "width": 100,  # 宽度
            "font": lambda x, y: {"underline": True},  # 字体样式
            "icon": "user_fill.svg",  # 显示图标
        }]
        list_view.set_header_list(header_list)

        data_list = [
            {"name": "John Brown"},
            {"name": "John"},
            {"name": "Brown"},
            {"name": "Lily"},
        ]
        # 设置数据模型
        model = MTableModel()
        model.set_header_list(header_list)
        model.set_data_list(data_list)

        # 支持搜索
        model_sort = MSortFilterModel()
        model_sort.setSourceModel(model)
        model_sort.set_header_list(header_list)

        list_view.setModel(model_sort)

        line_edit = MLineEdit().search().small()
        line_edit.textChanged.connect(model_sort.set_search_pattern)

        # 右键信号回调
        def on_context_menu(event: ItemViewMenuEvent):
            print(event.selection)

        # 支持右键信号
        list_view.enable_context_menu(True)
        list_view.sig_context_menu.connect(on_context_menu)
        layout.addWidget(line_edit)
        layout.addWidget(list_view)
        layout.addStretch()
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
```