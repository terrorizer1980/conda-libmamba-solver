# Changelog

All notable changes to this project will be documented in this file.

> The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
> and this project adheres to [calendar versioning](https://calver.org/) in the `YY.M.MICRO`format.

## [Unreleased]

<!--
Populate these categories as PRs are merged to `main`. When a release is cut,
copy to its corresponding section, deleting empty sections if any.
--->

### Added

### Changed

### Deprecated

### Removed

### Fixed

### Security


## [22.3.1] - 2022-03-23

### Fixed

* Make sure `noarch` packages get reinstalled if Python version changed (#26)
* Accept star-only version specs (e.g. `libblas=*=*mkl`) and fix support for `channel::package` syntax (#25)
* Enable support for authenticated channels (#23)

## [22.3.0] - 2022-03-09

_First public release_

## [22.2.0] - 2022-02-01

_Internal pre-release as a separate repository._

<!-- Hyperlinks --->

[Unreleased]: https://github.com/conda-incubator/conda-libmamba-solver/compare/22.3.1..main
[22.3.1]: https://github.com/conda-incubator/conda-libmamba-solver/releases/tag/22.3.1
[22.3.0]: https://github.com/conda-incubator/conda-libmamba-solver/releases/tag/22.3.0
[22.2.0]: https://github.com/conda-incubator/conda-libmamba-solver/releases/tag/22.2.0