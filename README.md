# Wagtail Font Awesome SVG

Add [Font Awesome v6](https://fontawesome.com/v6/icons?m=free&d=gallery) SVG icons to your Wagtail project. Only the `solid`, `regular` and `brands` icons are included.

## Install

```sh
pip install wagtail-font-awesome-svg
```

Add `wagtailfontawesomesvg` to your installed apps.

```python
INSTALLED_APPS = [
    'wagtailfontawesomesvg',
]
```

## Usage

This is an [overview of available icons](https://fontawesome.com/v6/icons?m=free&d=gallery). 
Choose an icon and add it via your `wagtail_hooks.py`:

```python
from wagtail import hooks

@hooks.register("register_icons")
def register_icons(icons):
    return icons + [
        'wagtailfontawesomesvg/brands/facebook.svg',
        'wagtailfontawesomesvg/regular/face-laugh.svg',
        'wagtailfontawesomesvg/solid/yin-yang.svg',
        ...
    ]
```
