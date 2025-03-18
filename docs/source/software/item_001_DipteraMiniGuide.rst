Diptera Miniguide
-----------------

*. . . derived from the Greek di ~ two, and ptera ~ wings*

A graphical user interface for generating and plotting 1D and 2D
flyscans

|image1|\ |image2|\ 

**The Diptera Graphical User Interface**

|image3|

To start Diptera:

Double-click the Diptera icon (should be located on control computer
desktop)

If you are prompted to select endstation (see below, left), please
ensure you choose the correct stages, click *Confirm choice* (most
stations will have autoselect feature in place).

Diptera will take a few seconds to configure and find the next scan
file. A window will be displayed to let you know the location was found
and the scan number was automatically incremented (see below, right),
otherwise, click *Browse* and select the location for scan files.

|image4|\ |image5|

Diptera should now be ready to use

**Scan Control Box**

This is the primary control box where the user selects the scan
stage(s), dimension, width, number of points, and count time. It also
contains the buttons for starting scans.

|image13|


.. container:: text-box

   To execute a (1D) flyscan:

   1. On the *Fly axis* row, select a stage from the drop-down menu
   2. Set the relative minimum and maximum stage positions (scan endpoints)
   3. Set the number of points
   4. Set the desired COUNT TIME (per point)
   5. Click START SCAN

   To execute a 2D flyscan:
   In addition to the steps described above . . .

   6. On the *Step axis* row, carry out steps 1-3 from above
   7. Click the checkbox to enable the second (step) dimension of the scan

.. note:: The step size must be some integral step of 0.0001 mm (e.g. 0.0050 or
          0.0002, but not 0.01000004). If this is violated, the LED will turn red
          and the scanning will be disabled.

.. hint:: Use ‘round’ extrema (0.050, not 0.052), and Points ending in 1
          (51, not 50).

*Scan directory* is automatically set when opening the program and *Scan
no.* automatically increments after each scan. User should not have to
modify these fields.

Pressing the Fly y (Fly z) button is the equivalent of selecting the
y-stage (z-stage) for the fly axis and then pressing the *START SCAN*
button.

After executing a 2D scan, the checkbox enabling the *Step axis* will be
automatically deselected; you must click it again before executing
another 2D scan.

Sometimes the desired speed of a scan will exceed a stage’s
capabilities. If so:

1. | The COUNT TIME will be automatically increased (and turn red),
   | after the scan it will return to the previous value and color, or .
     . .

2. An error message will appear prompting the user to modify scan
   parameters.

**Centering Control Box**

This is where the centering process is carried out. The centering
routine is essentially a special case of 2D scan where for the second
dimension, the step axis is the rotation stage, the min and max are -/+
omega for centering, and the number of points is 3.

|image16|

.. container:: text-box

   To execute the centering process:

   1. Set up a typical fly scan for the sample stack y-stage (Scan Control
      Box)

   2. Select delta omega (e.g., enter 6 to rotate -/+ 6 degrees)

   3. Click the *Enable* box

   4. Click START SCAN (Scan Control Box)

Step axis parameters will be autofilled, 2D scan will begin, window will
update after each step. After the scan, the first ‘Slice’ of the scan
(–omega) will be displayed:

|image21|

.. container:: text-box

   1. Scan center will be automatically determined (but drag sliders if
      necessary)

   2. Advance *Current Slice* and repeat step 5 until all centers are
      determined . . .

   3. . . . and all corrections and target position are calculated (button
      turns green)

   4. Click the green button to move x-stage to the target position

Centering will be automatically disabled; you must click *Enable* to
repeat the process.

**Intensity Control Box**

This is where the user selects the type of data plotted in the display
window.

|image22|

The data plotted in the display window is determined by the following
equation:

.. math:: I(signal)/I(reference)xScalefactor

If *I(reference)* checkbox is not checked, *I(reference)* = 1.

If *Data type* is ‘Derivative’, a point-to-point derivative of the
equation is plotted

*2D scaling*

For 2D plots user can adjust the contourmap max and min by
incrementing/decrementing the top and bottom entry boxes, respectively
(values from 0 – 100 %).

The number of colors can also be modified in the entry box on the far
right (4 – 128 colors).

.. note:: Due to the nature of flyscans, it is highly recommended to normalize the
         signal using the reference signal, i.e., keep I(reference) checkbox
         checked.

         All endstations have the same drop-down list for *Active Counter*, but
         not all endstations have all counters connected. Check with local
         contact if you want to change counters.

**Position Control Box**

This gives information about stage positions in relation to the vertical
bars on the plot

|image23|

After a scan, you can drag the blue lines to any point of interest. The
red dotted line will automatically follow as the mid-point between the
blue lines.

|image31|

To move the fly stage (listed as the *Active Element*), click the
*Minimum* (1), *Center* (2), or *Maximum* (3) box on the *Horizontal
axis* row

**Note:** For 2D scans, clicking the Center (2) button will also move
the step stage to the position (4) listed on the *Vertical axis* row.
This does NOT apply to centering scans.

**Plot Window**

|image32|\ |image33|

For a 1D plot (left), a simple routine will look for the min, mid, and
max intensity, and similarly, look for the left, mid, and right features
(defining the FWHM) of the scan object (e.g., DAC sample or crosshair).
These points are indicated by solid blue and dashed red lines. User can
drag the blue lines to desired postions, red lines are always redrawn as
mid points between blue lines.

The difference between the current stage position and the stage position
indicated by the vertical, dashed red line will appear in the
*Difference* label

For a 2D plot (right) user can click the mouse over any point to send
stage coordinates to the *Position Control* box. Clicking on the
*Center* button in the *Position Control* box will move both stages to
the desired postion.

Clicking *Overlay 2D Grid* will show a grid; the intersection of lines
indicate a single data point of the 2D scan

.. note:: Click the ‘Disk’ icon to save the image to disk

            One can zoom in/out using the toolbar icons

            One can always restore the original plot by clicking the ‘Home’ icon

**File Control Box**

Allows user to see path for current scan, load/save data, toggle between
scans and 1D slices of 2D scans

|image39|

To load a scan, click *Load Data* (1) and browse for desired file.

Click *Save ASCII* (2) to save a .txt file of the data currently
plotted. N.B. this is not the complete scan data saved in the binary
numpy file, but rather, the calculation (and resulting plot) determined
in *Intensity Control*

User can quickly browse recent plots using the arrow buttons (3)

Users can look at individual 1D ‘slices’ of 2D plots by clicking *2D
Slice* (4) and then toggling using the arrow buttons (4).

**Big buttons box**

**Overlays**

|image43|

To plot overlay data:

1. Click *Load Data* and browse to find the desired file, or

2. Click *Grab Data* to load the *Current Scan File* (File Control Box)

3. Check the checkbox to toggle the overlay on/off

..  note:: When you close the window, it automatically toggles the overlay(s) off

            Only 1D files can be overlaid. If you load a 2D file it will overlay
            slices if *2D Slice* is checked in the File Control Box. You can toggle
            which slice by clicking the arrow buttons.

**Big buttons box**

**Imaging**

This is for carrying out diffraction as the same time as a flyscan (1D
or 2D). This feature is not available at all endstations, nor is it
possible with all HPCAT area detectors. If in doubt, check with local
contact before attempting to use.

|image48|

| To carry of simultaneous diffraction:
| Ensure all scan parameters are set correctly in the scan control box

1. Establish connection with the detector by clicking *Initialize*

2. To change *Detector path* and *User directory*, you must change the
   path on the EPICS medm Area Detector control screen (not shown)

3. Enter the *Sample name* and *Image No.* (these will be sent to Area
   Detector)

4. Click *Enable*

5. Click START SCAN

.. note:: If the *User Directory* does not exist, the display label will be red
            (shown above) and scan cannot be executed. Create the folder in the
            user’s data directory and try again.

            User can automatically save ASCII files of scans (convenient for XRDI
            use, for example) by checking the *Write ASCII* box

            Enable is automatically deselected following a scan. User must enable it
            to execute another XRD scan.

**Big buttons box**

**Alignment**

This includes tools for alignment. It is intended for HPCAT staff use
only

|image49|

*Pseudo-Voigt Parameters (development):*

To characterize the focused beam with a spilt pseudo-voigt profile,
click *Focus Fit* (works only for derivative data of a 1D scan of sharp
edge).

*Full Centering Control*

This shows calculations for all three stages in full centering. Simply
execute the normal centering routine with crosshair and click *Move All*
to correct all three stages.

*Re-zero x, y, z*

These buttons are the equivalent of using SET in the motor record before
modifying RBV to 0.000 (commonly used with crosshair alignment). After
clicking one of these buttons, staff member must confirm intention to
re-zero stage RBV.

**Aborting a scan**

1D scans in Diptera CANNOT be aborted. Wait until the scan is finished
before moving motors or proceeding with your experiment.

2D scans in Diptera can be aborted by toggling a dedicated EPICS PV in
medm. The PV can be toggled ANYTIME during a scan, but the abort action
will be carried out ONLY at the end of a single fly pass.

Each station has an abort button that looks similar to the one below
(there may be other location(s) built into the endstation’s control
panel, also):

|image50|

To abort 2D scan, click this button. Be patient and wait for the current
fly pass to finish. The scan will stop and all stages and stage
parameters will return to original positions and values.

**Autostart Edits (STAFF ONLY)**

*To get Diptera to automatically open for your endstation:*

1. Find Diptera on your local machine and right-click

2. Select Edit with Notepad++

3. Navigate down to *Program Start* (near the end, shortly after line
   2650):

4. | Eight lines under *Program Start*, find the comment line:
   | # config.stack_choice.set('TEST')

5. Delete the first two characters of that line (# ) and

6. Modify the string in parenthese as follows:

+----------------------------------+-----------------------------------+
| BMB Laue Table                   | ‘BMB’                             |
+==================================+===================================+
| BMD                              | ‘BMDHL’                           |
+----------------------------------+-----------------------------------+
| IDB GP XPS                       | ‘GPHP’                            |
+----------------------------------+-----------------------------------+
| IDB GP Cryo                      | ‘GPHL’                            |
+----------------------------------+-----------------------------------+
| IDB LH                           | ‘IDBLH’                           |
+----------------------------------+-----------------------------------+
| IDD                              | ‘IDD’                             |
+----------------------------------+-----------------------------------+
| Test crate                       | ‘TEST’                            |
+----------------------------------+-----------------------------------+

7. For example, to autostart with IDB GP High Precision XPS Stages:

..

   config.stack_choice.set(‘GPHP’)

*To get Diptera to automatically find your savedata folder and next scan
number:*

1. Make sure you have mapped your ZEON\\epics\\saveData folder on your
   local machine as written in Diptera (see JSS to make sure it’s done
   properly)

2. Make sure you have a folder for the current year and run (e.g.,
   2017-1)

**softGlue configurations**

As of January 2017, all stations should be running unified softGlue
configurations.

These are loaded and maintained automatically.

**N.B.** If you use softGlue for other purposes, note that Diptera will
change the configuration automatically and will not change it back.
Please discuss with JSS how to manage this (there are some relatively
straightforward solutions)

See template belows:

softGlue for steppers:

|image51|

softGlue for XPS

|image52|


.. |image1| image:: /images/software/diptera/media/image1.jpeg
   :width: 300px
.. |image2| image:: /images/software/diptera/media/image2.jpeg
   :width: 300px
.. |image3| image:: /images/software/diptera/media/image3.png
   :width: 6in
.. |image4| image:: /images/software/diptera/media/image4.png
   :width: 1.88612in
.. |image5| image:: /images/software/diptera/media/image5.png
   :width: 3.625in

.. |image13| image:: /images/software/diptera/media/image13.png
   :width: 5.60134in

.. |image16| image:: /images/software/diptera/media/image16.png
   :width: 5.54087in

.. |image21| image:: /images/software/diptera/media/image21.png
   :width: 6in
.. |image22| image:: /images/software/diptera/media/image22.png
   :width: 5.67051in
.. |image23| image:: /images/software/diptera/media/image23.png
   :width: 5.5372in


.. |image31| image:: /images/software/diptera/media/image31.png
   :width: 6in
.. |image32| image:: /images/software/diptera/media/image17.png
   :width: 2.68611in
.. |image33| image:: /images/software/diptera/media/image18.png
   :width: 2.68964in



.. |image39| image:: /images/software/diptera/media/image39.png
   :width: 5.54795in

.. |image43| image:: /images/software/diptera/media/image43.png
   :width: 6in

.. |image48| image:: /images/software/diptera/media/image48.png
   :width: 6in
.. |image49| image:: /images/software/diptera/media/image49.png
   :width: 6in
.. |image50| image:: /images/software/diptera/media/image50.png
   :width: 2.77083in
.. |image51| image:: /images/software/diptera/media/image51.png
   :width: 6in
.. |image52| image:: /images/software/diptera/media/image52.png
   :width: 6in