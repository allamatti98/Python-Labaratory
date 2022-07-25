#Method 1
import Speed.Processors, Speed.Converters
Speed.Processors.ContactHorizontal("0704123574")
Speed.Converters.kg2lbs(78)

#Method 2
from Speed.Converters import kg2lbs, lbs2kgs
kg2lbs(76)
lbs2kgs(887)

#Method 3
from Speed import Converters, Processors
Converters.kg2lbs(34)
Processors.ContactHorizontal("0704123574")