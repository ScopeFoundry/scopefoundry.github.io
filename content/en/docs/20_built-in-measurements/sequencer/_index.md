---
title: Sequencer
description: Save sequences of measurements and other ScopeFoundry operations for later reuse.
weight: 1

---

To add to your app:

```python
    def setup(self):

        from ScopeFoundry import Sequencer, SweepSequencer

        self.add_measurement(Sequencer)
```

Check the available operation in the right panel. Hover over the operations label to display a description. 

On the left panel you see the actual script. Note that it can be saved for later reused.

![overview](overview.png)

Another Measurement, `SweepSequencer` , wraps the `Sequencer` into another for-loop.