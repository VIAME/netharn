"""
References:
    https://github.com/alykhantejani/initializers
"""
import ubelt as ub
from os.path import dirname, exists, join
from netharn import util
import torch

from netharn.initializers import nninit_base


class Pretrained(nninit_base._BaseInitializer):
    """
    Attributes:
        fpath (str): location of the pretrained weights file
        initializer (_BaseInitializer): backup initializer if the weights can
            only be partially applied

    Example:
        >>> from netharn.initializers.nninit_core import *
        >>> from netharn.models import toynet
        >>> self = Orthogonal()
        >>> model = toynet.ToyNet2d()
        >>> self(model)
        >>> layer = torch.nn.modules.Conv2d(3, 3, 3)
        >>> self(layer)
    """
    def __init__(self, fpath, initializer=None):
        self.fpath = fpath
        if isinstance(initializer, str):
            from netharn import initializers
            initializer = getattr(initializers, initializer)()
        self.initializer = initializer

    def forward(self, model):
        from netharn import XPU
        xpu = XPU.from_data(model)
        model_state_dict = xpu.load(self.fpath)
        if 'model_state_dict' in model_state_dict:
            model_state_dict = model_state_dict['model_state_dict']
        nninit_base.load_partial_state(model, model_state_dict,
                                       initializer=self.initializer)

    def history(self):
        """
        if available return the history of the model as well
        """
        # TODO: check for train_info.json in a few different places
        info_dpath = dirname(dirname(ub.truepath(self.fpath)))
        info_fpath = join(info_dpath, 'train_info.json')
        if exists(info_fpath):
            return util.read_json(info_fpath)
        else:
            return '__UNKNOWN__'


class Orthogonal(nninit_base._BaseInitializer):
    """
    Same as HeNormal, but uses pytorch implementation

    Example:
        >>> from netharn.initializers.nninit_core import *
        >>> from netharn.models import toynet
        >>> self = Orthogonal()
        >>> model = toynet.ToyNet2d()
        >>> self(model)
        >>> layer = torch.nn.modules.Conv2d(3, 3, 3)
        >>> self(layer)
    """
    def __init__(self, gain=1):
        self.gain = gain

    def forward(self, model):
        nninit_base.apply_initializer(model, torch.nn.init.orthogonal, self.__dict__)


class KaimingUniform(nninit_base._BaseInitializer):
    """
    Same as HeNormal, but uses pytorch implementation

    Example:
        >>> from netharn.initializers.nninit_core import *
        >>> from netharn.models import toynet
        >>> self = KaimingUniform()
        >>> model = toynet.ToyNet2d()
        >>> self(model)
        >>> layer = torch.nn.modules.Conv2d(3, 3, 3)
        >>> self(layer)
    """
    def __init__(self, param=0, mode='fan_in'):
        self.a = param
        self.mode = mode

    def forward(self, model):
        nninit_base.apply_initializer(model, torch.nn.init.kaiming_uniform,
                                      self.__dict__)


class KaimingNormal(nninit_base._BaseInitializer):
    """
    Same as HeNormal, but uses pytorch implementation

    Example:
        >>> from netharn.initializers.nninit_core import *
        >>> from netharn.models import toynet
        >>> self = KaimingNormal()
        >>> model = toynet.ToyNet2d()
        >>> self(model)
        >>> layer = torch.nn.modules.Conv2d(3, 3, 3)
        >>> self(layer)
    """
    def __init__(self, param=0, mode='fan_in'):
        self.a = param
        self.mode = mode

    def forward(self, model):
        nninit_base.apply_initializer(model, torch.nn.init.kaiming_uniform,
                                      self.__dict__)


if __name__ == '__main__':
    """
    CommandLine:
        python -m netharn.initializers.nninit_core all
    """
    import xdoctest
    xdoctest.doctest_module(__file__)