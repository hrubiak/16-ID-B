2D x-ray diffraction (XRD) imaging
----------------------------------

There are 3 different ways to conduct 2D XRD imaging:

1. Diptera's X-ray imaging tool with Pilatus
2. HPCAT SXD's Grid Scan with either MAR CCD or Pilatus. 
   Sample is rotated at each position when XRD is collected.
3. MEDM scan_more.adl

Each method is described below.

1. Diptera's X-ray imaging tool with Pilatus

   - Click Imaging button at the bottom of the Diptera control page
     to open the 'X-ray Imaging Tools' control
   - Press 'Initialize' button, and check 'Enable'
   - 2D parameters and count time are set in scan control
   - Press 'start scan' to start


2. HPCAT SXD's Grid Scan with either MAR CCD or Pilatus.
   
    Sample is rotated at each position when XRD is collected.

   - Open HPCAT SXD program on desk top. Select 'IDB laser
     heating' table, and a XR detector (either MARCCD or Pilatus).
   - Press 'Confirm Choice' button to open HPCAT SXD control
     page.

   - Note: The Detector path and user directory need to be set in
     detector control page before HPCAT SXD program is open.
   - Set file name, rotation angle range and exposure time D area
   - Click 'Define' in D area to get sample center position
     Set 2D parameters in 'Grid Dimensions' area
   - To start, press 'Grid Scan' button

3. Setting up a two-dimensional map of XRD patterns at 16-ID-B using the EPICS scan record in MEDM.

   .. figure:: /images/operation/epics/2d_scan/16IDB_dacxrd_LH_scans.png
      :alt: 16IDB_dacxrd_LH.adl
      :width: 540px
      :align: center

  From the main laser heating table control panel, open Scan-1 and Scan-2 from the Scans menu, these will open as two new separate windows.

  .. figure:: /images/operation/epics/2d_scan/16IDB_dacxrd_LH_scans_1.png
      :alt: scan_more.adl
      :width: 300px
      :align: center

  Within Scan-1, set the Positioner read as XpsLH:m2.RBV and the drive as XpsLH:m2.VAL. This corresponds to having the scan move and read back the position of LH CEN Y, the horizontal motion on the LH table sample stage.

  .. figure:: /images/operation/epics/2d_scan/16IDB_dacxrd_LH_scans_2.png
      :alt: scan_more.adl
      :width: 300px
      :align: center

  Set up the desired number of points for your scan using **#PTS**, and the range for your scan using the **START** and **END** fields. The **STEP** **SIZE** and **WIDTH** will be automatically calculated used the start and end positions and number of points requested.

  .. figure:: /images/operation/epics/2d_scan/16IDB_dacxrd_LH_scans_3.png
      :alt: scan_more.adl
      :width: 300px
      :align: center

  In this example, a scan from -10 µm to +10 µm in the Y direction with 5 µm step size is input.
  To trigger the Pilatus detector at each point, input **16pil-idb:cam1:Acquire** into field 2 of the **DetTriggers** block in **Scan-1**.

  .. figure:: /images/operation/epics/2d_scan/16IDB_dacxrd_LH_scans_4.png
      :alt: scan_more.adl
      :width: 300px
      :align: center

  If you make a typo in any of the fields requesting motor or detector variables, the title of that field will highlight itself red to alert you that it does not recognise the input.

  .. figure:: /images/operation/epics/2d_scan/16IDB_dacxrd_LH_scans_5.png
      :alt: scan_more.adl
      :width: 300px
      :align: center

  Remember that EPICS variables are case-sensitive. Remember also in MEDM that you must keep your mouse pointer inside the field when typing, and that you should hit Enter to lock in your entry before moving the pointer away.

  Next, in **Scan-2**, enter **XpsLH:m3.RBV** and **XpsLH:m3.VAL** as the read and drive variables, respectively. This will instruct **Scan-2** to move **LH SAM Z**, the vertical motion of the LH table sample stage.

  As before, set the number of desired steps in **#PTS** field in the upper-right hand corner, and the size of the vertical scan in the **START** and **END** fields.

  .. figure:: /images/operation/epics/2d_scan/16IDB_dacxrd_LH_scans_6.png
      :alt: scan_more.adl
      :width: 300px
      :align: center

  In this example, a scan from -10 µm to +10 µm in the Z direction with 5 µm step size is input.

  Lastly, in the Pilatus control panel, set your desired XRD exposure time, name for your data files, and an appropriate file path. It is generally recommended to create a new subdirectory for each map acquisition.

  .. figure:: /images/operation/epics/16IDB_PilatusShort.adl.png
      :alt: 16IDB_PilatusShort.adl.adl
      :width: 720px
      :align: center


  To begin the 2D map, press the **SCAN** button in **Scan-2**.

    .. figure:: /images/operation/epics/2d_scan/16IDB_dacxrd_LH_scans_7.png
      :alt: scan_more.adl
      :width: 300px
      :align: center