import PySimpleGUI as sg
from PIL import Image, ImageTk
from modes import *


class Layout:
    def __init__(self):
        self.hello = "Hello"

    def welcome(self):
        top = [
            [sg.Image(key='LAUNCH_IMAGE')]
        ]

        bottom = [
            [sg.Button("Login", size=(15, 1), pad=(25, 0), button_color='Black on White', bind_return_key=True,
                       key="LOGIN"),
             sg.Button("Register", size=(15, 1), pad=(25, 0), button_color='Black on White', bind_return_key=True,
                       key="REGISTER")]
        ]

        layout = [
            [sg.Column(top, background_color="Black")],
            [sg.Column(bottom, background_color="Black", expand_x=True, element_justification="center")]
        ]

        return layout

    def login(self):
        left_side = [
            [sg.Image(key='LOGIN_IMAGE', background_color="Black")]
        ]

        login_button = [
            [sg.Button("Login", size=(25, 1), pad=(5, 5), button_color='Black', bind_return_key=True, border_width=3)]
        ]

        register_button = [
            [sg.Text("Back", enable_events=True, key="BACK", text_color='#007ad2')],
        ]

        right_side = [
            [sg.Text("Username:")],
            [sg.InputText(key="USER", size=(30, 40), do_not_clear=False, pad=(10, 10))],
            [sg.Text("Password:")],
            [sg.InputText(key="PASS", password_char="*", size=(30, 40), do_not_clear=False, pad=(10, 10))],
            [sg.Column(login_button, element_justification='center', expand_x=True)],
            [sg.Column(register_button, element_justification='center', expand_x=True)],
        ]

        column2 = [
            [sg.Column(right_side)]
        ]

        main = [
            [sg.Column(column2, expand_x=True, element_justification="center")]
        ]

        layout = [
            [sg.Column(left_side),
             sg.Column(main, pad=(20, 20), expand_x=True, element_justification="center"),
             ]
        ]

        return layout

    def register(self):
        left_side = [
            [sg.Image(key='REGISTER_IMAGE')]
        ]

        register_button = [
            [sg.Button("Register", size=(25, 1), pad=(5, 5), button_color='Black', bind_return_key=True,
                       border_width=3)]
        ]

        back_button = [
            [sg.Text("Back", enable_events=True, key="BACK", text_color='#007ad2')],
        ]

        right_side = [
            [sg.Text("Username:")],
            [sg.InputText(key="USER", size=(30, 40), do_not_clear=True, pad=(10, 10))],
            [sg.Text("Password:")],
            [sg.InputText(key="PASS", password_char="*", size=(30, 40), do_not_clear=False, pad=(10, 10))],
            [sg.Text("Reenter Password:")],
            [sg.InputText(key="REENTER", password_char="*", size=(30, 40), do_not_clear=False, pad=(10, 10))],
            [sg.Column(register_button, element_justification='center', expand_x=True)],
            [sg.Column(back_button, element_justification='center', expand_x=True)]
        ]

        column2 = [
            [sg.Column(right_side)]
        ]

        main = [
            [sg.Column(column2, expand_x=True, element_justification="center")]
        ]

        layout = [
            [sg.Column(left_side),
             sg.Column(main, pad=(20, 20), expand_x=True, element_justification="Center"),
             ]
        ]

        return layout



