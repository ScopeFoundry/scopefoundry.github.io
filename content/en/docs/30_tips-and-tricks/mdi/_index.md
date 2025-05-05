---
title: Minimal App Launch
description: Loads measurement UI’s lazily for minimal view and faster boot time.
weight: 10
---

Setting `mdi = False` in the app class definition omits loading measurement UIs at startup, reducing startup time. However, the UIs can be loaded individually later.

```python
class FancyApp(BaseMicroscopeApp):

    name = "fancy app"
    mdi = False
```

![mdi-false](mdi-false.png)
