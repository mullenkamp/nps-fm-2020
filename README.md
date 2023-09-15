# nps-fm-2020

<p align="center">
    <em>Python package to estimate the grades for the nps-fm-2020</em>
</p>

[![build](https://github.com/nps-fm-2020/workflows/Build/badge.svg)](https://github.com/nps-fm-2020/actions)
[![codecov](https://codecov.io/gh/nps-fm-2020/branch/master/graph/badge.svg)](https://codecov.io/gh/nps-fm-2020)
[![PyPI version](https://badge.fury.io/py/npsfm.svg)](https://badge.fury.io/py/npsfm)

---

**Documentation**: <a href="https://mullenkamp.github.io/nps-fm-2020/" target="_blank">https://mullenkamp.github.io/nps-fm-2020/</a>

**Source Code**: <a href="https://github.com/nps-fm-2020" target="_blank">https://github.com/nps-fm-2020</a>

---

## Development

### Setup environment

We use [Hatch](https://hatch.pypa.io/latest/install/) to manage the development environment and production build. Ensure it's installed on your system.

### Run unit tests

You can run all the tests with:

```bash
hatch run test
```

### Format the code

Execute the following command to apply linting and check typing:

```bash
hatch run lint
```

### Publish a new version

You can bump the version, create a commit and associated tag with one command:

```bash
hatch version patch
```

```bash
hatch version minor
```

```bash
hatch version major
```

Your default Git text editor will open so you can add information about the release.

When you push the tag on GitHub, the workflow will automatically publish it on PyPi and a GitHub release will be created as draft.

## Serve the documentation

You can serve the Mkdocs documentation with:

```bash
hatch run docs-serve
```

It'll automatically watch for changes in your code.

## License

This project is licensed under the terms of the Apache Software License 2.0.
