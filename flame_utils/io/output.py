#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Output from FLAME.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np

from flame_utils.core import BeamState


def convert_results(res, **kws):
    """Convert all beam states of results generated by :func:`run()` method
    to be ``BeamState`` object.

    Parameters
    ----------
    res : list of tuple
        List of propagation results.

    Returns
    -------
    list of tuple
        Tuple of ``(r, s)``, where ``r`` is list of results at each monitor
        points, ``s`` is ``BeamState`` object after the last monitor point.
    """
    return [(i, BeamState(s)) for (i, s) in res]


def collect_data(result, **kws):
    """Collect data of interest from propagation results.

    Parameters
    ----------
    result :
        Propagation results with ``BeamState`` object.

    Keyword Arguments
    -----------------
    pos : float
        Longitudinally propagating position, [m].
    ref_beta : float
        Speed in the unit of light velocity in vacuum of reference charge
        state, Lorentz beta.
    ref_bg : float
        Multiplication of beta and gamma of reference charge state.
    ref_gamma : float
        Relativistic energy of reference charge state, Lorentz gamma.
    ref_IonEk : float
        Kinetic energy of reference charge state, [eV/u].
    ref_IonEs : float
        Rest energy of reference charge state, [eV/u].
    ref_IonQ : int
        Macro particle number of reference charge state.
    ref_IonW : float
        Total energy of reference charge state, [eV/u],
        i.e. :math:`W = E_s + E_k`.
    ref_IonZ : float
        Reference charge state, measured by charge to mass ratio, e.g.
        :math:`^{33^{+}}_{238}U: Q[33]/A[238]`.
    ref_phis : float
        Absolute synchrotron phase of reference charge state, [rad].
    ref_SampleIonK : float
        Wave-vector in cavities with different beta values of reference charge
        state.
    beta : Array
        Speed in the unit of light velocity in vacuum of all charge states,
        Lorentz beta.
    bg : Array
        Multiplication of beta and gamma of all charge states.
    gamma : Array
        Relativistic energy of all charge states, Lorentz gamma.
    IonEk : Array
        Kinetic energy of all charge states, [eV/u].
    IonEs : Array
        Rest energy of all charge states, [eV/u].
    IonQ : Array
        Macro particle number of all charge states.
    IonW : Array
        Total energy of all charge states, [eV/u], i.e. :math:`W = E_s + E_k`.
    IonZ : Array
        All charge states, measured by charge to mass ratio
    phis : Array
        Absolute synchrotron phase of all charge states, [rad]
    SampleIonK : Array
        Wave-vector in cavities with different beta values of all charge
        states.
    x0, xcen_all : Array
        X centroid for all charge states, [mm].
    y0, ycen_all : Array
        Y centroid for all charge states, [mm].
    xp0, xpcen_all : Array
        X centroid divergence for all charge states, [rad].
    yp0, ypcen_all : Array
        Y centroid divergence for all charge states, [rad].
    phi0, phicen_all : Array
        Longitudinal beam length, measured in RF frequency for all charge
        states, [rad].
    dEk0, dEkcen_all : Array
        Kinetic energy deviation w.r.t. reference charge state, for all charge
        states, [MeV/u].
    x0_rms, xrms : float
        General rms beam envelope for x, [mm].
    y0_rms, yrms : float
        General rms beam envelope for y, [mm].
    xp0_rms, xprms : float
        General rms beam envelope for x', [rad].
    yp0_rms, yprms : float
        General rms beam envelope for y', [rad].
    phi0_rms, phirms : float
        General rms beam envelope for :math:`\phi`, [rad].
    dEk0_rms, dEkrms : float
        General rms beam envelope for :math:`\delta E_k`, [MeV/u].
    xrms_all : Array
        General rms beam envelope for x of all charge states, [mm].
    yrms_all : Array
        General rms beam envelope for y of all charge states, [mm].
    xprms_all : Array
        General rms beam envelope for x' of all charge states, [rad].
    yprms_all : Array
        General rms beam envelope for y' of all charge states, [rad].
    phirms_all : Array
        General rms beam envelope for :math:`\phi` of all charge states, [rad].
    dEkrms_all : Array
        General rms beam envelope for :math:`\delta E_k` of all charge states, [MeV/u].
    x0_env, xcen : Array
        Weight average of all charge states for x', [rad].
    y0_env, ycen : Array
        Weight average of all charge states for y, [mm].
    xp0_env, xpcen : Array
        Weight average of all charge states for x', [rad].
    yp0_env, ypcen : Array
        Weight average of all charge states for y', [rad].
    phi0_env, phicen : Array
        Weight average of all charge states for :math:`\phi`, [mm].
    dEk0_env, dEkcen : Array
        Weight average of all charge states for :math:`\delta E_k`, [MeV/u].
    moment0_env, cenvector : Array
        Weight average of centroid for all charge states, array of
        ``[x, x', y, y', phi, dEk, 1]``, with the units of
        ``[mm, rad, mm, rad, rad, MeV/u, 1]``.
    moment0, cenvector_all : Array
        Centroid for all charge states, array of ``[x, x', y, y', phi, dEk, 1]``.
    moment0_rms, rmsvector : Array
        RMS beam envelope, part of statistical results from ``moment1``.
    moment1, beammatrix_all : Array
        Correlation tensor of all charge states, for each charge state.
    moment1_env, beammatrix : Array
        Correlation tensor of all charge states, average over all charge states.

    Returns
    -------
    dict
        Dict of ``{k1:v1, k2,v2...}``, keys are from keyword parameters.

    Note
    ----
    Set the data of interest with ``k=True`` as input will return the defined
    ``k`` value.

    Examples
    --------
    >>> # get x0 and y0 array
    >>> collect_data(r, x0=True, y0=True)

    See Also
    --------
    BeamState : FLAME beam state class for ``MomentMatrix`` simulation type.
    """
    valid_keys = [k for k, v in kws.items() if v is not None]
    try:
        return {ik: np.array([getattr(s, ik) for (i, s) in result]) for ik in valid_keys}
    except:
        result = convert_results(result)
        return {ik: np.array([getattr(s, ik) for (i, s) in result]) for ik in valid_keys}
