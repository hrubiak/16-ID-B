2D x-ray diffraction (XRD) imaging
----------------------------------

There are 3 different ways to conduct 2D XRD imaging:

(1) Diptera's X-ray imaging tool with Pilatus
(2) HPCAT SXD's Grid Scan with either MAR CCD or Pilatus.
Sample is rotated at each position when XRD is collected.
(3) MEDM scan_more.adl

Each method is described below.

(1) Diptera's X-ray imaging tool with Pilatus

- Click Imaging button at the bottom of the Diptera control page
  to open the 'X-ray Imaging Tools' control
- Press 'Initialize' button, and check 'Enable'
- 2D parameters and count time are set in scan control
- Press 'start scan' to start

(2) HPCAT SXD's Grid Scan with either MAR CCD or Pilatus.
    Sample is rotated at each position when XRD is collected.

- Open HPCAT SXD program on desk top. Select 'IDB laser
  heating' table, and a XR detector (either MARCCD or Pilatus).
- Press 'Confirm Choice' button to open HPCAT SXD control
  page.

- Note: The Detector path and user directory need to be set in
  detector control page before HPCAT SXD program is open.
- Set file name, rotation angle range and exposure time (D area
- Click 'Define' in D area to get sample center position
  Set 2D parameters in 'Grid Dimensions' area
- To start, press 'Grid Scan' button

(3) MEDM scan_more.adl

- Open scan_more.adl for 16IDB:scan1 and 16IDB:scan2 from
  the 'Scans' button in the 16IDB LH Table Control Panel

- Set scan parameters as shown below for an example of
  mapping LH table y (scan1) and z (scan2) from -0.2 to 0.2, 21 #
  pts and step size 0.02 and recording XRD with MAR CCD.

Note: (1) Increase the settling time in both scans to allow XR
detector enough time to start and to finish reading the image.
(2) XRD exposure time is set on Detector Control Page.