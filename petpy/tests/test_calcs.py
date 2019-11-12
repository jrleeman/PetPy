"""Tests calculations for the calc submodule."""

import numpy as np
from numpy.testing import assert_array_equal, assert_array_almost_equal
from unittest.mock import patch
from datetime import datetime
import pytest

from petpy.calcs import (acoustic_impedance, read_sensor_calibrated, classifier)
import petpy.calcs


def test_acoustic_impedance_valid_scalars():
    """Tests with valid scalar numbers."""
    # Setup
    vp = 2200
    rho = 2400
    truth = 5280000

    # Exercise
    result = acoustic_impedance(rho, vp)

    # Verify
    assert truth == result




def test_acoustic_impedance_valid_arrays():
    """Test with arrays of valid numbers."""
    # Setup
    vp = np.array([2200, 2100, 2000])
    rho = np.array([2400, 2300, 2200])
    truth = np.array([5280000, 4830000, 4400000])

    # Exercise
    result = acoustic_impedance(rho, vp)

    # Verify
    assert_array_almost_equal(truth, result, 2)


def mocked_read_sensor():
    """Mock the sensor by always returning unity."""
    return 1


@patch('petpy.calcs.read_sensor', new=mocked_read_sensor)
def test_read_sensor_calibrated():
    """Test the the calibration works with a unity sensor input."""
    # Setup
    truth = 2.2

    # Exercise
    result = read_sensor_calibrated()

    # Verify
    assert_array_almost_equal(truth, result)


def mocked_get_current_utc_time():
    """Mock the time function for testing."""
    return datetime(2019, 3, 26, 12)


@patch('petpy.calcs.get_current_utc_time', new=mocked_get_current_utc_time)
def test_current_utc_time():
    """Test if our time return works."""
    # Setup
    truth = datetime(2019, 3, 26, 12)

    # Exercise
    result = petpy.calcs.get_current_utc_time()

    # Verify
    assert truth == result


@pytest.mark.parametrize('density, expected, will_fail', [
    (2750, 'granite', False),
    (2500, 'sandstone', False),
    (1000, 'not a rock', False),
    (2800, 'granite', False),
    (-5, None, True)
])
def test_classifier(density, expected, will_fail):
    """Verify that we correctly identify rocks."""
    # Setup

    if will_fail:
        with pytest.raises(ValueError):
            classifier(density)

    else:
        result = classifier(density)
        assert result == expected
