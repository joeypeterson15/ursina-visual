from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
# '''example of inheriting Entity'''

app = Ursina()

class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model='sphere'
        self.texture='shore'
        self.color = color.red
        self.scale_y = 1
        self.shader='lit_with_shadows_shader'
        self.texture_scale=(10,10)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def input(self, key):
        if key == 'space':
            self.animate_x(2, duration=1)

    def update(self):
        self.x += held_keys['d'] * time.dt * 10
        self.x -= held_keys['a'] * time.dt * 10

player = Player(x=-1)
app.run()


# player = FirstPersonController()

# sphere = Entity(
#     model='sphere',
#     texture='shore',  # Use 'shore' or any other texture
#     scale=(1, 1, 1),
#     position=(0, 1, 5)
# )

# app.run()
