# Wagtail Font Awesome SVG

Add [Font Awesome](https://fontawesome.com/icons?d=gallery&m=free) SVG icons to your Wagtail project.

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

This is an [overview of available icons](https://fontawesome.com/icons?d=gallery&m=free). 
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
