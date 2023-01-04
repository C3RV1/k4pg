import k4pg
import pygame as pg


class ButtonText(k4pg.Button, k4pg.Text):
    def __init__(self, *args, pressed_color: pg.Color = None,
                 hover_color: pg.Color = None, not_pressed_color: pg.Color = None, **kwargs):
        self._pressed_color = pressed_color
        self._hover_color = hover_color
        self._not_pressed_color = not_pressed_color
        super(ButtonText, self).__init__(*args, **kwargs)
        self.color = self._not_pressed_color

    def get_hover(self, cam):
        if not self.visible:
            return False
        mouse_pos = self.inp.get_mouse_pos()
        if self.get_screen_rect(cam)[0].collidepoint(mouse_pos[0], mouse_pos[1]):
            return True
        return False

    def get_press(self):
        if self.inp.get_mouse_up(1):
            return True
        return False

    def on_not_pressed(self):
        if self._not_pressed_color:
            self.color = self._not_pressed_color

    def on_pressed(self):
        if self._pressed_color:
            self.color = self._pressed_color

    def on_hover(self):
        if self._hover_color:
            self.color = self._hover_color

    @property
    def not_pressed_color(self):
        return self._not_pressed_color

    @not_pressed_color.setter
    def not_pressed_color(self, v: str):
        self._not_pressed_color = v
        if not self._pressed:
            self.color = v

    @property
    def pressed_color(self):
        return self._pressed_color

    @pressed_color.setter
    def pressed_color(self, v: str):
        self._pressed_color = v
        if self._pressed:
            self.color = v

    @property
    def hover_color(self):
        return self._hover_color

    @hover_color.setter
    def hover_color(self, v: str):
        self._hover_color = v
        if self._hovering:
            self.color = v
