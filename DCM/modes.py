import PySimpleGUI as sg


class Mode:
    def __init__(self):
        self.lower_rate_limit = [30, 35, 40, 45, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,
                                 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
                                 90, 95, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175]
        self.upper_rate_limit = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140,
                                 145, 150, 155, 160, 165, 170, 175]
        self.atrial_amplitude = ["OFF", 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0,
                                 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.5, 4.0, 4.5, 5.0, 5.5,
                                 6.0, 6.5, 7.0]
        self.atrial_pulse_width = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5,
                                   1.6, 1.7, 1.8, 1.9]
        self.ventricular_amplitude = ["OFF", 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9,
                                      2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.5, 4.0, 4.5,
                                      5.0, 5.5, 6.0, 6.5, 7.0]
        self.ventricular_pulse_width = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5,
                                        1.6, 1.7, 1.8, 1.9]
        self.hysteresis = ["OFF", 30, 35, 40, 45, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66,
                           67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
                           90, 95, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175]
        self.rate_smoothing = ["OFF", 3, 6, 9, 12, 15, 18, 21, 25]
        self.atrial_sensitivity = [0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0,
                                   7.5, 8.0, 8.5, 9.0, 9.5, 10.0]
        self.ventricular_sensitivity = [0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5,
                                        7.0,
                                        7.5, 8.0, 8.5, 9.0, 9.5, 10.0]
        self.VRP = [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340,
                    350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 490, 500, 510]
        self.ARP = [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340,
                    350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 490, 500, 510]

    def AOO(self):
        sg.theme('Reddit')

        left_parameters = [
            [sg.Text("Lower Rate Limit (ppm):", pad=(10, 10))],
            [sg.Text("Upper Rate Limit (ppm):", pad=(10, 10))],
        ]

        left_inputs = [
            [sg.Combo(self.lower_rate_limit, key="AOO_LRL", size=(10, 10), pad=(10, 10), readonly=True)],
            [sg.Combo(self.upper_rate_limit, key="AOO_URL", size=(10, 10), pad=(10, 10), readonly=True)],
        ]

        right_parameters = [
            [sg.Text("Atrial Amplitude (V):", pad=(10, 10))],
            [sg.Text("Atrial Pulse Width (ms):", pad=(10, 10))],
        ]

        right_inputs = [
            [sg.Combo(self.atrial_amplitude, key="AOO_AA", size=(10, 10), pad=(10, 10), readonly=True)],
            [sg.Combo(self.atrial_pulse_width, key="AOO_APW", size=(10, 10), pad=(10, 10), readonly=True)],
        ]

        buttons = [
            [sg.Image(key='AOO_LOAD', enable_events=True, tooltip="Load previously sent parameters"),
             sg.Push(),
             sg.Image(key='AOO_SEND', enable_events=True, tooltip="Send parameters to pacemaker")],
        ]

        AOO_layout = [
            [
                sg.Column(left_parameters, pad=(0, 0), expand_x=True, element_justification="left"),
                sg.Column(left_inputs, pad=(0, 0), expand_x=True, element_justification="left"),
                sg.Column(right_parameters, pad=(0, 0), expand_x=True, element_justification="left"),
                sg.Column(right_inputs, pad=(0, 0), expand_x=True, element_justification="left"),
            ],
            [sg.VPush()],
            [sg.Column(buttons, expand_x=True, element_justification="left")]
        ]

        return AOO_layout

    def AAI(self):
        sg.theme('Reddit')

        left_parameters = [
            [sg.Text("Lower Rate Limit (ppm):", pad=(10, 10))],
            [sg.Text("Upper Rate Limit (ppm):", pad=(10, 10))],
            [sg.Text("ARP (ms):", pad=(10, 10))],
            [sg.Text("Hysteresis:", pad=(10, 10))],
        ]

        left_inputs = [
            [sg.Combo(self.lower_rate_limit, key="AAI_LRL", size=(10, 10), pad=(10, 10), readonly=True)],
            [sg.Combo(self.upper_rate_limit, key="AAI_URL", size=(10, 10), pad=(10, 10), readonly=True)],
            [sg.Combo(self.ARP, key="AAI_ARP", size=(10, 10), pad=(10, 10), readonly=True)],
            [sg.Combo(self.hysteresis, key="AAI_H", size=(10, 10), pad=(10, 10), readonly=True)],
        ]

        right_parameters = [
            [sg.Text("Atrial Amplitude (V):", pad=(10, 10))],
            [sg.Text("Atrial Pulse Width (ms):", pad=(10, 10))],
            [sg.Text("Atrial Sensitivity (mV):", pad=(10, 10))],
            [sg.Text("Rate Smoothing (%):", pad=(10, 10))],
        ]

        right_inputs = [
            [sg.Combo(self.atrial_amplitude, key="AAI_AA", size=(10, 10), pad=(10, 10), readonly=True)],
            [sg.Combo(self.atrial_pulse_width, key="AAI_APW", size=(10, 10), pad=(10, 10), readonly=True)],
            [sg.Combo(self.atrial_sensitivity, key="AAI_AS", size=(10, 10), pad=(10, 10), readonly=True)],
            [sg.Combo(self.rate_smoothing, key="AAI_RS", size=(10, 10), pad=(10, 10), readonly=True)],
        ]

        buttons = [
            [sg.Image(key='AAI_LOAD', enable_events=True, tooltip="Load previously sent parameters"),
             sg.Push(),
             sg.Image(key='AAI_SEND', enable_events=True, tooltip="Send parameters to pacemaker")],
        ]

        AAI_layout = [
            [
                sg.Column(left_parameters, pad=(0, 0), expand_x=True, element_justification="left"),
                sg.Column(left_inputs, pad=(0, 0), expand_x=True, element_justification="left"),
                sg.Column(right_parameters, pad=(0, 0), expand_x=True, element_justification="left"),
                sg.Column(right_inputs, pad=(0, 0), expand_x=True, element_justification="left"),
            ],
            [sg.VPush()],
            [sg.Column(buttons, expand_x=True, element_justification="left")]
        ]

        return AAI_layout

    def VOO(self):
        sg.theme('Reddit')

        left_parameters = [
            [sg.Text("Lower Rate Limit (ppm):", pad=(10, 10))],
            [sg.Text("Upper Rate Limit (ppm):", pad=(10, 10))],
        ]

        left_inputs = [
            [sg.Combo(self.lower_rate_limit, key="VOO_LRL", size=(10, 10), pad=(10, 10), readonly=True)],
            [sg.Combo(self.upper_rate_limit, key="VOO_URL", size=(10, 10), pad=(10, 10), readonly=True)],
        ]

        right_parameters = [
            [sg.Text("Ventricular Amplitude (V):", pad=(10, 10))],
            [sg.Text("Ventricular Pulse Width (ms):", pad=(10, 10))],
        ]

        right_inputs = [
            [sg.Combo(self.ventricular_amplitude, key="VOO_VA", size=(10, 10), pad=(10, 10), readonly=True)],
            [sg.Combo(self.ventricular_pulse_width, key="VOO_VPW", size=(10, 10), pad=(10, 10), readonly=True)],
        ]

        buttons = [
            [sg.Image(key='VOO_LOAD', enable_events=True, tooltip="Load previously sent parameters"),
             sg.Push(),
             sg.Image(key='VOO_SEND', enable_events=True, tooltip="Send parameters to pacemaker")],
        ]

        VOO_layout = [
            [
                sg.Column(left_parameters, pad=(0, 0), expand_x=True, element_justification="left"),
                sg.Column(left_inputs, pad=(0, 0), expand_x=True, element_justification="left"),
                sg.Column(right_parameters, pad=(0, 0), expand_x=True, element_justification="left"),
                sg.Column(right_inputs, pad=(0, 0), expand_x=True, element_justification="left"),
            ],
            [sg.VPush()],
            [sg.Column(buttons, expand_x=True, element_justification="left")]
        ]

        return VOO_layout

    def VVI(self):
        sg.theme('Reddit')

        left_parameters = [
            [sg.Text("Lower Rate Limit (ppm):", pad=(10, 10))],
            [sg.Text("Upper Rate Limit (ppm):", pad=(10, 10))],
            [sg.Text("VRP:", pad=(10, 10))],
            [sg.Text("Hysteresis:", pad=(10, 10))],
        ]

        left_inputs = [
            [sg.Combo(self.lower_rate_limit, key="VVI_LRL", size=(10, 10), pad=(10, 10), readonly=True)],
            [sg.Combo(self.upper_rate_limit, key="VVI_URL", size=(10, 10), pad=(10, 10), readonly=True)],
            [sg.Combo(self.VRP, key="VVI_VRP", size=(10, 10), pad=(10, 10), readonly=True)],
            [sg.Combo(self.hysteresis, key="VVI_H", size=(10, 10), pad=(10, 10), readonly=True)],
        ]

        right_parameters = [
            [sg.Text("Ventricular Amplitude (V):", pad=(10, 10))],
            [sg.Text("Ventricular Pulse Width (ms):", pad=(10, 10))],
            [sg.Text("Ventricular Sensitivity (mV):", pad=(10, 10))],
            [sg.Text("Rate Smoothing (%):", pad=(10, 10))],
        ]

        right_inputs = [
            [sg.Combo(self.ventricular_amplitude, key="VVI_VA", size=(10, 10), pad=(10, 10), readonly=True)],
            [sg.Combo(self.ventricular_pulse_width, key="VVI_VPW", size=(10, 10), pad=(10, 10), readonly=True)],
            [sg.Combo(self.ventricular_sensitivity, key="VVI_VS", size=(10, 10), pad=(10, 10), readonly=True)],
            [sg.Combo(self.rate_smoothing, key="VVI_RS", size=(10, 10), pad=(10, 10), readonly=True)],

        ]

        buttons = [
            [sg.Image(key='VVI_LOAD', enable_events=True, tooltip="Load previously sent parameters"),
             sg.Push(),
             sg.Image(key='VVI_SEND', enable_events=True, tooltip="Send parameters to pacemaker")],
        ]

        VVI_layout = [
            [
                sg.Column(left_parameters, pad=(0, 0), expand_x=True, element_justification="left"),
                sg.Column(left_inputs, pad=(0, 0), expand_x=True, element_justification="left"),
                sg.Column(right_parameters, pad=(0, 0), expand_x=True, element_justification="left"),
                sg.Column(right_inputs, pad=(0, 0), expand_x=True, element_justification="left"),
            ],
            [sg.VPush()],
            [sg.Column(buttons, expand_x=True, element_justification="left")]
        ]

        return VVI_layout
