---
title: Range with Settings and cirular Network
description: Use settings to define a range of values in your application - or create your own interdependent network of settings.
weight: 10
---




```python
from ScopeFoundry.measurement import Measurement


class XSweep(Measurement):

    name = "x_sweep"

    def setup(self):
        # Define a range of X-values with start, stop, and step
        self.range = self.settings.New_Range("X", initials=(1, 2, 2))

    def run(self):
        # Access the array of X-values
        for x in self.range.array:
            # Perform operations for each X-value
            ...
```

The `New_Range` method creates six settings that allow the user to define a range of values. Three of those six are redundant.

To define the range, the user can either use:

- `X_start`  
- `X_stop`  

or:

- `X_range`  
- `X_center`  

To define the step size, the user can either use:

- `X_step`  
- `X_num`.  

# Circular Networks

These six settings above are interconnected to ensure the range remains self-consistent. For example, if `X_stop` is increased by the user, then both `X_range` and `X_center` are automatically updated accordingly.  
The reverse is also true; for example, if the user changes `X_range`, then `X_start` and `X_stop` are updated.  
This circular quality of interdependence would result in infinite recursion, with each setting updating the others.

To break this recursion, subclass `ScopeFoundry.lq_circular_network.LQCircularNetwork`.
