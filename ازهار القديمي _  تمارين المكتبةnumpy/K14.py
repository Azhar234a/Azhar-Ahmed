from numpy.random import MT19937
from numpy.random import RandomState, SeedSequence
rs = RandomState(MT19937(SeedSequence(123456789)))
# Later, you want to restart the stream
rs = RandomState(MT19937(SeedSequence(987654321)))