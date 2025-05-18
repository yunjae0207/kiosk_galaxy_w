from kivy.uix.screenmanager import Screen, ScreenManager,SwapTransition
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.properties import ListProperty, StringProperty, ObjectProperty, NumericProperty
from kivy.factory import Factory
from kivy.app import App
from kivy.clock import Clock

class Screen_Language(Screen):
    pass
class Screen_Zero(Screen):
    pass
class Screen_First(Screen):
    pass
class Screen_Second(Screen):
    pass
class Screen_Third(Screen):
    pass
class Screen_Fourth(Screen):
    rv = ObjectProperty(None)
    cart_items = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_kv_post(self, base_widget):
        self.refresh_view()

    def refresh_view(self):
        self.rv.data = [{
            'item_text': item,
            'on_delete': self.remove_item
        } for item in self.cart_items]
        
    def remove_item(self, item):  
        if item in self.cart_items:
            self.cart_items.remove(item)
            self.refresh_view()

    def clear_all_items(self):  # 전체 삭제 메서드
        self.cart_items.clear()
        self.refresh_view()

class Screen_Fifth(Screen):
    pass
class Screen_Sixth(Screen):
    def on_enter(self):
        Clock.schedule_once(self.click_button, 4)

    def click_button(self, dt):
        end_button = self.ids.end_button
        end_button.dispatch('on_release')
class Sub_First(Screen):
    pass
class Sub_Second(Screen):
    pass
class Sub_Third(Screen):
    pass
class Sub_Fourth(Screen):
    pass
class Button_Sub(Button):
    price = NumericProperty(0) 
    product_name = StringProperty("")
class Button_Pay(Button):
    pass
class Button_Plus(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # 부모 클래스 초기화
        self.current_color = (0.93,0.93,0.93, 1)  # 초기 색상 값 설정
    def change_color(self):
        if self.current_color == (0.93,0.93,0.93, 1):
            self.background_color = (1, 0, 0, 1)
            self.current_color = (1, 0, 0, 1)
        else:
            self.background_color = (0.93,0.93,0.93, 1)
            self.current_color = (0.93,0.93,0.93, 1)
class Popup_Store(Popup):
    popup_store_label_first = ObjectProperty(None)
class Popup_Pay(Popup):
    popup_pay_label_first = ObjectProperty(None)
class CartItem(BoxLayout):
    item_text = StringProperty()
    on_delete = ObjectProperty(None)

class Screen_Seventh(Screen):
    pass
class Screen_Eighth(Screen):
    pass
class Screen_Ninth(Screen):
    pass
class Screen_Tenth(Screen):
    rv = ObjectProperty(None)
    cart_items_en = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_kv_post(self, base_widget):
        self.refresh_view()

    def refresh_view(self):
        self.rv.data = [{
            'item_text': item,
            'on_delete': self.remove_item
        } for item in self.cart_items_en]
        
    def remove_item(self, item):  
        if item in self.cart_items_en:
            self.cart_items_en.remove(item)
            self.refresh_view()

    def clear_all_items(self):  # 전체 삭제 메서드
        self.cart_items_en.clear()
        self.refresh_view()
class Screen_Eleventh(Screen):
    pass
class Screen_Twelfth(Screen):
    def on_enter(self):
        Clock.schedule_once(self.click_button, 4)

    def click_button(self, dt):
        end_button = self.ids.end_button
        end_button.dispatch('on_release')
class Sub_First_En(Screen):
    pass
class Sub_Second_En(Screen):
    pass
class Sub_Third_En(Screen):
    pass
class Sub_Fourth_En(Screen):
    pass
class Popup_Store_En(Popup):
    popup_store_en_label_first = ObjectProperty(None)
class Popup_Pay_En(Popup):
    popup_pay_en_label_first = ObjectProperty(None)
class Button_Sub_En(Button):
    price = NumericProperty(0) 
    product_name = StringProperty("")
class Button_Pay_En(Button):
    pass
class Button_Plus_En(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # 부모 클래스 초기화
        self.current_color = (0.93,0.93,0.93, 1)  # 초기 색상 값 설정
    def change_color(self):
        if self.current_color == (0.93,0.93,0.93, 1):
            self.background_color = (1, 0, 0, 1)
            self.current_color = (1, 0, 0, 1)
        else:
            self.background_color = (0.93,0.93,0.93, 1)
            self.current_color = (0.93,0.93,0.93, 1)
class CartItem_En(BoxLayout):
    item_text = StringProperty()
    on_delete = ObjectProperty(None)