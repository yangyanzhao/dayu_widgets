![img_53.png](img_53.png)
## 简介
`MPage` 是一个自定义的分页组件，用于处理大量数据的分页显示。它可以将长列表分成若干页，并且每次只加载一页数据。用户可以通过按钮和下拉菜单来选择每页显示的数据量以及当前页数。
******
## 初始化`MPage`
  - `page = MPage()`
********
## 设置总条目数
  - `page.set_total(100)`
******
## 设置可选的数据量配置
  - ```python
    selections = [25, 50, 75, 100] 
    page.set_page_config(selections)
    ```
******
## 监听页码改变事件
  - `page.sig_page_changed.connect(lambda page_size, page_number: print(f"page_size:{page_size} | page_number:{page_number}"))`
******
## 示例代码

```python
import asyncio
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout
from qasync import QEventLoop
from dayu_widgets import MTheme, MPage
class DemoWidget(QWidget):
    def __init__(self, parent=None):
        super(DemoWidget, self).__init__(parent)
        layout = QVBoxLayout()
        self.setLayout(layout)
        page = MPage()
        # 设置总条目数
        page.set_total(100)
        # 可选的数据量配置
        selections = [25, 50, 75, 100]
        page.set_page_config(selections)
        page.sig_page_changed.connect(lambda page_size, page_number: print(f"page_size:{page_size} | page_number:{page_number}"))
        layout.addWidget(page)
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
