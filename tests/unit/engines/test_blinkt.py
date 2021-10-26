
import pytest
import saltext.blinkt.engines.blinkt_mod as blinkt_engine


@pytest.fixture
def configure_loader_modules():
    module_globals = {
        "__salt__": {"this_does_not_exist.please_replace_it": lambda: True},
    }
    return {
        blinkt_engine: module_globals,
    }


def test_replace_this_this_with_something_meaningful():
    assert "this_does_not_exist.please_replace_it" in blinkt_engine.__salt__
    assert blinkt_engine.__salt__["this_does_not_exist.please_replace_it"]() is True
