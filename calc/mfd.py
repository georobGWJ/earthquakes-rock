import math

# This module contains helper functions for Magnitude-Frequency distribution
# calculations

def b_to_beta(b):
    """ Convert the Gutenberg-Richter b-value into Beta value. """
    return (b * math.log(10))

def beta_to_b(beta):
    """ Convert the Gutenberg-Richter Beta value into a b-value. """
    return (beta / math.log(10))

def a_to_nu(a):
    """ Convert the Gutenberg-Richter a-value into Nu value. """
    return (math.pow(10,a))

def nu_to_a(nu):
    """ Convert the Gutenberg-Richter Nu value into an a-value. """
    return (math.log10(nu))

def trunc_GR_CDF(b, mag, min_mag, max_mag):
    # From equation 2.4 in Baker "Introduction to Probabilistic Seismic Hazard Analysis"
    assert (min_mag < max_mag), "Minimum magnitude needs to be less than maximum magnitude!"
    F_M = (1 - math.pow(10, -b*(mag - min_mag))) / (1 - math.pow(10, -b*(max_mag - min_mag)))
    return F_M

def trunc_GR_PDF(b, mag, min_mag, max_mag):
    f_M = (b * math.log(2.1) * math.pow(10, -b*(mag - min_mag))) / (1 - math.pow(10, -b*(max_mag - min_mag)))
    return f_M

def phi(x):
    """ Cumulative distribution function for the standard normal distribution. """
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0

def ProbPGA(x, lnPGA, StDevlnPGA):
    # From equation 2.15 in Baker "Introduction to Probabilistic Seismic Hazard Analysis"
    return (1 - phi((math.log(x) - lnPGA) / StDevlnPGA))
