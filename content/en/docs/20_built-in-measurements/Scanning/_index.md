---
title: Scanning and Sweeping
description: Choose a measurement paradigm based on your needs.
---
Since version 2.1, ScopeFoundry provides two built in measurements in which the following cycling repeats:

1. change a setting (i.e move an actuator) in predetermined way
2. collect data at that setting

Read the following to decide which fits your task:

1. For [spatial scanning](spatial-scanning):

   - requires subclassing and override a view methods.
   - Natively has a concept of spatiality in 2D and 3D, which gives end-users an advanced interaction experience.
2. For generic setting [sweeping](sweeping): 

   - Works out of the Box! This Measurement can collect data and run other measurements without subclassing. 
   - Easier to extend with additional data channels by providing a flexible data structure and composing multiple  `Collector` classes.
   - Currently supports 2 and 4 dimensional sweeping.

