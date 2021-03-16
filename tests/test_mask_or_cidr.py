import pytest

from mask_or_cidr import __version__
from mask_or_cidr.mask_calculator import invert_mask


def test_version():
    assert __version__ == '0.1.0'


cidr_mask = [
    ('0', '0.0.0.0'),
    ('1', '128.0.0.0'),
    ('2', '192.0.0.0'),
    ('9', '255.128.0.0'),
    ('18', '255.255.192.0'),
    ('25', '255.255.255.128')]


@pytest.mark.parametrize("cidr, mask", cidr_mask)
def test_valid_cidr(cidr, mask):
    assert invert_mask(cidr) == mask


@pytest.mark.parametrize("cidr, mask", cidr_mask)
def test_valid_mask_to_cird(cidr, mask):
    assert invert_mask(mask) == cidr


@pytest.mark.parametrize("mask", [
    '-1',
    'fpp',
    '33',
    '257.0.0.',
    '244.0.43.0'])
def test_invalid_mask(mask):
    assert invert_mask(mask) == 'invalid'
