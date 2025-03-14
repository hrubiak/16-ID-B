X-ray detector control (Pilatus 2M CdTe)
----------------------------------------


1. Click the "Area Detector " button on "16IDB LH Table Control
Panel" (on the row of colored buttons, it's the first one on the
left)

.. figure:: /images/operation/epics/16IDB_dacxrd_LH.png
   :alt: 16IDB_dacxrd_LH.adl
   :width: 540px
   :align: center

On the "Area Detector" pull-down menu, one can select Pilatus 2M - full or Pilatus 2M - short

.. figure:: /images/operation/epics/Area_detector_menu.png
   :alt: Area_detector_menu
   :width: 120px
   :align: center

In most cases, Pilatus 2M - short control is sufficient.

.. figure:: /images/operation/epics/16IDB_PilatusShort.adl.png
   :alt: 16IDB_PilatusShort.adl
   :width: 720px
   :align: center

If you need to use external trigger, or other advanced features, Pilatus 2M - full control has to be
used.

.. figure:: /images/operation/epics/pilatusDetector.adl.png
   :alt: pilatusDetector.adl
   :width: 720px
   :align: center