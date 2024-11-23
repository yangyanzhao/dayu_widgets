## 为自定义组件添加阴影
悬停时获得阴影效果
```python
from dayu_widgets.mixin import hover_shadow_mixin

@hover_shadow_mixin
class MMeta(QtWidgets.QWidget):
    pass
```
聚焦时获得阴影效果
```python
from dayu_widgets.mixin import cursor_mixin
@cursor_mixin
class MMeta(QtWidgets.QWidget):
    pass
```
## 为widget示例添加阴影
函数:
```python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from Qt import QtGui
from Qt import QtWidgets


def add_focus_shadow(widget):
    """
    Add shadow effect for the given widget when it is focused.
    When focus in the widget, enable shadow effect.
    When focus out the widget, disable shadow effect.
    """
    # Save the original focusInEvent and focusOutEvent methods
    original_focus_in_event = widget.focusInEvent
    original_focus_out_event = widget.focusOutEvent

    def _focus_in_event(event):
        if not widget.graphicsEffect():
            shadow_effect = QtWidgets.QGraphicsDropShadowEffect(widget)
            dayu_type = widget.property("dayu_type")
            color = vars(dayu_theme).get("{}_color".format(dayu_type or "primary"), "primary_color")
            shadow_effect.setColor(QtGui.QColor(color))
            shadow_effect.setOffset(0, 0)
            shadow_effect.setBlurRadius(5)
            shadow_effect.setEnabled(False)
            widget.setGraphicsEffect(shadow_effect)
        if widget.isEnabled():
            widget.graphicsEffect().setEnabled(True)
        original_focus_in_event(event)  # Call the original focusInEvent with only the event argument

    def _focus_out_event(event):
        if widget.graphicsEffect():
            widget.graphicsEffect().setEnabled(False)
        original_focus_out_event(event)  # Call the original focusOutEvent with only the event argument

    # Replace the original focusInEvent and focusOutEvent with the new ones
    widget.focusInEvent = _focus_in_event
    widget.focusOutEvent = _focus_out_event


# Example usage:
# widget = QtWidgets.QPushButton("Focus me")
# add_focus_shadow(widget)

from dayu_widgets import dayu_theme


def add_hover_shadow_mixin(widget):
    """
    Add shadow effect for the given widget when it is hovered.
    When mouse enter the widget, enable shadow effect.
    When mouse leave the widget, disable shadow effect.
    """
    # Save the original enterEvent and leaveEvent methods
    original_enter_event = widget.enterEvent
    original_leave_event = widget.leaveEvent

    def _enter_event(event):
        if not widget.graphicsEffect():
            shadow_effect = QtWidgets.QGraphicsDropShadowEffect(widget)
            dayu_type = widget.property("type")
            color = vars(dayu_theme).get("{}_color".format(dayu_type or "primary"), "primary_color")
            shadow_effect.setColor(QtGui.QColor(color))
            shadow_effect.setOffset(0, 0)
            shadow_effect.setBlurRadius(5)
            shadow_effect.setEnabled(False)
            widget.setGraphicsEffect(shadow_effect)
        if widget.isEnabled():
            widget.graphicsEffect().setEnabled(True)
        original_enter_event(event)  # Call the original enterEvent with only the event argument

    def _leave_event(event):
        if widget.graphicsEffect():
            widget.graphicsEffect().setEnabled(False)
        original_leave_event(event)  # Call the original leaveEvent with only the event argument

    # Replace the original enterEvent and leaveEvent with the new ones
    widget.enterEvent = _enter_event
    widget.leaveEvent = _leave_event

# Example usage:
# widget = QtWidgets.QPushButton("Hover me")
# add_hover_shadow(widget)

# Example usage:
# widget = QtWidgets.QPushButton("Hover me")
# add_hover_shadow(widget)

# Example usage:
# widget = QtWidgets.QPushButton("Hover me")
# add_hover_shadow(widget)

```
 示例:
```python
q_widget = QWidget()
# 悬停时获得阴影效果
add_hover_shadow_mixin(q_widget)
# 聚焦时获得阴影效果
add_focus_shadow(q_widget)
```