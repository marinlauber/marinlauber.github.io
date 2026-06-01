---
layout: article
title: Python-VPP
header:
    image: https://raw.githubusercontent.com/marinlauber/Python-VPP/refs/heads/master/Figure.png
tags: VPP
date: 2026-06-01
cover: https://raw.githubusercontent.com/marinlauber/Python-VPP/refs/heads/master/Figure.png
---

### Introduction

`Python-VPP` is a 3-DOF Velocity Prediction Program (VPP) written in pure Python. It predicts the sailing performance of yachts by solving force and moment equilibrium equations across a range of true wind speeds (TWS) and true wind angles (TWA), finding the boat speed and sail trim that satisfy hydrodynamic and aerodynamic equilibrium at each condition.

### Method

The program is based on the ORC-VPP framework, using their response surfaces for viscous and wave resistance of the hull and appendages, as well as their aerodynamic force coefficients. It is applicable to most relatively heavy-displacement monohull yachts.

The main inputs are a set of yacht parameters: appendage geometry (chord, span), hull properties (waterline length, displacement, draft, wetted surface area, righting moment arm), and standard sail measurements. These geometric quantities can be extracted from Rhino or any hull-design software. The core solver iterates over the TWS/TWA grid and minimises the force/moment residuals using a Newton-type scheme, producing a full performance polar.

### Examples

Some example output for the YD-41 (the reference yacht from *Principles of Yacht Design*) is shown below. The program can generate polar plots of boat speed and sail trim variables, as well as polar files in formats compatible with common routing software (Adrena, Qtlvm, Expedition).

![Python-VPP performance polar for the YD-41](https://raw.githubusercontent.com/marinlauber/Python-VPP/refs/heads/master/Figure.png)

### Code

The code is available as an open-source project, with full documentation at [marinlauber.github.io/Python-VPP](https://marinlauber.github.io/Python-VPP/):

[Source code](https://github.com/marinlauber/Python-VPP?tab=readme-ov-file)

Thanks to Thomas Dickson, an online app is also available if you prefer not to install the package locally:

[Online App](https://yacht-vpp.streamlit.app/VPP_%E2%9B%B5)