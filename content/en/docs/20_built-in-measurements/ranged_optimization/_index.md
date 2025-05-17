---
title: Ranged Optimization
description: Maximize a signal within a range.
weight: 1
---

Sweeps a setting \\(z\\) within a discrete interval \\(I\\), measures an optimization quantity \\(f(z)\\) and calculates \\(z_0\\) such that:


```math
f(z_0) \geq f(z) \, \, \, \, \, \, \forall z \in I
```

finally sets \\(z = z_0 + z_{offset}\\).

### Add to your app:

```python
    def setup(self):

        from ScopeFoundry import RangedOptimization

        self.add_measurement(RangedOptimization(self))
```


![overview](overview.png)

The interval \\(I\\) is defined by \\((z_{center}, z_{span}, z_{num})\\).

You can further post process the data to get a more accurate \\(z_0\\).

