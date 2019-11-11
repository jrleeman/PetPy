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
    return mass / volume
