import numpy as np

def acoustic_impedance(rho, vp):
  """
  Calculate acoustic impedance of a rock.
  """
  return rho * vp

def density(mass, volume):
    """
    Calculate density.
    """
    return mass / volume * 2

def friction():
    """
    Determine rock friction.
    testing
    """
    return 0.6
