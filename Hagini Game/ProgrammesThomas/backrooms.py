from win32api import GetSystemMetrics
import pygame as pyg

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
pyg.init()
pyg.font.init()
pyg.display.set_caption('hagini game')
screen = pyg.display.set_mode((width,height), 0, 32)
clock = pyg.time.Clock()