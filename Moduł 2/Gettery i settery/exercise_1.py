class Lightsaber:
    
    def __init__(self, color):
        self._color = color
        
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
       

a = Lightsaber('blue')
print(a)
print(a.side)
        
