import pygame


class Camera:

    def __init__(self):
        self.cameraX = 0
        self.cameraY = 0

    def CameraMove(self, direction):
        self.cameraX += direction
        if self.cameraX <= 0:
            self.cameraX = 0

    def GetCameraX(self):
        return self.cameraX
