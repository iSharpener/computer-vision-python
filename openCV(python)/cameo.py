# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 19:48:57 2018

@author: Xiaopeng
"""

import cv2
from captureManager import WindowManager,CaptureManager

class Cameo(object):
    def __init__(self):
        self._windowManager = WindowManager('Cameo',self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0),
                    self._windowManager,True)
        
    def run(self):
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            
            self._captureManager.exitFrame()
            self._windowManager.processEvents()
    def onKeypress(self,keycode):
        if keycode == 32:
            self._captureManager.writeImage('screenshot.png')
        elif keycode == 9:
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('screenshot.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27:
            self._windowManager.destoryWindow()
if __name__=="__main__":
    cam = Cameo()
    cam.run()