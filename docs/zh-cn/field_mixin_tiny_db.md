## 简介
使双向绑定拥有LocalStorage的能力

******
## 初始化TinyDB
  - ```python
    from tinydb import TinyDB
    # 数据库句柄
    tiny_db = TinyDB(path='json_db.json', ensure_ascii=False, encoding='utf-8')
    # 配置表
    table_settings = tiny_db.table('Settings')
    # 控件记忆表
    table_memory = tiny_db.table('Memory')
********
## 数据绑定（直接复制到项目中使用）
  - ```python
        def widget_bind_value(parent: MFieldMixin, widget: QWidget, field_name: str, widget_property: str,
                          widget_signal: str):
            """
            控件数据绑定数据，用来记住数据回显，使控件有记忆力。
            :param parent: 父级控件
            :param widget: 绑定控件
            :param field_name: 字段名称
            :param widget_property: 控件属性名称
            :param widget_signal: 控件的数据改变信号
            :return:
            """
            # 注册属性
            parent.register_field(name=field_name)
            # 尝试获取配置
            field_data = table_memory.get(cond=Query()[field_name].exists())
            # 设置读取值
            if field_data and field_data[field_name]:
                parent.set_field(name=field_name, value=field_data[field_name])
            else:
                parent.set_field(name=field_name, value=widget.property(widget_property))
            # 双向绑定
            parent.bind(data_name=field_name, widget=widget, qt_property=widget_property, signal=widget_signal,
                    callback=lambda: table_memory.upsert(document={field_name: parent.field(field_name)},
                                                         cond=Query()[field_name].exists()))
******
## 示例使用

```python
        # 好友名称
        friend_edit = MLineEdit()
        friend_edit.setPlaceholderText("请输入微信好友名称")
        friend_edit.set_prefix_widget(MToolButton().svg(path="icons/微信好友.svg").icon_only())
        friend_edit.set_delay_duration(millisecond=2000)  # 延迟时间（毫秒）
        widget_bind_value(parent=self, 
                          widget=friend_edit, 
                          field_name="wx_friend_chat_assistant",
                          widget_property="text",
                          widget_signal="textChanged")
```