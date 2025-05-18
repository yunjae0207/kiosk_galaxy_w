from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, SwapTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.label import Label
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from screen import Screen_First
from kivy.factory import Factory
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.properties import ListProperty
from kivy.core.window import Window

import os
import sys


# MyApp 
class MyApp(App):
    def build(self):
        Window.size = (1920, 1080)
        return Builder.load_file('screen.kv')

    def show_popup_store(self, item_text):
        self.popup_store_instance = Factory.Popup_Store()
        self.popup_store_instance.popup_store_label_first.text = item_text
        self.popup_store_instance.open()

    def show_popup_pay(self, item_text):
        self.popup_pay_instance = Factory.Popup_Pay()
        self.popup_pay_instance.popup_pay_label_first.text = item_text
        self.popup_pay_instance.open()
    
    def show_popup_store_en(self, item_text):
        self.popup_store_en_instance = Factory.Popup_Store_En()
        self.popup_store_en_instance.popup_store_en_label_first.text = item_text
        self.popup_store_en_instance.open()

    def show_popup_pay_en(self, item_text):
        self.popup_pay_en_instance = Factory.Popup_Pay_En()
        self.popup_pay_en_instance.popup_pay_en_label_first.text = item_text
        self.popup_pay_en_instance.open() 
        
    def change_mainscreen_fourth(self):
        self.root.current = 'fourth'
    def change_mainscreen_sixth(self):
        self.root.current = 'sixth'
    def change_mainscreen_tenth(self):
        self.root.current = 'tenth'
    def change_mainscreen_twelfth(self):
        self.root.current = 'twelfth'
    def change_mainscreen_zero(self):
        pass
        #Clock.schedule_once(lambda dt: self.current = 'sixth', 3)

    def add_item(self):
        popup = self.popup_store_instance  # ← 사용자가 실제 보고 있는 팝업
        new_item = popup.popup_store_label_first.text
        fourth_screen = self.root.get_screen('fourth')
        if new_item:
            fourth_screen.cart_items.append(new_item)
            fourth_screen.refresh_view()

    def add_item_en(self):
        popup = self.popup_store_en_instance  # ← 사용자가 실제 보고 있는 팝업
        new_item = popup.popup_store_en_label_first.text
        tenth_screen = self.root.get_screen('tenth')
        if new_item:
            tenth_screen.cart_items_en.append(new_item)
            tenth_screen.refresh_view()




    scheduled_popup_closure = None

    def close_existing_popup(self, root):
        if root and root._window:  # 팝업이 열려 있는 상태인지 확인
            if self.scheduled_popup_closure:
                Clock.unschedule(self.scheduled_popup_closure)
            self.scheduled_popup_closure = Clock.schedule_once(lambda dt: (root.dismiss(), self.change_mainscreen_sixth()), 4)

    def cancel_scheduled_popup_close(self):
        if self.scheduled_popup_closure:
            Clock.unschedule(self.scheduled_popup_closure)
            self.scheduled_popup_closure = None

    def delete_all_items(self):
        fourth_screen = self.root.get_screen('fourth')
        fourth_screen.clear_all_items()
        fourth_screen.refresh_view()

    def delete_all_items_en(self):
        tenth_screen = self.root.get_screen('tenth')
        tenth_screen.clear_all_items()
        tenth_screen.refresh_view()

    
    def close_existing_popup_en(self, root):
        if root and root._window:  # 팝업이 열려 있는 상태인지 확인
            if self.scheduled_popup_closure:
                Clock.unschedule(self.scheduled_popup_closure)
            self.scheduled_popup_closure = Clock.schedule_once(lambda dt: (root.dismiss(), self.change_mainscreen_twelfth()), 4)

    def cancel_scheduled_popup_en_close(self):
        if self.scheduled_popup_closure:
            Clock.unschedule(self.scheduled_popup_closure)
            self.scheduled_popup_closure = None


        




class ReloadHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.src_path.endswith(".py") or event.src_path.endswith(".kv"):
            print("starting")
            os.execv(sys.executable, ['python'] + sys.argv)


observer = Observer()
observer.schedule(ReloadHandler(), '.', recursive=True)
observer.start()

try:
    MyApp().run()  
finally:
    observer.stop()
    observer.join()