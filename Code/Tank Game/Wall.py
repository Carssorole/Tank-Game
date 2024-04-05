"""
This is the Wall class.
Tutorials and sources used for this class:
Initial wall creation: https://www.youtube.com/watch?v=cWtyxv4i-fQ
Implementing walls into game: https://www.youtube.com/watch?v=1ruj8v3_ydM
Making walls solid: https://www.youtube.com/watch?v=XWsnIup4XlY&list=PLM-syYolLbsz5paY9gafMzMpWgv-h4ac6&index=8
"""
import pytmx
from pytmx import load_pygame

SCOREBOARD_HEIGHT = 66


def wall_tiles(window, tmxdata, height, scoreboard_height):
    start_y = scoreboard_height
    for layer in tmxdata.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid, in layer:
                tile = tmxdata.get_tile_image_by_gid(gid)
                if tile:
                    window.blit(tile, (x * tmxdata.tilewidth, start_y + y * tmxdata.tileheight))


def get_tile_properties(tmxdata, x, y):
    tile_x = x // tmxdata.tilewidth
    tile_y = y // tmxdata.tileheight
    properties = tmxdata.get_tile_properties_by_gid(tmxdata.get_tile_gid(tile_x, tile_y, 0))
    return properties or {}


def can_move_to(tmxdata, rect, x, y, scoreboard_height):
    points = [
        (rect.left + x, rect.top + y - scoreboard_height),
        (rect.right + x - 1, rect.top + y - scoreboard_height),
        (rect.left + x, rect.bottom + y - 1 - scoreboard_height),
        (rect.right + x - 1, rect.bottom + y - 1 - scoreboard_height)
    ]
    for point in points:
        tile_x = point[0] // tmxdata.tilewidth
        tile_y = point[1] // tmxdata.tileheight
        try:
            properties = tmxdata.get_tile_properties(tile_x, tile_y, 0)
        except ValueError:
            properties = {}
        if properties and properties.get("solid"):
            return False
    return True
