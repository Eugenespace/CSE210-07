import os
import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast
from game.casting.ruby import Ruby
from game.casting.rock import Rock

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.display_service import DisplayService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 20
PLAYER_SIZE = 25
GEM_SIZE = 25
ROCK_SIZE = 27
CENTER = "center"
COLS = 60
ROWS = 40
CAPTION = "Greed"

WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 20
DEFAULT_ARTIFACTS2 = 20
INIT_NUM_ROCKS = 20
INIT_NUM_GEMS = 5


def main():

    # create the cast
    cast = Cast()

    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)

    # create the player
    x = int(MAX_X / 2)
    # different position. needs to go to the bottom of the page
    y = int(MAX_Y / 1.1)
    position = Point(x, y)

    player = Actor()
    player.set_text('''Ü''')  # the moving guy
    player.set_font_size(PLAYER_SIZE)
    player.set_color(WHITE)
    # may change this to keep player at the bottom of the screen only
    player.set_position(position)
    cast.add_actor("players", player)

    # create the artifacts - Here is where they are pulling from Data
    messages = "Score: "

    for n in range(DEFAULT_ARTIFACTS):
        text = "*"  # me: changed the symbols to display. CHR() = character function
        # this needs to get the points from a function and display here instead of messages from a file
        message = messages

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        artifact = Artifact()
        artifact.set_text(text)
        # artifact.set_text(text2)
        artifact.set_font_size(GEM_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        artifact.set_message(message)
        cast.add_actor("artifacts", artifact)
        
        

    # adding a second artifact. TESTING: it works! just has 2 Found Kitten messages. One for each symbol.

    for n in range(DEFAULT_ARTIFACTS2):
        # text = "*" #me: changed the symbols to display. CHR() = character function
        text2 = "®" #chr(2588)  # box character?
        # this needs to get the points from a function and display here instead of messages from a file
        message = messages

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(129, 156, 161)

        rock = Artifact()
        # artifact.set_text(text)
        rock.set_text(text2)
        rock.set_font_size(ROCK_SIZE)
        rock.set_color(color)
        rock.set_position(position)
        rock.set_message(message)
        cast.add_actor("rocks", rock)

    for n in range(INIT_NUM_GEMS):

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        
        position = Point(x, y)
        position = position.scale(CELL_SIZE)
        ruby = Ruby()
        ruby.set_font_size(ROCK_SIZE)
        ruby.set_position(position)
        cast.add_actor("rubys", ruby)


    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    display_service = DisplayService(CAPTION.format(
        CENTER), MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, display_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()
