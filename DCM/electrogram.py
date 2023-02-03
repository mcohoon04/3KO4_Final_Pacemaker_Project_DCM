#!/usr/bin/env python
import PySimpleGUI as sg
from random import randint
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, FigureCanvasAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from datetime import datetime
from itertools import count
from random import random
from matplotlib.animation import FuncAnimation


def currentTime():
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%H:%M:%S")
    return timestampStr


# Yet another usage of MatPlotLib with animations.

def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def graph(window):
    NUM_DATAPOINTS = 10000
    # define the form layout

    canvas_elem = window['CANVAS1']
    canvas = canvas_elem.TKCanvas

    canvas_elem = window['CANVAS2']
    canvas2 = canvas_elem.TKCanvas

    # draw the initial plot in the window
    fig = Figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.grid()
    fig_agg = draw_figure(canvas, fig)
    fig_agg2 = draw_figure(canvas2, fig)

    # make a bunch of random data points
    dpts = [randint(-1, 5) for x in range(NUM_DATAPOINTS)]

    for i in range(len(dpts)):
        event, values = window.read(timeout=10)
        if event in ('Exit', None):
            exit(69)
        if event == "STOP":
            break
        ax.cla()  # clear the subplot
        ax.grid()  # draw the grid
        data_points = 50  # draw this many data points (on next line)
        ax.plot(range(data_points), dpts[i:i + data_points], color='#007ad2')
        fig_agg.draw()
        fig_agg2.draw()

    del(fig)
    window.refresh()
