__all__ = []

from scikits.talkbox.tools import *
import scikits.talkbox.tools as tools
__all__ += tools.__all__

import scikits.talkbox.linpred as linpred
from scikits.talkbox.linpred import *
__all__ += linpred.__all__

import version

from numpy.testing import Tester

test = Tester().test
bench = Tester().bench
