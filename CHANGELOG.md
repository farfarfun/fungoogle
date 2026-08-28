# Changelog

## [Unreleased]

### Changed

- **Breaking**: renamed the import name and PyPI package name from `notegoogle` to `fungoogle` to match the repository name. Anyone doing `import notegoogle` or `pip install notegoogle` must switch to `import fungoogle` / `pip install fungoogle`.
- The old `notegoogle` PyPI package will get one final release forwarding to `fungoogle` (manual follow-up by the repo owner). Note: an unrelated empty placeholder package already exists on PyPI under the name `fungoogle` (0.0.1) and will need to be dealt with separately before this project can actually publish under that name.
