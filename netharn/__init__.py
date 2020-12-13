"""
# Command to regenerate the the autogenerated portion of this file
# (Remote the --dry to actually run it)
mkinit netharn --noattrs --dry
mkinit netharn --noattrs
"""
__version__ = '0.5.13'

try:
    # PIL 7.0.0 removed PIL_VERSION, which breaks torchvision, monkey patch it
    # back in.
    import PIL
    PIL.PILLOW_VERSION = PIL.__version__
except (AttributeError, Exception):
    pass


# patch for imgaug
try:
    import numpy as np
    np.random.bit_generator = np.random._bit_generator
except (AttributeError, Exception):
    pass


from netharn.api import (
    Initializer, Optimizer, Criterion, Loaders, Scheduler, Dynamics,
    configure_hacks, configure_workdir,
)
from netharn.device import (XPU,)
from netharn.fit_harn import (FitHarn,)
from netharn.hyperparams import (HyperParams,)
from netharn.monitor import (Monitor,)
from netharn.analytic.output_shape_for import (
    OutputShapeFor, OutputShape, HiddenShapes)
from netharn.analytic.receptive_field_for import (
    ReceptiveFieldFor, ReceptiveField, HiddenFields)

__extra_all__ = [
    'Initializer',
    'Optimizer',
    'Criterion',
    'Loaders',
    'Scheduler',
    'Dynamics',
    'configure_hacks',
    'configure_workdir',

    'XPU',
    'FitHarn',
    'HyperParams',
    'Monitor',
    'Initializer',

    'OutputShapeFor',
    'OutputShape',
    'HiddenShapes',

    'ReceptiveFieldFor',
    'ReceptiveField',
    'HiddenFields',
]

## AUTOGENERATED AFTER THIS POINT
# <AUTOGEN_INIT>
from netharn import api
from netharn import criterions
from netharn import data
from netharn import device
from netharn import exceptions
from netharn import fit_harn
from netharn import hyperparams
from netharn import initializers
from netharn import layers
from netharn import metrics
from netharn import mixins
from netharn import models
from netharn import monitor
from netharn import optimizers
from netharn import prefit
from netharn import schedulers
from netharn import util
from netharn.analytic import analytic_for
from netharn.analytic import output_shape_for
from netharn.analytic import receptive_field_for

__all__ = ['Criterion', 'Dynamics', 'FitHarn', 'HiddenFields', 'HiddenShapes',
           'HyperParams', 'Initializer', 'Initializer', 'Loaders', 'Monitor',
           'Optimizer', 'OutputShape', 'OutputShapeFor', 'ReceptiveField',
           'ReceptiveFieldFor', 'Scheduler', 'XPU', 'analytic_for', 'api',
           'configure_hacks', 'configure_workdir', 'criterions', 'data',
           'device', 'exceptions', 'fit_harn', 'hyperparams',
           'initializers', 'layers', 'metrics', 'mixins', 'models', 'monitor',
           'optimizers', 'output_shape_for', 'prefit', 'receptive_field_for',
           'schedulers', 'util']
# </AUTOGEN_INIT>
