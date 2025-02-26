---
title: Defining a range with settings
description:  Useful online to define a range of values using settings
weight: 10
---

```python
from ScopeFoundry.measurement import Measurement


class CurrentSweep(Measurement):

    name = "current_sweep"


    def setup(self):

        self.current_range = self.settings.New_Range("currents", initials=(1, 2, 2))

    def run(self):

        currents = self.current_range.array
        
        for cur in currents:
          	...

```

the example above will create 5 settings.

The user can use:

1. _start 
2. _stop
3. _step

to define a range. Alternatively instead of using start/stop the user can use

1. range
2. center

The 5 settings are interconnected so that to stay self consistent. 