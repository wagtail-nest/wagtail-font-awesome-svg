from wagtail import hooks


@hooks.register("register_icons")
def register_icons(icons):
    return icons + [
        "wagtailfontawesomesvg/brands/facebook.svg",
        "wagtailfontawesomesvg/regular/laugh.svg",
        "wagtailfontawesomesvg/solid/yin-yang.svg",
    ]
