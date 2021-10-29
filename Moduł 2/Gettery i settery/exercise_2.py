class Lightsaber:
    
    def __init__(self, color):
        self.color = color
        
    def __str__(self):
        light_side = ('blue', 'green', 'violet')
        dark_side = ('red')
        if self._color in light_side:
            return f'Lighstaber: {self._color}, force: light'
        if self._color in dark_side:
            return f'Lighstaber: {self._color}, force: dark'
    
    @property
    def side(self):
        light_side = ('blue', 'green', 'violet')
        dark_side = ('red')
        if self._color in light_side:
            return 'light side'
        if self._color in dark_side:
            return 'dark side'

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        colors = ('blue', 'green', 'violet', 'red')
        if color in colors:
            self._color = color
        else:
            raise ValueError('Bad lightsaber color')

a = Lightsaber('blue')
print(a._color)
print(a.color)

