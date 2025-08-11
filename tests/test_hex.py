import pytest
from ibex_non_ca_helpers.hex import compress_and_hex, dehex_and_decompress, dehex_and_decompress_waveform


def test_can_dehex_and_decompress():
    expected = b"test123"
    hexed_and_compressed = b"789c2b492d2e31343206000aca0257"
    result = dehex_and_decompress(hexed_and_compressed)
    assert result == expected


def test_can_hex_and_compress():
    to_compress_and_hex = "test123"
    expected = b"789c2b492d2e31343206000aca0257"
    result = compress_and_hex(to_compress_and_hex)
    assert result == expected

def test_non_bytes_given_to_dehex_and_decompress_raises_assertionerror():
    with pytest.raises(AssertionError):
        dehex_and_decompress("test")

def test_non_string_given_to_compress_and_hex_raises_assertionerror():
    with pytest.raises(AssertionError):
        compress_and_hex(b"test")

def test_non_list_given_to_dehex_and_decompress_waveform_raises_assertionerror():
    with pytest.raises(AssertionError):
        dehex_and_decompress_waveform("test")

def test_dehex_and_decompress_waveform_with_ok_waveform_returns_expected():
    pass