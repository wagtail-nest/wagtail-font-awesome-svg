# Wagtail Font Awesome SVG Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- Drop support for Python 3.8 and 3.9 (both end-of-life).
- Add support for Python 3.14.
- Add support for Django 6.0.
- Drop Wagtail 5 and Wagtail 6 classifiers (both end-of-life). Supported Wagtail range is now 7.0 LTS through 7.4 LTS.
- Pin minimum Wagtail to 7.0.

## [2.0] - 2025-08-23

- Update icons for Font Awesome 7.0.0 by @Stormheg in #19

## [1.2.1] - 2025-08-23

- Update changelog

## [1.2] - 2025-08-23

- Adjust the classifiers to indicate support for Django 5.1, 5.2 and Wagtail 6 and 7.
- Move to pyproject.toml, adopt PEP-639-style license specification by @Stormheg in #17
- Update icons for Font Awesome 6.7.2 by @Stormheg in #18

## [1.1] - 2025-06-05

- Adjustments to support Wagtail 6.x and drop Django < 4.2
- Scrape icons from fontawesome-free-6.5.2-web

## [1.0.1] - 2022-10-04

- Update readme and examples.

## [1.0] - 2022-10-04

- FontAwesome 6 support.
- Breaking changes, 457 icons being either removed or renamed (for example, volume-down became volume-low).
- There are 827 completely new or new names.
- Ref: https://fontawesome.com/docs/web/setup/upgrade/whats-changed#icons-renamed-in-version-6.

## [0.0.4] - 2022-10-04

- Update icons for Wagtail 5.0 icons preview compatibility. Fixes #10 and #12.
  - The xmlns attribute is added for icons defined in this package.
  - Switched to `<svg>` tags rather than `<symbol>`.
  - Supports the Wagtail icons preview built into the CMS.
  - Adds licence information to the icons.
- Adjustments to support Wagtail 4.1 and drop Django < 3.2
 
## [0.0.3] 2022-10-28

- Initial release.


[unreleased]: https://github.com/wagtail-nest/wagtail-font-awesome-svg/compare/1.0.1...HEAD
[1.0.1]: https://github.com/wagtail-nest/wagtail-font-awesome-svg/compare/1.0...1.0.1
[1.0]: https://github.com/wagtail-nest/wagtail-font-awesome-svg/compare/0.0.4...1.0
[0.0.4]: https://github.com/wagtail-nest/wagtail-font-awesome-svg/compare/0.0.3...0.0.4
[0.0.3]: https://github.com/wagtail-nest/wagtail-font-awesome-svg/tree/0.0.3
