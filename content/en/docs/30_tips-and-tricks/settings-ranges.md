---
title: Defining a Range with Settings
description: Use settings to define a range of values in your application.
weight: 10
---

```python
from ScopeFoundry.measurement import Measurement


class CurrentSweep(Measurement):

    name = "current_sweep"

    def setup(self):
        # Define a range of currents with start, stop, and step values
        self.current_range = self.settings.New_Range("currents", initials=(1, 2, 2))

    def run(self):
        # Access the array of current values
        currents = self.current_range.array
        
        for cur in currents:
            ...
```

The example above will create 5 settings.

The user can use:

1. `_start`  
2. `_stop`  
3. `_step`  

to define a range. Alternatively, instead of using `start`/`stop`, the user can use:

1. `range`  
2. `center`  

The 5 settings are interconnected to ensure they remain self-consistent.