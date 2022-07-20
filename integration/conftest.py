MARKER = """\
unit: Mark unit tests
integration: Mark Integration tests
high: Hight Priority
medium: Medium Priority
low: Low Priority
"""

def pytest_configure(config):
    map(lambda line: config.addinivalue_line('markers', line), MARKER.split("\n"))