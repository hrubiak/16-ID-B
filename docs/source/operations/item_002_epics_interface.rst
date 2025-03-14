Start Laser Heating EPICS/MEDM user interface
---------------------------------------------

On the Windows desktop of the control computer, users will find a shortcut named ``16idb MEDM``.

.. note:: MobaXterm program should be started or runnning in the background before opening the MEDM interface, otherwise
          the interface will not start. 


Attached below is a screen shot of the 16ID-B upper level status/control panel.

.. figure:: /images/operation/epics/00_16IDB.adl.png
   :alt: 00_16ID.adl
   :width: 200px
   :align: center

To operate Laser Heating Table

Click on "Laser Heating Table" to start 16IDB LH Table control
panel. You will find all x-ray diffraction experiment operation
related buttons on this panel.

.. figure:: /images/operation/epics/16IDB_dacxrd_LH.png
   :alt: 16IDB_dacxrd_LH.adl
   :width: 540px
   :align: center

For experimental control,

(1) 'Sample' button to open controls for sample stages

.. figure:: /images/operation/epics/16IDB_LH_Sample-XPS_Short.adl.png
   :alt: 16IDB_LH_Sample-XPS_Short.adl
   :width: 400px
   :align: center

Click the green 'Full' button to open full control. This is
needed for initial setup of DAC, i.e. putting sample on
rotation axis of sample rotation stage. 

.. figure:: /images/operation/epics/16IDB_LH_Sample-XPS_Full_M.adl.png
   :alt: 16IDB_LH_Sample-XPS_Full_M.adl
   :width: 400px
   :align: center

Once the DAC alignment is finished, click the green 'short'
button to go back to the 'Sample stage (short) page. This
page hides the LH CEN X control to prevent acidental
change of the stage position.

(2) 'Pinhole' button for pinhole position optimazition if needed

.. figure:: /images/operation/epics/16IDB_LH_Pinhole_user_Short.adl.png
   :alt: 16IDB_LH_Pinhole_user_Short.adl
   :width: 400px
   :align: center

(3) 'Detectors' button for switching detectors or changing
detector position if needed.

.. figure:: /images/operation/epics/16IDB_LH_Detectors.adl.png
   :alt: 16IDB_LH_Detectors.adl
   :width: 400px
   :align: center

For laser heating system control, click the blue button laser
heating' located at the upper right cornor of the 16 IDB LH
Table Control Panel to start a page called: 16IDB Laser Heating
Control.

.. figure:: /images/operation/epics/LH_control.adl.png
   :alt: LH_control.adl
   :width: 720px
   :align: center


.. raw:: html

   <br><br>

.. hint:: Please be aware that when entering a new value into a field in an MEDM interface, the mouse cursor must hover over the field. 
          Then the Enter key on the keyboard needs to be pressed to accept the edited value. If the mouse cursor leaves the 
          field before the Enter key is pressed the edited value will revert to the original value.