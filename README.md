# Wagtail Font Awesome SVG

Add [Font Awesome 5.14](https://fontawesome.com/icons?d=gallery&m=free) SVG icons to your Wagtail project.

Note: Wagtail does not officially support SVG icons yet, but is working towards it.
See Wagtail issue [#6107](https://github.com/wagtail/wagtail/issues/6107) for progress.

## Install

    pip install wagtail-font-awesome-svg

Add `wagtailfontawesomesvg` to your installed apps.

    INSTALLED_APPS = [
        'wagtailfontawesomesvg',
    ]

## Usage

This is an [overview of available icons](https://fontawesome.com/icons?d=gallery&m=free). 
Choose an icon and add it via your `wagtail_hooks.py`:

    from wagtail import hooks

    @hooks.register("register_icons")
    def register_icons(icons):
        return icons + [
            'wagtailfontawesomesvg/brands/facebook.svg',
            'wagtailfontawesomesvg/regular/laugh.svg',
            'wagtailfontawesomesvg/solid/yin-yang.svg',
            ...
        ]
