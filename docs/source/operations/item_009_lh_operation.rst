Laser heating experiment related control and operation
------------------------------------------------------

**Turn laser on**

Two lasers for up- and down-stream side heating respectively.

1. Turn the power key to 'ON' position.
2. Press the REMOTE START button.
3. Turn on laser interlock by press the laser 1 ON button on the
   laser interlock panel (on the wall near IDB door, one button
   controls the interlock of both lasers)
4. Press emission ON button.
   Laser power is controlled on medm laser heating control page.

**Turn laser off**

1. Laser emission can be turned off by pressing the EMISSION OFF
   button, by turning off the laser safety interlock, or by opening
   the hutch door.
2. To turn off the power supply, turn the power key to off
   position.

Laser heating temperature measurement software
==============================================

Software name: PyRadiant (former T-View)

Location: Desk top of laser heating temperature measurement
computer. 

PyRadiant user manual folder

Laser heating system operation - CW mode
========================================

The laser heating control page can be opened by clicking the
LASER HEATING button (blue color) at the upper right corner of
the LH table control page.

.. figure:: /images/operation/epics/16IDB_dacxrd_LH_annotated_arrow.png
   :alt: 16IDB_dacxrd_LH.adl
   :width: 540px
   :align: center 



.. figure:: /images/operation/epics/LH_control.adl.png
   :alt: LH_control.adl
   :width: 540px
   :align: center

1. Align DAC to the rotation center of the sample stage, and visually
   observe the cell to make sure that the heating optics can be
   moved in safely.

2. Move the optics in by clicking the IN buttons in "Heating Unit-Y
   Control". If one of the IN button is missing, it means the optics
   may be blocked, and moving it in may cause collision. Make sure
   the omega angle of the sample stage is at zero, and the 80-micron
   clean-up pinhole X = 0 (should visually confirm that pinhole tube is
   not blocking the optics). The button should appear once OMEGA
   = 0 and pinhole X = 0 are met.

3. To observe the sample images, the white lights need to be at IN
   position by clicking the buttons on both sides. A solid yellow
   circle next to the IN button indicates the white light mirror is at IN
   position. Then turn on the white light.

4. You should see the sample images on the monitors. The focus of
   the images can be adjusted by moving the laser focus lenses up
   and down (twick right is up and left is down). Focus the images.

5. For in-situ laser heating with XRD, you will need to align the x-ray
   fluorescence spot. First observe the XR fluorescence spots on
   both monitors and align each to the black dot on the two screen.
   The black dot is the image of spectrograph pinhole that collects
   the thermal radiation for temperature determination. X-ray beam
   and heating laser have been previously aligned with this pinhole
   for precise in-situ measurement. For users, please follow the
   following steps:

   a. Turn off the white light and move the white light mirror to off
      position
   b. XRD control at scan mode to open the XR shutter (adjust
      camera CCD time if needed)
   c. Adjust the heating mirrors to align the fluorescence images to
      the corresponding pinhole image respectively.

6. To check the alignment, select a spot in the cell that can be seen
   from both sides (sample marker). Move the spot on one side to
   align with the black dot by moving the sample stage's cenY and
   samZ. Then observe the spot on the monitor of the other side. If
   it aligns with the black dot, it means your alignment is successful.
   Very often it's not aligned. In this case, you will need to decide 
   which side to trust based on the quality of the fluorescence spot
   (FS). For example, if you have a sharp fluorescence spot on the
   down-stream side, adjust the down-stream heating mirror to align
   FS. Then use the sample marker to align the up-stream side.

7. Once you finish step 6., you can select a position on sample for
   heating by adjusting cenY and samZ to align the position with the
   black dot.

8. Laser power can be controlled together for both lasers or separately.

9. Temperature measurement is carried out by pressing 'Start T'
   button after setting proper ccd time.


Modulation pulse laser heating experiment setup
===============================================

This document describes the setup of single pulse laser heating
experiment with three XRD pulses before, during and after the
heating pulse.

1. Electronic connection

.. figure:: /images/operation/LH_timing_electronics_diagram.png
   :alt: LH_timing_electronics_diagram
   :width: 720px
   :align: center 