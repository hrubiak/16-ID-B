Understanding Radiometric Temperature Measurement in Laser-Heated DAC Experiments
==================================================================================

Introduction
------------

In laser-heated diamond anvil cell (DAC) experiments, we measure temperature by collecting 
**spectrally-resolved thermal radiation** emitted from the hotspot. This light carries a spectral signature that reveals the sample temperature.

What Are We Measuring?
----------------------

The detector collects photons in the **600–800 nm** range. This range includes visible and near-infrared light, where thermal radiation intensity varies significantly with temperature.

.. figure:: /images/operation/lh/lh_radiometry_measurement.png
   :align: center
   :width: 40%

   Conceptual illustration of the laser-heated DAC experiment with spectral signal going into a detector.

Black-body Radiation and Temperature
------------------------------------

Higher temperatures shift the **peak of emission** to shorter wavelengths and **increase the emitted intensity**.

.. figure:: /images/operation/lh/lh_radiometry_blackbody.png
   :align: center
   :width: 90%

   Planck’s law curves for various temperatures, with the 600–800 nm range highlighted.

Why Exposure Time and Gain Matter
---------------------------------

Because radiation intensity **increases rapidly with temperature** (~ \( T^4 \)), setting the correct **exposure time** and **detector gain** is essential:

- Too little exposure → low signal-to-noise
- Too much exposure → saturation and loss of spectral data

.. figure:: /images/operation/lh/lh_radiometry_SB-Law.png
   :align: center
   :width: 90%

   Emitted power scales with the fourth power of temperature, as described by the Stefan–Boltzmann law.

What Does Hotter Look Like?
---------------------------

The color of thermal emission changes with temperature, transitioning from dull red to bright white and beyond.

.. figure:: /images/operation/lh/lh_radiometry_thermal_color.svg
   :align: center
   :width: 80%

   Visual reference for black-body color temperature, ranging from 1000 K to 12000 K.

Summary
-------

- ✅ Radiation is collected between **600–800 nm**
- ✅ Intensity increases with **temperature (\( T^4 \))**
- ✅ Adjust **exposure time and gain** based on expected temperature
- ✅ Avoid **saturation** to ensure accurate temperature measurement

For help with setup or interpretation, contact the beamline scientist.