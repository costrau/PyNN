"""
Definition of default parameters (and hence, standard parameter names) for
standard cell models.

Plain integrate-and-fire models:
    IF_curr_exp
    IF_curr_alpha
    IF_cond_exp
    IF_cond_alpha
    
Integrate-and-fire with adaptation:
    IF_cond_exp_gsfa_grr
    EIF_cond_alpha_isfa_ista
    EIF_cond_exp_isfa_ista    
    
Integrate-and-fire model for use with the FACETS hardware
    IF_facets_hardware1
    
Hodgkin-Huxley model
    HH_cond_exp

Spike sources (input neurons) 
    SpikeSourcePoisson
    SpikeSourceArray
    SpikeSourceInhGamma
               
"""
from __future__ import absolute_import

import numpy
from .common import StandardCellType

class IF_curr_alpha(StandardCellType):
    """
    Leaky integrate and fire model with fixed threshold and alpha-function-
    shaped post-synaptic current.
    """
    
    default_parameters = {
        'v_rest'     : -65.0,   # Resting membrane potential in mV. 
        'cm'         :   1.0,   # Capacity of the membrane in nF
        'tau_m'      :  20.0,   # Membrane time constant in ms.
        'tau_refrac' :   0.0,   # Duration of refractory period in ms. 
        'tau_syn_E'  :   0.5,   # Rise time of the excitatory synaptic alpha function in ms.
        'tau_syn_I'  :   0.5,   # Rise time of the inhibitory synaptic alpha function in ms.
        'i_offset'   :   0.0,   # Offset current in nA
        'v_reset'    : -65.0,   # Reset potential after a spike in mV.
        'v_thresh'   : -50.0,   # Spike threshold in mV.
        'v_init'     : -65.0,   # Membrane potential in mV at t = 0
    }
    recordable = ['spikes', 'v']
    conductance_based = False

class IF_curr_exp(StandardCellType):
    """
    Leaky integrate and fire model with fixed threshold and
    decaying-exponential post-synaptic current. (Separate synaptic currents for
    excitatory and inhibitory synapses.
    """
    
    default_parameters = {
        'v_rest'     : -65.0,   # Resting membrane potential in mV. 
        'cm'         : 1.0,     # Capacity of the membrane in nF
        'tau_m'      : 20.0,    # Membrane time constant in ms.
        'tau_refrac' : 0.0,     # Duration of refractory period in ms. 
        'tau_syn_E'  : 5.0,     # Decay time of excitatory synaptic current in ms.
        'tau_syn_I'  : 5.0,     # Decay time of inhibitory synaptic current in ms.
        'i_offset'   : 0.0,     # Offset current in nA
        'v_reset'    : -65.0,   # Reset potential after a spike in mV.
        'v_thresh'   : -50.0,   # Spike threshold in mV.
        'v_init'     : -65.0,   # Membrane potential in mV at t = 0
    }
    recordable = ['spikes', 'v']
    conductance_based = False

class IF_cond_alpha(StandardCellType):
    """
    Leaky integrate and fire model with fixed threshold and alpha-function-
    shaped post-synaptic conductance.
    """
    
    default_parameters = {
        'v_rest'     : -65.0,   # Resting membrane potential in mV. 
        'cm'         : 1.0,     # Capacity of the membrane in nF
        'tau_m'      : 20.0,    # Membrane time constant in ms.
        'tau_refrac' : 0.0,     # Duration of refractory period in ms.
        'tau_syn_E'  : 0.3,     # Rise time of the excitatory synaptic alpha function in ms.
        'tau_syn_I'  : 0.5,     # Rise time of the inhibitory synaptic alpha function in ms.
        'e_rev_E'    : 0.0,     # Reversal potential for excitatory input in mV
        'e_rev_I'    : -70.0,   # Reversal potential for inhibitory input in mV
        'v_thresh'   : -50.0,   # Spike threshold in mV.
        'v_reset'    : -65.0,   # Reset potential after a spike in mV.
        'i_offset'   : 0.0,     # Offset current in nA
        'v_init'     : -65.0,   # Membrane potential in mV at t = 0
    }
    recordable = ['spikes', 'v', 'gsyn']
    
class IF_cond_exp(StandardCellType):
    """
    Leaky integrate and fire model with fixed threshold and 
    exponentially-decaying post-synaptic conductance.
    """
    
    default_parameters = {
        'v_rest'     : -65.0,   # Resting membrane potential in mV. 
        'cm'         : 1.0,     # Capacity of the membrane in nF
        'tau_m'      : 20.0,    # Membrane time constant in ms.
        'tau_refrac' : 0.0,     # Duration of refractory period in ms.
        'tau_syn_E'  : 5.0,     # Decay time of the excitatory synaptic conductance in ms.
        'tau_syn_I'  : 5.0,     # Decay time of the inhibitory synaptic conductance in ms.
        'e_rev_E'    : 0.0,     # Reversal potential for excitatory input in mV
        'e_rev_I'    : -70.0,   # Reversal potential for inhibitory input in mV
        'v_thresh'   : -50.0,   # Spike threshold in mV.
        'v_reset'    : -65.0,   # Reset potential after a spike in mV.
        'i_offset'   : 0.0,     # Offset current in nA
        'v_init'     : -65.0,   # Membrane potential in mV at t = 0
    }
    recordable = ['spikes', 'v', 'gsyn']

class IF_cond_exp_gsfa_grr(StandardCellType):
    """
    Linear leaky integrate and fire model with fixed threshold,
    decaying-exponential post-synaptic conductance, conductance based spike-frequency adaptation,
    and a conductance-based relative refractory mechanism.

    See: Muller et al (2007) Spike-frequency adapting neural ensembles: Beyond mean-adaptation
    and renewal theories. Neural Computation 19: 2958-3010.

    See also: EIF_cond_alpha_isfa_ista
    """
    
    default_parameters = {
        'v_rest'     : -65.0,   # Resting membrane potential in mV. 
        'cm'         : 1.0,     # Capacity of the membrane in nF
        'tau_m'      : 20.0,    # Membrane time constant in ms.
        'tau_refrac' : 0.0,     # Duration of refractory period in ms.
        'tau_syn_E'  : 5.0,     # Decay time of the excitatory synaptic conductance in ms.
        'tau_syn_I'  : 5.0,     # Decay time of the inhibitory synaptic conductance in ms.
        'e_rev_E'    : 0.0,     # Reversal potential for excitatory input in mV
        'e_rev_I'    : -70.0,   # Reversal potential for inhibitory input in mV
        'v_thresh'   : -50.0,   # Spike threshold in mV.
        'v_reset'    : -65.0,   # Reset potential after a spike in mV.
        'i_offset'   : 0.0,     # Offset current in nA
        'v_init'     : -65.0,   # Membrane potential in mV at t = 0
        'tau_sfa'    : 100.0,   # Time constant of spike-frequency adaptation in ms
        'e_rev_sfa'  : -75.0,   # spike-frequency adaptation conductance reversal potential in mV
        'q_sfa'      : 15.0,    # Quantal spike-frequency adaptation conductance increase in nS
        'tau_rr'     : 2.0,     # Time constant of the relative refractory mechanism in ms
        'e_rev_rr'   : -75.0,   # relative refractory mechanism conductance reversal potential in mV
        'q_rr'       : 3000.0   # Quantal relative refractory conductance increase in nS   
    }
    recordable = ['spikes', 'v', 'gsyn']

    
class IF_facets_hardware1(StandardCellType):
    """
    Leaky integrate and fire model with conductance-based synapses and fixed 
    threshold as it is resembled by the FACETS Hardware Stage 1. 
    
    The following parameters can be assumed for a corresponding software
    simulation: cm = 0.2 nF, tau_refrac = 1.0 ms, e_rev_E = 0.0 mV.  
    For further details regarding the hardware model see the FACETS-internal Wiki:
    https://facets.kip.uni-heidelberg.de/private/wiki/index.php/WP7_NNM
    """
    
    default_parameters = {
        'g_leak'    :   20.0,     # nS
        'v_reset'   :  -80.0,     # mV
        'e_rev_I'   :  -80.0,     # mV
        'v_rest'    :  -75.0,     # mV
        'v_thresh'  :  -55.0,     # mV
        'tau_refrac':    1.0      # ms
    }
    recordable = ['spikes', 'v']


class HH_cond_exp(StandardCellType):
    """Single-compartment Hodgkin-Huxley model."""
    
    default_parameters = {
        'gbar_Na'   : 20000.0,
        'gbar_K'    : 6000.0,
        'g_leak'    : 10.0,
        'cm'        : 0.2,
        'v_offset'  : -63.0,
        'e_rev_Na'  : 50.0,
        'e_rev_K'   : -90.0,
        'e_rev_leak': -65.0,
        'e_rev_E'   : 0.0,
        'e_rev_I'   : -80.0,
        'tau_syn_E' : 0.2,
        'tau_syn_I' : 2.0,
        'i_offset'  : 0.0,
        'v_init'    : -65.0,
    }
    recordable = ['spikes', 'v', 'gsyn']

class EIF_cond_alpha_isfa_ista(StandardCellType):
    """
    Exponential integrate and fire neuron with spike triggered and
    sub-threshold adaptation currents (isfa, ista reps.) according to:
    
    Brette R and Gerstner W (2005) Adaptive Exponential Integrate-and-Fire Model
    as an Effective Description of Neuronal Activity. J Neurophysiol 94:3637-3642

    See also: IF_cond_exp_gsfa_grr, EIF_cond_exp_isfa_ista
    """
    
    default_parameters = {
        'v_init'    : -70.6,  # Initial membrane potential in mV
        'w_init'    : 0.0,    # Initial spike-adaptation current in nA
        'cm'        : 0.281,  # Capacitance of the membrane in nF
        'tau_refrac': 0.0,    # Duration of refractory period in ms.
        'v_spike'   : -40.0,    # Spike detection threshold in mV.
        'v_reset'   : -70.6,  # Reset value for V_m after a spike. In mV.
        'v_rest'    : -70.6,  # Resting membrane potential (Leak reversal potential) in mV.
        'tau_m'     : 9.3667, # Membrane time constant in ms
        'i_offset'  : 0.0,    # Offset current in nA
        'a'         : 4.0,    # Subthreshold adaptation conductance in nS.
        'b'         : 0.0805, # Spike-triggered adaptation in nA
        'delta_T'   : 2.0,    # Slope factor in mV
        'tau_w'     : 144.0,  # Adaptation time constant in ms
        'v_thresh'  : -50.4,  # Spike initiation threshold in mV
        'e_rev_E'   : 0.0,    # Excitatory reversal potential in mV.
        'tau_syn_E' : 5.0,    # Rise time of excitatory synaptic conductance in ms (alpha function).
        'e_rev_I'   : -80.0,  # Inhibitory reversal potential in mV.
        'tau_syn_I' : 5.0,    # Rise time of the inhibitory synaptic conductance in ms (alpha function).
    }
    recordable = ['spikes', 'v', 'gsyn']

class EIF_cond_exp_isfa_ista(StandardCellType):
    """
    Exponential integrate and fire neuron with spike triggered and
    sub-threshold adaptation currents (isfa, ista reps.) according to:
    
    Brette R and Gerstner W (2005) Adaptive Exponential Integrate-and-Fire Model
    as an Effective Description of Neuronal Activity. J Neurophysiol 94:3637-3642

    See also: IF_cond_exp_gsfa_grr, EIF_cond_alpha_isfa_ista
    """
    
    default_parameters = {
        'v_init'    : -70.6,  # Initial membrane potential in mV
        'w_init'    : 0.0,    # Initial spike-adaptation current in nA
        'cm'        : 0.281,  # Capacitance of the membrane in nF
        'tau_refrac': 0.0,    # Duration of refractory period in ms.
        'v_spike'   : -40.0,    # Spike detection threshold in mV.
        'v_reset'   : -70.6,  # Reset value for V_m after a spike. In mV.
        'v_rest'    : -70.6,  # Resting membrane potential (Leak reversal potential) in mV.
        'tau_m'     : 9.3667, # Membrane time constant in ms
        'i_offset'  : 0.0,    # Offset current in nA
        'a'         : 4.0,    # Subthreshold adaptation conductance in nS.
        'b'         : 0.0805, # Spike-triggered adaptation in nA
        'delta_T'   : 2.0,    # Slope factor in mV
        'tau_w'     : 144.0,  # Adaptation time constant in ms
        'v_thresh'  : -50.4,  # Spike initiation threshold in mV
        'e_rev_E'   : 0.0,    # Excitatory reversal potential in mV.
        'tau_syn_E' : 5.0,    # Decay time constant of excitatory synaptic conductance in ms.
        'e_rev_I'   : -80.0,  # Inhibitory reversal potential in mV.
        'tau_syn_I' : 5.0,    # Decay time constant of the inhibitory synaptic conductance in ms.
    }
    recordable = ['spikes', 'v', 'gsyn']

class SpikeSourcePoisson(StandardCellType):
    """Spike source, generating spikes according to a Poisson process."""

    default_parameters = {
        'rate'     : 1.0,     # Mean spike frequency (Hz)
        'start'    : 0.0,     # Start time (ms)
        'duration' : 1e6      # Duration of spike sequence (ms)
    }
    recordable = ['spikes']
    synapse_types = ()

class SpikeSourceInhGamma(StandardCellType):
    """
    Spike source, generating realizations of an inhomogeneous gamma process,
    employing the thinning method.

    See: Muller et al (2007) Spike-frequency adapting neural ensembles: Beyond
    mean-adaptation and renewal theories. Neural Computation 19: 2958-3010.
    """

    default_parameters = {
        'a'        : numpy.array([1.0]), # time histogram of parameter a of a gamma distribution (dimensionless)
        'b'        : numpy.array([1.0]), # time histogram of parameter b of a gamma distribution (seconds)
        'tbins'    : numpy.array([0]),   # time bins of the time histogram of a,b in units of ms
        'rmax'     : 1.0,                # Rate (Hz) of the Poisson process to be thinned, usually set to max(1/b)
        'start'    : 0.0,                # Start time (ms)
        'duration' : 1e6                 # Duration of spike sequence (ms)
    }
    recordable = ['spikes']
    synapse_types = ()

class SpikeSourceArray(StandardCellType):
    """Spike source generating spikes at the times given in the spike_times array."""
    
    default_parameters = { 'spike_times' : [] } # list or numpy array containing spike times in milliseconds.
    recordable = ['spikes']
    synapse_types = ()    
           
    def __init__(self, parameters):
        if parameters and 'spike_times' in parameters:
            parameters['spike_times'] = numpy.array(parameters['spike_times'], 'float')
        StandardCellType.__init__(self, parameters)
        