import os
import random
import game.shared.gamecontants as gameconstants

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


def main():
    # create the cast
    cast = Cast()

    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(gameconstants.FONT_SIZE)
    banner.set_color(gameconstants.WHITE)
    banner.set_position(Point(gameconstants.CELL_SIZE, 0))
    cast.add_actor("banners", banner)

    # create the player
    # The gameconstants MAX_X MAX_Y change the original value an inheritances
    x = int(gameconstants.MAX_X / 2)
    # different position. needs to go to the bottom of the page
    y = int(gameconstants.MAX_Y / 1.1)
    position = Point(x, y)

    player = Actor()
    player.set_text('''Ü''')  # the moving guy
    player.set_font_size(gameconstants.PLAYER_SIZE)
    player.set_color(gameconstants.WHITE)
    # may change this to keep player at the bottom of the screen only
    player.set_position(position)
    cast.add_actor("players", player)

    # create the artifacts - Here is where they are pulling from Data
    messages = "Score: "

    for n in range(gameconstants.DEFAULT_ARTIFACTS):
        text = "*"  # me: changed the symbols to display. CHR() = character function
        # this needs to get the points from a function and display here instead of messages from a file
        message = messages
        # The gameconstants COLS and ROWS change the original value change an inheritances
        x = random.randint(1, gameconstants.COLS - 1)
        y = random.randint(1, gameconstants.ROWS - 1)
        position = Point(x, y)
        position = position.scale(gameconstants.CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        artifact = Artifact()
        artifact.set_text(text)
        # artifact.set_text(text2)
        artifact.set_font_size(gameconstants.GEM_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        artifact.set_message(message)
        cast.add_actor("artifacts", artifact)

    # adding a second artifact. TESTING: it works! just has 2 Found Kitten messages. One for each symbol.

    for n in range(gameconstants.DEFAULT_ARTIFACTS2):
        # text = "*" #me: changed the symbols to display. CHR() = character function
        text2 = "®"  # chr(2588)  # box character?
        # this needs to get the points from a function and display here instead of messages from a file
        message = messages
        # The gameconstants COLS and ROWS change the original value an inheritances
        x = random.randint(1, gameconstants.COLS - 1)
        y = random.randint(1, gameconstants.ROWS - 1)
        position = Point(x, y)
        position = position.scale(gameconstants.CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(129, 156, 161)

        rock = Artifact()
        # artifact.set_text(text)
        rock.set_text(text2)
        rock.set_font_size(gameconstants.ROCK_SIZE)
        rock.set_color(color)
        rock.set_position(position)
        rock.set_message(message)
        cast.add_actor("rocks", rock)

    for n in range(gameconstants.INIT_NUM_GEMS):
        # The gameconstants COLS and ROWS change the original value an inheritances
        x = random.randint(1, gameconstants.COLS - 1)
        y = random.randint(1, gameconstants.ROWS - 1)

        position = Point(x, y)
        position = position.scale(gameconstants.CELL_SIZE)
        ruby = Ruby()
        ruby.set_font_size(gameconstants.ROCK_SIZE)
        ruby.set_position(position)
        cast.add_actor("rubys", ruby)

    # start the game
    keyboard_service = KeyboardService(gameconstants.CELL_SIZE)
    display_service = DisplayService(
        gameconstants.CAPTION.format(gameconstants.CENTER),
        gameconstants.MAX_X,
        gameconstants.MAX_Y,
        gameconstants.CELL_SIZE,
        gameconstants.FRAME_RATE
    )
    director = Director(keyboard_service, display_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()
