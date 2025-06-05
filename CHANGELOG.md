# Wagtail Font Awesome SVG Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
