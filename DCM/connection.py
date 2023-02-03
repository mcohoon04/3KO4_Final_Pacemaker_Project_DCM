import serial
import struct
from time import sleep
import json


class Connect:
    def __init__(self, com):
        # set port for laptop being used
        self.frdm_port = com
        # set baud rate for the device
        self.baud = 115200

    def is_connected(self):
        # CODE LINE ADDED FOR SHOWING CODE WITHOUT PACEMAKER
        return True
        # # create object pacemaker for serial communication
        # pacemaker = serial.Serial(self.frdm_port, self.baud)
        # pacemaker.reset_input_buffer()
        # pacemaker.reset_output_buffer()
        # if pacemaker.isOpen():
        #     pacemaker.close()
        #     return True
        # else:
        #     pacemaker.close()
        #     return False

    def send_para(self, mode, user):
        # CODE LINE ADDED FOR SHOWING CODE WITHOUT PACEMAKER
        return True
        # # create object pacemaker for serial communication
        # pacemaker = serial.Serial(self.frdm_port, self.baud)
        # pacemaker.reset_input_buffer()
        # pacemaker.reset_output_buffer()
        # print("%b" + '\n', pacemaker.isOpen())
        #
        # # open json to be read from
        # f = open("data/data.json", "r+")
        # data = json.load(f)
        #
        # # initialize variables
        # para = b'\x00'
        # para_check = b'\x00'
        #
        # if mode == 1:
        #     LRL = struct.pack("B", int(data[user]["VOO"]["LRL"]))
        #     URL = struct.pack("B", int(data[user]["VOO"]["URL"]))
        #     VA = struct.pack("f", float(data[user]["VOO"]["VA"]))
        #     # additional rounding needed for PW
        #     PW = round(data[user]["VOO"]["VPW"])
        #     if PW == 0:
        #         PW = 1
        #     VPW = struct.pack("H", PW)
        #     VS = struct.pack("f", float(1.0))
        #     VRP = struct.pack("H", int(170))
        #     AT = b'\x00'
        #     RT = b'\x00'
        #     RF = b'\x00'
        #     RspT = b'\x00'
        #     para = b'\x16' + b'\x55' + b'\x01' + LRL + URL + VA + VPW + VS + VRP
        #     para_check = b'\x01' + LRL + URL + VA + VPW + VS + VRP
        #     # AT + RT + RF + RspT
        #
        # if mode == 2:
        #     LRL = struct.pack("B", int(data[user]["AOO"]["LRL"]))
        #     URL = struct.pack("B", int(data[user]["AOO"]["URL"]))
        #     AA = struct.pack("f", float(data[user]["AOO"]["AA"]))
        #     # additional rounding needed for PW
        #     PW = round(data[user]["AOO"]["APW"])
        #     if PW == 0:
        #         PW = 1
        #     APW = struct.pack("H", PW)
        #     AS = struct.pack("f", float(1.0))
        #     ARP = struct.pack("H", int(170))
        #     AT = b'\x00'
        #     RT = b'\x00'
        #     RF = b'\x00'
        #     RspT = b'\x00'
        #     para = b'\x16' + b'\x55' + b'\x02' + LRL + URL + AA + APW + AS + ARP
        #     para_check = b'\x02' + LRL + URL + AA + APW + AS + ARP
        #     # AT + RT + RF + RspT
        #
        # if mode == 3:
        #     LRL = struct.pack("B", int(data[user]["VVI"]["LRL"]))
        #     URL = struct.pack("B", int(data[user]["VVI"]["URL"]))
        #     VA = struct.pack("f", float(data[user]["VVI"]["VA"]))
        #     # additional rounding needed for PW
        #     PW = round(data[user]["VVI"]["VPW"])
        #     if PW == 0:
        #         PW = 1
        #     VPW = struct.pack("H", PW)
        #     VS = struct.pack("f", float(data[user]["VVI"]["VS"]))
        #     VRP = struct.pack("H", int(data[user]["VVI"]["VRP"]))
        #     AT = b'\x00'
        #     RT = b'\x00'
        #     RF = b'\x00'
        #     RspT = b'\x00'
        #     para = b'\x16' + b'\x55' + b'\x03' + LRL + URL + VA + VPW + VS + VRP
        #     para_check = b'\x03' + LRL + URL + VA + VPW + VS + VRP
        #     # + AT + RT + RF + RspT
        #
        # if mode == 4:
        #     LRL = struct.pack("B", int(data[user]["AAI"]["LRL"]))
        #     URL = struct.pack("B", int(data[user]["AAI"]["URL"]))
        #     AA = struct.pack("f", float(data[user]["AAI"]["AA"]))
        #     # additional rounding needed for PW
        #     PW = round(data[user]["AAI"]["APW"])
        #     if PW == 0:
        #         PW=1
        #     APW = struct.pack("H", PW)
        #     AS = struct.pack("f", float(data[user]["AAI"]["AS"]))
        #     ARP = struct.pack("H", int(data[user]["AAI"]["ARP"]))
        #     AT = b'\x00'
        #     RT = b'\x00'
        #     RF = b'\x00'
        #     RspT = b'\x00'
        #     para = b'\x16' + b'\x55' + b'\x04' + LRL + URL + AA + APW + AS + ARP
        #     para_check = b'\x04' + LRL + URL + AA + APW + AS + ARP
        #     # + AT + RT + RF + RspT
        #
        # tries = 0
        # while pacemaker.in_waiting == 0:
        #     pacemaker.write(para)
        #     tries += 1
        #     sleep(0.01)
        #     if (tries == 500): # 5 SECONDS
        #         print("you suck, horribly.\n\there are your stinky numbers.")
        #         print(para)
        #         return False
        # print(tries)
        #
        # # sleep(0.1)
        # # TO-DO: check to see if echo matches the write
        # print(para_check)
        # echo_check = pacemaker.read(16)
        # print("echo'd data for check")
        # print(echo_check)
        # pacemaker.close()
        #
        # if para_check:
        #     return True
        # else:
        #     return False

    def rqst_para(self, user):
        # # create object pacemaker for serial communication and ensure the line is open
        # pacemaker = serial.Serial(self.frdm_port, self.baud)
        # pacemaker.reset_input_buffer()
        # pacemaker.reset_output_buffer()
        # print("%b" + '\n', pacemaker.isOpen())
        #
        # # send the data to request parameters
        # send = b'\x16' + b'\x49' + b'\x01' + b'\x01' + b'\x01' + b'\x01' + b'\x01' + b'\x01' + b'\x01' + b'\x01' + b'\x01' + b'\x01' + b'\x01' + b'\x01' + b'\x01' + b'\x01' + b'\x01'
        # pacemaker.write(send)
        #
        # print("write done")
        # # open data json file to be edited
        # f = open("data/data.json", "r+")
        # data = json.load(f)
        #
        # # obtain mode the pacemaker is in to know what parameters are being recieved
        # para = pacemaker.read(16)
        # print(para)
        # mode = para[0]
        # print(mode)
        #
        # if mode == 1:
        #     # VOO
        #     data[user]["VOO"] = {
        #         "LRL": para[1],
        #         "URL": para[2],
        #         "VA": struct.unpack("f", para[3:7])[0],
        #         "VPW": struct.unpack("H", para[7:9])[0]
        #     }
        # if mode == 2:
        #     # AOO
        #     data[user]["AOO"] = {
        #         "LRL": para[1],
        #         "URL": para[2],
        #         "AA": struct.unpack("f", para[3:7])[0],
        #         "APW": struct.unpack("H", para[7:9])[0]
        #     }
        # if mode == 3:
        #     # VVI
        #     data[user]["VVI"] = {
        #         "LRL": para[1],
        #         "URL": para[2],
        #         "VA": struct.unpack("f", para[3:7])[0],
        #         "VPW": struct.unpack("H", para[7:9])[0],
        #         "VS": struct.unpack("f", para[9:13])[0],
        #         "VRP": struct.unpack("H", para[13:15])[0],
        #         "H": data[user]["VVI"]["H"],
        #         "RS": data[user]["VVI"]["RS"]
        #     }
        #
        # if mode == 4:
        #     # AAI
        #     data[user]["AAI"] = {
        #         "LRL": para[1],
        #         "URL": para[2],
        #         "AA": struct.unpack("f", para[3:7])[0],
        #         "APW": struct.unpack("H", para[7:9])[0],
        #         "AS": struct.unpack("f", para[9:13])[0],
        #         "ARP": struct.unpack("H", para[13:15])[0],
        #         "H": data[user]["AAI"]["H"],
        #         "RS": data[user]["AAI"]["RS"]
        #     }
        #
        # open("data/data.json", "w").write(json.dumps(data, indent=4, separators=(',', ': ')))
        #
        # # close port
        # pacemaker.close()
        #
        # # return mode to be used by main class
        # return mode
        # CODE LINE ADDED FOR SHOWING CODE WITHOUT PACEMAKER
        return 1

    def rqst_egram(self):
        # create object pacemaker for serial communication and ensure the line is open
        # pacemaker = serial.Serial(self.frdm_port, self.baud)
        # #pacemaker.reset_input_buffer()
        # #pacemaker.reset_output_buffer()
        # print("%b" + '\n', pacemaker.isOpen())
        #
        # # ask for egram data
        #
        # pacemaker.write(
        #     b'\x16' + b'\x47' + b'\x00' + b'\x00' + b'\x00' + b'\x00' + b'\x00' + b'\x00' + b'\x00' + b'\x00' + b'\x00'+ b'\x00' + b'\x00' + b'\x00' + b'\x00' + b'\x00' + b'\x00'
        # )
        # # format data being received
        # data = pacemaker.read(16)
        # print("read data")
        # a_volt = struct.unpack("d", data[0:8])[0]
        # v_volt = struct.unpack("d", data[8:16])[0]
        #
        # volts = [(10*a_volt)-5, (10*v_volt)-5]
        #
        # # close port
        # pacemaker.close()
        # return volts
        return [(10 * 1) - 5, (10 * 1) - 5]

    def egram_data(self):
        # # create object pacemaker for serial communication and ensure the line is open
        # pacemaker = serial.Serial(self.frdm_port, self.baud)
        # pacemaker.reset_input_buffer()
        # pacemaker.reset_output_buffer()
        #
        # # format data being received
        # data = pacemaker.read(16)
        # print("read data")
        # a_volt = struct.unpack("d", data[0:8])[0]
        # v_volt = struct.unpack("d", data[8:16])[0]
        #
        # # volts = [(10*a_volt)-5, (10*v_volt)-5]
        # volts = [a_volt, v_volt]
        # # close port
        # pacemaker.close()
        #
        # # return voltages to be used in egram
        # return volts
        return [(10*1)-5, (10*1)-5]

    def stop_egram(self):
        x=1
        # # create object pacemaker for serial communication and ensure the line is open
        # pacemaker = serial.Serial(self.frdm_port, self.baud)
        # pacemaker.reset_input_buffer()
        # pacemaker.reset_output_buffer()
        # print("%b" + '\n', pacemaker.isOpen())
        #
        # # stop egram data
        # pacemaker.write(
        #     b'\x16' + b'\x62' + b'\x00' + b'\x00' + b'\x00' + b'\x00' + b'\x00' + b'\x00' + b'\x00' + b'\x00' + b'\x00'
        #     + b'\x00' + b'\x00' + b'\x00' + b'\x00' + b'\x00' + b'\x00'
        # )
        #
        # # close port
        # pacemaker.close()

