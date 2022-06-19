import pytest
from block import BlockFunctions
from main_window import Functions
from bluetooth import Bluetooth_Functions
from appium import webdriver


@pytest.fixture(scope="session")
def browser():
    cap = {
        "automationName": "XCUITest",
        'platformName': 'ios',
        'platformVersion': '15.5',
        'deviceName': 'iPhone 13',
        'app': 'Mimesis.Settings'}

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=cap)
    yield driver


def test_open_app(browser):
    functions = Functions(browser)
    assert functions.main_window() is True


def test_airplane_mode(browser):
    functions = Functions(browser)
    functions.airplane_mode()
    assert functions.airplane_mode_check() is '1'


def test_mobile_data(browser):
    functions = Functions(browser)
    functions.mobile_data()
    assert functions.mobile_data_check() is None


def test_wi_fi(browser):
    functions = Functions(browser)
    functions.wi_fi()
    assert functions.wi_fi_check() is None


def test_bluetooth(browser):
    functions = Functions(browser)
    functions.bluetooth()
    assert functions.bluetooth_check() is None


def test_enlarge_block(browser):
    functions = Functions(browser)
    functions.block()
    size = {'height': 480, 'width': 320}
    assert functions.block_check() == size


def test_decrease_block(browser):
    functions = Functions(browser)
    functions.block()
    functions.miniblock()
    size = {'height': 160, 'width': 160}
    assert functions.block_check() == size


def test_bluetooth_devices(browser):
    bfunctions = Bluetooth_Functions(browser)
    bfunctions.bluetooth_devices()
    check = bfunctions.bluetooth_devices_check()
    assert check in 'Bluetooth'


def test_bluetooth_settings(browser):
    bfunctions = Bluetooth_Functions(browser)
    bfunctions.bluetooth_devices()
    bfunctions.bluetooth_settings()
    assert bfunctions.bluetooth_settings_check


def test_airdrop(browser):
    blockfunctions = BlockFunctions(browser)
    functions = Functions(browser)
    functions.block()
    blockfunctions.airdrop()
    assert blockfunctions.airdrop_check() is '1'


def test_hotspot(browser):
    blockfunctions = BlockFunctions(browser)
    functions = Functions(browser)
    functions.block()
    blockfunctions.hotspot()
    assert blockfunctions.hotspot_check() is '1'


def test_minimize_app(browser):
    functions = Functions(browser)
    functions.minimize_app()
    assert functions.window_check() is None


def test_reopen_app(browser):
    functions = Functions(browser)
    functions.reopen_app()
    assert functions.main_window() is True
