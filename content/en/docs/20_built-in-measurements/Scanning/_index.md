---
title: Scanning and Sweeping
description: Choose a measurement paradigm based on your needs.
date: 2025-06-01
---

Since version 2.1, ScopeFoundry provides two built in measurements in which the following cycling repeats:

1. Change the position, voltage, ... in predetermined way
2. Collect data

For this common task ScopeFoundry provides several solutions. Read the following to decide which fits your task:

1. For [spatial scanning](spatial-scanning):

   - requires subclassing and override a view methods.
   - Natively has a concept of spatiality in 2D and 3D, which gives end-users an advanced interaction experience.

2. For generic setting [sweeping](sweeping): 

   - Works out of the Box! This Measurement can collect data and run other measurements without subclassing. 
   - Easier to extend with additional data channels by providing a flexible data structure and composing multiple  `Collector` classes.
   - Currently supports 1, 2 and 4 dimensional sweeping.
   - New in ScopeFoundry 2.1 and is still experimental. Internal working is subject to change
   
   

For your own Measurement from scratch consider using this [shortcut](https://scopefoundry.org/docs/30_tips-and-tricks/settings-ranges/).

