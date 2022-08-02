import pytest

MARKER = """\
unit: Mark unit tests
integration: Mark Integration tests
high: Hight Priority
medium: Medium Priority
low: Low Priority
win: Run on Windows
"""
def pytest_configure(config):
    for line in MARKER.split("\n"):
        config.addinivalue_line('markers', line)

@pytest.fixture(autouse=True)
def go_to_tmpdir(request): #injecao de dependencias
    tmpdir = request.getfixturevalue("tmpdir")
    with tmpdir.as_cwd():
        yield # protocolo de generators