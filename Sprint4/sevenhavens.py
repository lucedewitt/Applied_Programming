import arcade

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Platformer"

# Constants used to scale our sprites from their original size
TILE_SCALING = 0.5

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

class GameView(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

        # Load the game's background music and start it looping when the window opens.
        self.background_music = arcade.load_sound("game-music.mp3")
        self.music_player = arcade.play_sound(self.background_music, loop=True)

        # Textures for the player's left- and right-facing directions
        self.player_texture_left = arcade.load_texture(
            "jae-sprites/sprite_jae2.png"
        )
        self.player_texture_right = arcade.load_texture(
            "jae-sprites/sprite_jae3.png"
        )
        self.player_texture_idle_left = arcade.load_texture(
            "jae-sprites/sprite_jae1.png"
        )
        self.player_texture_idle_right = arcade.load_texture(
            "jae-sprites/sprite_jae0.png"
        )

        # Separate variable that holds the player sprite
        self.player_sprite = arcade.Sprite(self.player_texture_idle_right)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_facing = "right"
        self.left_pressed = False
        self.right_pressed = False

        # SpriteList for our player
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        # SpriteList for our boxes and ground
        # Putting our ground and box Sprites in the same SpriteList
        # will make it easier to perform collision detection against
        # them later on. Setting the spatial hash to True will make
        # collision detection much faster if the objects in this
        # SpriteList do not move.
        # The box can move, so do not use a spatial hash for this list.
        self.wall_list = arcade.SpriteList()

        # Create one large ground sprite using the cropped image.
        ground = arcade.Sprite("sh_objects/sh_objects2.png", scale=1)
        ground.width = WINDOW_WIDTH
        ground.height = 198
        ground.center_x = WINDOW_WIDTH / 2
        # Keep the top of the ground at its original y-position (64).
        ground.center_y = 64 - ground.height / 2
        self.wall_list.append(ground)

        # Create floating platforms.
        # Each entry is: (x position, y position)
        floating_platforms = [
            (480, 285),
            (800, 390),
            (1056, 500),
        ]

        for x, y in floating_platforms:
            platform = arcade.Sprite("sh_objects/sh_objects2.png", scale=1)
            platform.center_x = x
            platform.center_y = y
            self.wall_list.append(platform)

        # Create one pushable box.
        self.moving_box = arcade.Sprite(
            "sh_objects/sh_objects1.png",
            scale=1,
        )
        self.moving_box.center_x = 512
        self.moving_box.center_y = 96
        self.wall_list.append(self.moving_box)

        # Create a Platformer Physics Engine.
        # This will handle moving our player as well as collisions between
        # the player sprite and whatever SpriteList we specify for the walls.
        # It is important to supply static platforms to the walls parameter. There is a
        # platforms parameter that is intended for moving platforms.
        # If a platform is supposed to move, and is added to the walls list,
        # it will not be moved.
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite,
            walls=self.wall_list,
            gravity_constant=GRAVITY,
        )

        # Background image
        self.background_sprite = arcade.Sprite("sh_background.png")
        self.background_sprite.center_x = WINDOW_WIDTH / 2
        self.background_sprite.center_y = WINDOW_HEIGHT / 2

        self.background_list = arcade.SpriteList()
        self.background_list.append(self.background_sprite)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass

    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()

        # Draw background first
        self.background_list.draw()

        # Draw our sprites
        self.player_list.draw()
        self.wall_list.draw()

    def on_update(self, delta_time):
        """Movement and Game Logic"""

        # Push the box when the player walks into it from the side.
        player_overlaps_box_vertically = (
            self.player_sprite.bottom < self.moving_box.top
            and self.player_sprite.top > self.moving_box.bottom
        )

        if player_overlaps_box_vertically:
            if (
                self.player_sprite.change_x > 0
                and self.player_sprite.right <= self.moving_box.left + PLAYER_MOVEMENT_SPEED
                and self.player_sprite.right + self.player_sprite.change_x
                >= self.moving_box.left
            ):
                self.moving_box.center_x += self.player_sprite.change_x
            elif (
                self.player_sprite.change_x < 0
                and self.player_sprite.left >= self.moving_box.right - PLAYER_MOVEMENT_SPEED
                and self.player_sprite.left + self.player_sprite.change_x
                <= self.moving_box.right
            ):
                self.moving_box.center_x += self.player_sprite.change_x

        # Move the player using our physics engine
        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True
            self.player_facing = "left"
            self.player_sprite.texture = self.player_texture_left
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True
            self.player_facing = "right"
            self.player_sprite.texture = self.player_texture_right

        if self.left_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called whenever a key is released."""

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False

        if self.left_pressed:
            self.player_facing = "left"
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
            self.player_sprite.texture = self.player_texture_left
        elif self.right_pressed:
            self.player_facing = "right"
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
            self.player_sprite.texture = self.player_texture_right
        else:
            self.player_sprite.change_x = 0
            if self.player_facing == "left":
                self.player_sprite.texture = self.player_texture_idle_left
            else:
                self.player_sprite.texture = self.player_texture_idle_right


def main():
    """Main function"""
    window = GameView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
