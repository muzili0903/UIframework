"""
@Time ： 2021/8/5 22:01
@Auth ： muzili
@File ： methodMap.py
@IDE  ： PyCharm
"""
METHODS = {
    "clearAndInput": "self.wdo.clear_input_text(tp, element, content)",
    "input": "self.wdo.input_text(tp, element, content)",
    "getText": "self.wdo.get_text(tp, element)",
    "click": "self.wdo.click(tp, element)",
    "radio": "self.wdo.radio(tp, element)",
    "single": "self.wdo.single(tp, element, content, s_tp='text')",
    "checkboxOne": "self.wdo.checkbox(tp, element)",
    "checkboxAll": "self.wdo.checkbox_all(tp, elements)",
    "delCheckbox": "self.wdo.del_checkbox(tp, element)",
    "multi": "self.wdo.multi(tp, element, content, s_tp='text')",
    "delMulti": "self.wdo.del_multi(tp, element, content, s_tp='text')",
    "delAllMulti": "self.wdo.del_all_multi(tp, elements)",
    "confirm": "self.wdo.confirm()",
    "cancel": "self.wdo.cancel()",
    "enterFrame": "self.wdo.frame(tp, element)",
    "quitFrame": "self.wdo.quit_frame()",
    "parentFrame": "self.wdo.parent_frame()",
    "window": "self.wdo.window(index)",
    "save": "self.wdo.save(tp, element, content)",
    "saveInput": "self.wdo.save_input()",
    "saveResult": "self.wdo.save_result()"
}

ELE_TYPE = ['xp', 'id', 'css', 'cls', 'name', 'lk', 'plk', 'tag']

EXCEL_METHODS = ['saveInput', 'saveResult']

