import toml
from more_itertools import always_iterable
from jaraco.context import suppress
from jaraco.functools import apply


@apply(always_iterable)
@suppress(Exception)
def read_opts():
    with open('pyproject.toml') as strm:
        defn = toml.load(strm)
    section = defn.get("tool.jaraco.test.pytest.allow", {})
    breakpoint()


def pytest_addoption(parser, pluginmanager):
    for opt in read_opts():
        parser.add_option(opt)
