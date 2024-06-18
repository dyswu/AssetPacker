# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:04:11 2024

Generate DB to store files

@author: derew
"""


import pandas as pd
import hashlib
import databases

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.button import Button

kv = Builder.load_string(
"""
BoxLayout:
    orientation: "vertical"
    padding: dp(50)
    spacing: dp(20)
    canvas.before:
        Color:
            rgba: .5, 0, 0, 1
        Rectangle:
            size: self.size
            pos: self.pos
    Label:
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                size: dp(100), dp(100)
                pos: self.pos
        text: "Title"
        color: 1, 1, 1, 1
        halign: "center"
        
    Button:
        text: "Button 1"
        size_hint: 0.25, 0.25
    Button:
        text: "Button 2"
        size_hint: 1, 0.5
        color: 1, 1, 1, 1
        background_color: 0.5, .7, 1, 1
    Button:
        text: "Button 3"
        size_hint: None, None
        size: dp(300), dp(300)
        color: 1, 1, 1, 1
        background_color: 1, 1, 1, 1
        background_normal: 'button_clicked.png'
        background_down: ''
        on_press: print("Button 3 pressed")
        on_release: print("Button 3 released")
    Label:
        text: "Normal Text"
    Label:
        text: "Green Text"
        color: 0,1,0,1
        size_hint: 0.25, 0.25
    Label:
        text: "Big Green Text"
        color: 0,1,0,1
        font_size: dp(10)
    Label:
        text: "A very long text that does not fit in the screen"
        font_size: dp(42)
        text_size: root.width, None
    Label:
        text: "Text with [b]bold[/b], [i]italic[/i], [u]underline[/u], [s]strikethrough[/s] and [color=ff0000]red[/color] text that fit on the screen"
        font_size: dp(35)
        markup: True
        halign: "center"
        text_size: root.width, None
"""
)

class MenuApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    MenuApp().run()
    
 