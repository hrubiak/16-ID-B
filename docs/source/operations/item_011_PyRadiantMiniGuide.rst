Using PyRadiant to measure temperature
======================================

PyRadiant is a graphical application for measuring temperature by fitting black-body radiation curves to spectroscopic data collected during laser heating in a DAC experiment.

PyRadiant is typically preconfigured by beamline staff—users only need to follow a few simple steps to begin viewing temperatures in real time.

1. **Launch PyRadiant** from the desktop or application menu.

2. **Click "Load"** (top-left) to open the most recent ``.spe`` file from the experiment folder.

   .. figure:: /images/software/pyradiant/main_screen.png
      :width: 90%
      :align: center
      :alt: Main interface

      Main PyRadiant interface with file controls at the top left.

3. In the right-side **Settings panel**, choose the preloaded configuration under *Settings save and restore* (e.g., ``2025xxxx-PIMAX4``).

4. Click **"Load"** under the settings panel to apply the configuration (ROIs, wavelength range, calibration).

   .. figure:: /images/software/pyradiant/side_panel.png
      :width: 90%
      :align: center
      :alt: Settings and configuration panel

      Use the right panel to load configuration settings and apply them to the current file.

5. The **Temperature tab** will automatically show the Planck fit for both **Upstream** and **Downstream** spectra.

   .. figure:: /images/software/pyradiant/main_screen.png
      :width: 90%
      :align: center
      :alt: Temperature fit view

      Fitted spectra with temperature results displayed at the top.

6. If multiple frames are present, **navigate with the ←/→ buttons** or use the **T Log** button to view the temperature history graph.

7. To view raw spectra, switch to the **Spectrum tab** and choose **1D**, **2D**, or **RAW** view modes as needed.

   .. figure:: /images/software/pyradiant/spectra_2d_roi.png
      :width: 90%
      :align: center
      :alt: 2D spectrum with ROI boxes

      2D Spectrum view with ROIs for upstream, downstream, and background.

8. **Check the Auto box** (top bar) to enable automatic updates as new ``.spe`` files are written.

9. Optionally, click **Save Data** or **Save Graph** in the Output panel to export results.

.. note::
   Beamline configurations are typically handled in advance. Only change settings or calibrations if instructed by staff.