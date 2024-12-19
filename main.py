def on_a_pressed():
    if Retning == 0:
        mySprite.set_image(assets.image("""
            myImage6
        """))
        pause(100)
        mySprite.set_image(assets.image("""
            myImage2
        """))
    else:
        mySprite.set_image(assets.image("""
            myImage5
        """))
        pause(100)
        mySprite.set_image(img("""
            .....ffffff.....
                        ....f4edeeef....
                        ....fdddeeeef...
                        ...fedddffffff..
                        ..ffffffeeeeedf.
                        .feddddddddddff.
                        .f4444444fffff..
                        .ffffffffeedef..
                        ...ff28f22ddef..
                        ...f111114def...
                        ...f444444ef....
                        ...f9111199ff...
                        ..fde98999eeef..
                        .fdde7777dddeef.
                        .fdfe9797deee11f
                        f11fe9797def141f
                        f14fe9797defff1f
                        f1ffebbbfeef..f.
                        .f.f1111118f....
                        ...f111f888f....
                        ...feef.feef....
                        ....ff...ff.....
        """))
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    global Retning
    mySprite.set_image(img("""
        .....ffffff.....
                ....f4edeeef....
                ....fdddeeeef...
                ...fedddffffff..
                ..ffffffeeeeedf.
                .feddddddddddff.
                .f4444444fffff..
                .ffffffffeedef..
                ...ff28f22ddef..
                ...f111114def...
                ...f444444ef....
                ...f9111199ff...
                ..fde98999eeef..
                .fdde7777dddeef.
                .fdfe9797deee11f
                f11fe9797def141f
                f14fe9797defff1f
                f1ffebbbfeef..f.
                .f.f1111118f....
                ...f111f888f....
                ...feef.feef....
                ....ff...ff.....
    """))
    Retning = 1
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    global Retning
    mySprite.set_image(assets.image("""
        myImage2
    """))
    Retning = 0
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

Retning = 0
mySprite: Sprite = None
mySprite = sprites.create(assets.image("""
    myImage2
"""), SpriteKind.player)
Retning = 0
scene.camera_follow_sprite(mySprite)
controller.move_sprite(mySprite)
tiles.set_current_tilemap(tilemap("""
    level2
"""))
tiles.place_on_tile(mySprite, tiles.get_tile_location(8, 8))