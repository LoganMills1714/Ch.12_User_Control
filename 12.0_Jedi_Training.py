"""
# 12.0 Jedi Training (10 pts)  Name:Logan Mills
 
Update the code in this chapter to do the following:
Open a 500px by 500px window.
Change the Ball class to a Box class.
Instantiate two 30px by 30px boxes. One red and one blue.
Make the blue box have a speed of 240 pixels/second
Make the red box have a speed of 180 pixels/second
Control the blue box with the arrow keys.
Control the red box with the WASD keys.
Do not let the boxes go off of the screen.
Incorporate different sounds when either box hits the edge of the screen.
Have two people play this TAG game at the same time.
The red box is always "it" and needs to try to catch the blue box.
When you're done demonstrate to your instructor!


Starter Testing Code:
"""
import arcade
SW = 500
SH = 500
RED_SPEED = 3
BLUE_SPEED = 4

class Box:
    def __init__(self, pos_x, pos_y, dx, dy, rad, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col
        self.laser_sound = arcade.load_sound("laser.wav", False)
        self.explosion_sound = arcade.load_sound("explosion.wav", False)

    def draw_box(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.rad, self.rad, self.col)

    def update_box(self):
        self.pos_y += self.dy
        self.pos_x += self.dx

        if self.pos_x < self.rad/2:
            self.pos_x = self.rad/2
            arcade.play_sound(self.laser_sound)
            self.dx = 0
        if self.pos_x > SW - self.rad/2:
            self.pos_x = SW - self.rad/2
            arcade.play_sound(self.laser_sound)
            self.dx = 0
        if self.pos_y < self.rad/2:
            self.pos_y = self.rad/2
            arcade.play_sound(self.explosion_sound)
            self.dy = 0
        if self.pos_y > SH - self.rad/2:
            self.pos_y = SH - self.rad/2
            arcade.play_sound(self.explosion_sound)
            self.dy = 0

        #bounce off edge of screen
        # if self.pos_x < self.rad or self.pos_x > SW - self.rad:
        #     self.dx *= -1
        # if self.pos_y < self.rad or self.pos_y > SH - self.rad:
        #     self.dy *= -1

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.set_mouse_visible(True)
        self.redbox = Box(50, 250, 0, 0, 30, arcade.color.RED)
        self.bluebox = Box(450, 250, 0, 0, 30, arcade.color.BLUE)

    def on_draw(self):
        arcade.start_render()
        self.redbox.draw_box()
        self.bluebox.draw_box()

    def on_update(self, dt):
        self.redbox.update_box()
        self.bluebox.update_box()


    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.A:
            self.redbox.dx = -RED_SPEED
        elif key == arcade.key.D:
            self.redbox.dx = RED_SPEED
        elif key == arcade.key.S:
            self.redbox.dy = -RED_SPEED
        elif key == arcade.key.W:
            self.redbox.dy = RED_SPEED

        if key == arcade.key.LEFT:
            self.bluebox.dx = -BLUE_SPEED
        elif key == arcade.key.RIGHT:
            self.bluebox.dx = BLUE_SPEED
        elif key == arcade.key.DOWN:
            self.bluebox.dy = -BLUE_SPEED
        elif key == arcade.key.UP:
            self.bluebox.dy = BLUE_SPEED

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.A or key == arcade.key.D:
            self.redbox.dx = 0
        elif key == arcade.key.S or key == arcade.key.W:
            self.redbox.dy = 0

        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.bluebox.dx = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.bluebox.dy = 0


        

def main():
    window = MyGame(SW, SH, "User Control Practice")
    arcade.run()

if __name__=="__main__":
    main()
