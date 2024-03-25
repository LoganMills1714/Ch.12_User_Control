"""
USER CONTROL PROJECT
-----------------
Your choice!!! Have fun and be creative.
Create a background and perhaps animate some objects.
Pick a user control method and navigate an object around your screen.
Make your object more interesting than a ball.
Create your object with a new class.
Perhaps move your object through a maze or move the object to avoid other moving objects.
Incorporate some sound.
Type the directions to this project below:

DIRECTIONS:
----------
Please type directions for this game here.

Use A and D to move left and right and W to jump, avoid the spikes and get to the end
"""

import arcade
from time import sleep

SW = 1280  # Define Window Size
SH = 720
SPEED = 3  # Define speed of cube
JUMP_SPEED = 4.4  # Define jump speed (Basically height)


class Cube:
    def __init__(self, pos_x, pos_y, dx, dy, side, col, col2):  # Initialize variables and sounds
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.side = side
        self.col = col
        self.col2 = col2
        self.explosion_sound = arcade.load_sound("explode_11.ogg", False)  # Death Sound
        self.complete = arcade.load_sound("endStart_02.ogg")  # Complete Sound
        self.music = arcade.load_sound("StereoMadness.mp3", False)  # Running Music (Stereo Madness)
        self.music.play(0.4, 0, True)  # Play the music

    def draw_cube(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.side, self.side, self.col)  # Main Cube
        arcade.draw_rectangle_outline(self.pos_x, self.pos_y, self.side, self.side, arcade.color.BLACK)  # Cube outline
        arcade.draw_rectangle_filled(self.pos_x - 7, self.pos_y + 7, 7, 7, self.col2)  # Eyes and eye outlines
        arcade.draw_rectangle_outline(self.pos_x - 7, self.pos_y + 7, 7, 7, arcade.color.BLACK)
        arcade.draw_rectangle_filled(self.pos_x + 7, self.pos_y + 7, 7, 7, self.col2)
        arcade.draw_rectangle_outline(self.pos_x + 7, self.pos_y + 7, 7, 7, arcade.color.BLACK)
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y - 5, 26, 7, self.col2)  # Mouth and mouth outline
        arcade.draw_rectangle_outline(self.pos_x, self.pos_y - 5, 26, 7, arcade.color.BLACK)

    def update_cube(self):
        self.pos_y += self.dy  # Move the cube up and down according to velocity
        self.pos_x += self.dx  # Move the cube left and right according to velocity

        self.dy -= 0.1  # Continually move the cube down to give gravity
        if self.pos_y <= 240:  # If at the floor don't move down anymore
            self.dy = 0
            self.pos_y = 240  # Don't go inside the floor

        if self.pos_x < self.side/2: # Left wall barrier
            self.pos_x = self.side/2

        if self.pos_x > SW-self.side/2:  # Right wall barrier
            self.pos_x = SW-self.side/2

        if self.pos_x > 300 and self.pos_x < 420 and self.pos_y < 280:  # First triple spike collision detection
            arcade.play_sound(self.explosion_sound)  # If collided with spikes play death sound
            self.pos_x = 100  # Restart to original position
            self.pos_y = 240

        if self.pos_x > 600 and self.pos_x < 720 and self.pos_y < 280:  # Second triple spike collision detection
            arcade.play_sound(self.explosion_sound)  # If collided with spikes play death sound
            self.pos_x = 100  # Restart to original position
            self.pos_y = 240

        if self.pos_x > 900 and self.pos_x < 1020 and self.pos_y < 280:  # Third triple spike collision detection
            arcade.play_sound(self.explosion_sound)  # If collided with spikes play death sound
            self.pos_x = 100  # Restart to original position
            self.pos_y = 240

        if self.pos_x >= 1200:  # If at end of level
            arcade.play_sound(self.complete)  # Play complete sound
            sleep(5)
            exit()


class MyGame(arcade.Window):
    def __init__(self, width, height, title):  # Define variables and textures
        super().__init__(width, height, title)
        self.cube = Cube(100, 240, 0, 0, 40, (251, 196, 0), (1, 254, 255))  # Setting variables for cube
        self.background = arcade.load_texture("BACKGROUND.jpg")
        self.checkpoint = arcade.load_texture("CHECKPOINT.png")

    def on_draw(self):
        arcade.start_render()  # Start drawing things
        arcade.draw_texture_rectangle(SW / 2, SH / 2, 1280, 720, self.background)  # Draw the background
        arcade.draw_texture_rectangle(1200, 260, 20, 40, self.checkpoint)  # Draw the checkpoint at the end

        self.cube.draw_cube()  # Draw cube with variables given in __init__

        arcade.draw_rectangle_filled(640, 100, 1280, 240, (136, 1, 202))  # Big block for ground
        for i in range(25, 1500, 220):  # Create squares for ground
            arcade.draw_rectangle_filled(i, 100, 200, 200, (108, 1, 164))  # Smaller squares for ground

        for i in range(300, 400, 40):  # Make a triple spike
            arcade.draw_triangle_filled(i, 220, i+20, 260, i+40, 220, arcade.color.BLACK)  # Black triangle
            arcade.draw_triangle_outline(i, 220, i + 20, 260, i + 40, 220, arcade.color.WHITE)  # White outline

        for i in range(600, 700, 40):  # Make a triple spike
            arcade.draw_triangle_filled(i, 220, i+20, 260, i+40, 220, arcade.color.BLACK)  # Black triangle
            arcade.draw_triangle_outline(i, 220, i + 20, 260, i + 40, 220, arcade.color.WHITE)  # White outline

        for i in range(900, 1000, 40):  # Make a triple spike
            arcade.draw_triangle_filled(i, 220, i+20, 260, i+40, 220, arcade.color.BLACK)  # Black triangle
            arcade.draw_triangle_outline(i, 220, i + 20, 260, i + 40, 220, arcade.color.WHITE)  # White outline

    def on_update(self, dt):
        self.cube.update_cube()  # Update cube each frame

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.A:  # If A pressed go left at speed defined at top of file
            self.cube.dx = -SPEED
        elif key == arcade.key.D:  # If D pressed go left at speed defined at top of file
            self.cube.dx = SPEED
        elif key == arcade.key.W:  # If W pressed go up (Will go back down due to gravity statement earlier)
            if self.cube.pos_y == 240:  # Make sure cube is on the ground before jumping
                self.cube.dy = JUMP_SPEED

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.A or key == arcade.key.D:  # Allow cube to stop going sideways if key is released
            self.cube.dx = 0


def main():
    MyGame(SW, SH, "Bootleg Geometry Dash")  # Instantiate the game class with our width, height, and title
    arcade.run()


if __name__ == "__main__":  # Run the program
    main()
