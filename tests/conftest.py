import pytest


@pytest.fixture()
def set_up():
    print('Start Main functionality test')
    yield
    print('Сompletion Main functionality test')

@pytest.fixture(scope='module')
def set_group():
    print('Start of testing functionality')
    yield
    print('Сompletion of testing functionality')
