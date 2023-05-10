---
permalink: /Research/
title: Research
layout: collection
author_profile: true
comments: true
description: Details of my Research
gallery_research:
  - url: /assets/images/APS_cover.png
    image_path: /assets/images/APS_cover.png
    alt: "placeholder image 1"
    title: "Isosurface lambda-2 criterion of the flow over a curved plate at Re:125'000"
  - url: /assets/images/deformation_strain_cauchy.png
    image_path: /assets/images/deformation_strain_cauchy.png
    alt: "placeholder image 2"
    title: "Isocontour of structural deformation and stress field in a membrane wing during a cycle for various membrane elasticity"
  - url: /assets/images/poincare_collection.png
    image_path: /assets/images/poincare_collection.png
    alt: "placeholder image 3"
    title: "Poincare map of the velocity and position of the tip of a oscillating inverted flag for a lot of different flag stiffness"
---

&nbsp;

<p style="text-align:justify; margin-left:20px"> 
My research focuses on the computational fluid-structure interaction of membranes and shells, which are essential components of many engineering systems, such as heart valves, sails, and parachutes. These systems present highly complex and nonlinear behaviors that require advanced computational methods to accurately model and solve. Using large-scale computational methods, my research aims to provide a deeper understanding of these behaviors and answer key questions related to their design and performance. By applying my findings to practical engineering applications, I hope to contribute to the development of more efficient, reliable, and safe systems in a wide range of fields.</p>

<p style="text-align:justify; margin-left:20px">
To deal with the complex and nonlinear behaviors of thin structures in computational fluid-structure interaction, I have developed an immersed-boundary method that is specifically tailored to address the challenges posed by these structures. This method has proven to be highly effective in coupling a fluid solver to a generalized shell structural solver through a partitioned approach, allowing for a flexible coupling that can handle a wide range of applications.
</p>

<p style="text-align:justify; margin-left:20px">
One of the key challenges in this approach is solving the fixed point problem for the interface coupling condition. To tackle this, I use a quasi-Newton scheme that approximates the linear system common to all Newton-type methods via input/output pairs from previous time steps. This is an efficient approach that incorporates added-mass effects from the previous time step, allowing the solver to converge much faster than standard Gauss-Seidel relaxation methods.
</p>

<p style="text-align:justify; margin-left:20px">
The advantage of this solver is that it is not limited by the displacement of the structure, enabling us to study very large-scale deformations such as inverted flags or bat wings. This has opened up new avenues for research in understanding the behavior of thin structures in fluid-structure interaction, and has potential applications in a wide range of fields, from aerospace to biomedical engineering.
</p>

**Sample from my Research**

<hr>
<p style="font-size:16px">
Sample figures generate for my research.
</p>
{% include gallery id="gallery_research" class="full" %}