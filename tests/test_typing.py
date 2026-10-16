import numpy as np

from ibex_non_ca_helpers.typing import PVBaseValue, PVValue


def test_pv_base_value():
    # Note: test doesn't check anything at runtime, but will fail pyright check if invalid
    _: PVBaseValue = 1
    _: PVBaseValue = 1.23
    _: PVBaseValue = True
    _: PVBaseValue = "foo"


def test_pv_value():
    # Note: test doesn't check anything at runtime, but will fail pyright check if invalid
    _: PVValue = [1, 2, 3]
    _: PVValue = [1.23, 4.56]
    _: PVValue = [True, False]
    _: PVValue = ["foo", "bar"]
    _: PVValue = ["foo", 1, 1.23, True]
    _: PVValue = np.zeros([1, 2, 3])
