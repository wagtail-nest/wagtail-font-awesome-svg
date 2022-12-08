# Wagtail Font Awesome SVG

Add [Font Awesome 5.14](https://fontawesome.com/icons?d=gallery&m=free) SVG icons to your Wagtail project.

Note: Wagtail does not officially support SVG icons yet, but is working towards it.
See Wagtail issue [#6107](https://github.com/wagtail/wagtail/issues/6107) for progress.

[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![PyPI version](https://badge.fury.io/py/wagtail-font-awesome-svg.svg)](https://badge.fury.io/py/wagtail-font-awesome-svg)
[![Font Awesome SVG CI](https://github.com/allcaps/wagtail-font-awesome-svg/actions/workflows/test.yml/badge.svg)](https://github.com/allcaps/wagtail-font-awesome-svg/actions/workflows/test.yml)

## Links

- [Documentation](https://github.com/allcaps/wagtail-font-awesome-svg/blob/main/README.md)
- [Changelog](https://github.com/allcaps/wagtail-font-awesome-svg/blob/main/CHANGELOG.md)
- [Contributing](https://github.com/allcaps/wagtail-font-awesome-svg/blob/main/CHANGELOG.md)
- [Discussions](https://github.com/allcaps/wagtail-font-awesome-svg/discussions)
- [Security](https://github.com/allcaps/wagtail-font-awesome-svg/security)

## Supported versions

- Python ...
- Django ...
- Wagtail ...

## Installation

    pip install wagtail-font-awesome-svg

Add `wagtailfontawesomesvg` to your installed apps.

    INSTALLED_APPS = [
        'wagtailfontawesomesvg',
    ]

## Usage

This is an [overview of available icons](https://fontawesome.com/icons?d=gallery&m=free). 
Choose an icon and add it via your `wagtail_hooks.py`:

    from wagtail.core import hooks

    @hooks.register("register_icons")
    def register_icons(icons):
        return icons + [
            'wagtailfontawesomesvg/brands/facebook.svg',
            'wagtailfontawesomesvg/regular/laugh.svg',
            'wagtailfontawesomesvg/solid/yin-yang.svg',
            ...
        ]
