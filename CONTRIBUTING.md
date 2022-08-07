# Contributing to Dundie Project

Summary of project

## Guidelines

- Backwards compatibility
- Multiplataform
- Python 3 only

## Code of conduct

- Be gentle

## How to Contribute

### Fork repository
- Click fork button on [github_repo](https://github.com/...)
  
### Clone to local dev environment

```bash
git clone https://github.com/seunome/...
...
```

### Prepare virtual env

```bash
cd dundie-rewards
make virtualenv
make install
```

### Coding style

- This project follows PEP8

### Run tests

```bash
make test
#or
make watch
```

### Commit rules

- We follow conventional commit messages ex: '[bugfix] reason #issue'
- We require signed commits

### Pull Request rules

- We require all tests be passing