import sys

from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication

from dayu_widgets import MTableModel, MSortFilterModel, MFieldMixin, MTableView, dayu_theme, MLineEdit, MAlert
import examples._mock_data as mock


class TableViewExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(TableViewExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        # 构建数据模型
        model_1 = MTableModel()
        model_1.set_header_list(mock.header_list)
        model_1.set_data_list(mock.data_list)

        # 构建排序模型
        model_sort = MSortFilterModel()
        model_sort.setSourceModel(model_1)
        model_sort.set_header_list(mock.header_list)

        # 构建小表格
        table_small = MTableView(size=dayu_theme.small, show_row_count=False)  # show_row_count显示行号
        table_small.setModel(model_sort)
        table_small.set_header_list(mock.header_list)
        table_small.setShowGrid(True)  # 显示网格

        main_lay = QtWidgets.QVBoxLayout()
        self.setLayout(main_lay)

        # 搜索栏
        line_edit = MLineEdit().search().small()
        line_edit.textChanged.connect(model_sort.set_search_pattern)
        main_lay.addWidget(line_edit)
        main_lay.addWidget(table_small)
        main_lay.addStretch()
        main_lay.addWidget(MAlert('Simply use "MItemViewSet" or "MItemViewFullSet"'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = TableViewExample()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
