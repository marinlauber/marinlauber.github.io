---
title: Gallery
layout: archive
permalink: /Gallery/
author_profile: true
comments: true
description: A Gallery of my work.
categories:
  - Post Formats
tags:
  - gallery
  - Post Formats
  - tiled
gallery:
  - url: /assets/images/attractor_1.png
    image_path: /assets/images/attractor_1.png
    alt: "placeholder image 1"
    title: "Image 1 title caption"
  - url: /assets/images/attractor_2.png
    image_path: /assets/images/attractor_2.png
    alt: "placeholder image 2"
    title: "Image 2 title caption"
  - url: /assets/images/attractor_3.png
    image_path: /assets/images/attractor_3.png
    alt: "placeholder image 3"
    title: "Image 3 title caption"
  - url: /assets/images/attractor_4.png
    image_path: /assets/images/attractor_4.png
    alt: "placeholder image 4"
    title: "Image 4 title caption"
  - url: /assets/images/attractor_8.png
    image_path: /assets/images/attractor_8.png
    alt: "placeholder image 5"
    title: "Image 5 title caption"
  - url: /assets/images/attractor_5.png
    image_path: /assets/images/attractor_5.png
    alt: "placeholder image 6"
    title: "Image 6 title caption"
  - url: /assets/images/attractor_6.png
    image_path: /assets/images/attractor_6.png
    alt: "placeholder image 7"
    title: "Image 7 title caption"
  - url: /assets/images/attractor_7.png
    image_path: /assets/images/attractor_7.png
    alt: "placeholder image 8"
    title: "Image 8 title caption"
gallery2:
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
gallery3:
  - image_path: /assets/images/output.gif
    alt: "placeholder image 2"
  - image_path: /assets/images/fempar.gif
    alt: "placeholder image 2"
gallery4:
  - image_path: /assets/images/vismara.png
    alt: "Vismara Marine"
---

<h2 style="font-size:18px">Attractors</h2>
<hr>
<p style="font-size:16px">
Some Random Text
</p>

{% include gallery id="gallery" layout="half" caption="Attractors" %}

<h2 style="font-size:18px">Others</h2>
<hr>
<p style="font-size:16px">
Some Random Text
</p>

{% include gallery id="gallery2" class="full" caption="Others" %}

<h2 style="font-size:18px">Gifs</h2>
<hr>
<p style="font-size:16px">
Some Random Text
</p>

{% include gallery id="gallery3" class="full" caption="GIFs" %}

<h2 style="font-size:18px">CFD</h2>
<hr>
<p style="font-size:16px">
Some Random Text
</p>

{% include gallery id="gallery4" class="full" caption="CFD" %}
