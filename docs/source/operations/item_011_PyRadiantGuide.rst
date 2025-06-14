.. _pyradiant-docs:

PyRadiant Documentation
=======================

Introduction
------------

PyRadiant is a Python-based graphical user interface (GUI) application designed for fast, visual analysis of thermal emission spectra collected during laser-heated diamond anvil cell (DAC) experiments. It provides real-time feedback by fitting black-body radiation models to the data, allowing users to estimate sample temperature during high-pressure experiments.

Originally based on code forked from `T-Rax <https://github.com/CPrescher/T-Rax>`_, PyRadiant combines this with functionality ported from the legacy LabVIEW program **T-View**, and includes numerous new features for usability and beamline integration.

The application supports Princeton Instruments ``.spe`` files collected using WinSpec (File Version 2) or LightField (File Version 3).

PyRadiant can optionally connect to EPICS to read detector data directly and publish fitted temperature values to process variables (PVs), enabling display on beamline control screens or archival as experimental metadata.

Maintainer:
    Ross Hrubiak (hrubiak@anl.gov)  
    High Pressure Collaborative Access Team, Argonne National Laboratory

.. note::
   At the beamline, PyRadiant is typically preconfigured by the staff. Users primarily interact with the GUI to view real-time fitted temperature values or explore previously recorded files.

.. figure:: /images/software/pyradiant/main_screen.png 
   :width: 90%
   :align: center
   :alt: Main temperature fitting view in PyRadiant

   The main PyRadiant interface showing Planck fits for upstream and downstream spectra. Fitted temperatures and maximum intensities are displayed, along with file information and metadata at the bottom.

Program Architecture
--------------------

PyRadiant is organized into the following functional sections:

- **File Control Bar**: For opening and sorting ``.spe`` files, switching frames, toggling full-screen display, and accessing logs.
- **Main Display Tabs**:
  
  - **Temperature Tab**: Shows Planck curve fits, calculated temperatures, and optionally a temperature history plot.
  - **Spectrum Tab**: Offers multiple views of the raw and processed CCD data.
  
- **Right-Side Panel**:
  - Contains controls for configuration, wavelength and ROI selection, background subtraction, calibration, and EPICS integration.
- **Output Panel**:
  - Provides export options for fitted spectra, plots, and tabulated data.

.. figure:: /images/software/pyradiant/side_panel.png
   :width: 90%
   :align: center
   :alt: PyRadiant configuration panel with ROI and wavelength settings

   The right-side configuration panel in PyRadiant, showing options to load/save settings, define wavelength range, and select ROIs for upstream, downstream, and background. These settings control how the temperature fit is applied to the spectral data.

File Handling and Navigation
----------------------------

To load and navigate temperature data:

1. **Open a ``.spe`` file** using the file control bar at the top left.
2. **Apply a configuration** by loading a ``.trs`` file via the Settings panel. These files store wavelength ranges, ROI settings, and calibration.
3. **Navigate frames** using the left/right arrow buttons. If the file contains multiple frames, a temperature vs. frame plot appears below the main fit.
4. **Switch between files** using the file list on the left. Sorting can be toggled between alphabetical ("A–Z") and modification time ("watch icon").
5. **Enable Auto Mode** to automatically process new files as they appear.

Main Display Tabs
-----------------

**Temperature Tab**
~~~~~~~~~~~~~~~~~~~
Displays the fitted black-body spectra using either the Planck or Wien model. Two regions are fit independently (Upstream and Downstream), and the temperatures are displayed above the plots.

If multiple frames exist, the **T-history plot** appears beneath the fit panel.

**Spectrum Tab**
~~~~~~~~~~~~~~~~
Includes three viewing modes:

- **1D**: Shows the extracted spectrum for each ROI.
- **2D**: Displays a full CCD image with ROIs and background overlaid.
- **RAW**: For kinetics-mode data. Shows raw stacked CCD frames without processing, useful for diagnostics.

.. figure:: /images/software/pyradiant/spectra_1d.png
   :width: 90%
   :align: center
   :alt: 1D spectra view in Spectrum tab

   The 1D view in the Spectrum tab displays the extracted spectral intensity for both the upstream and downstream ROIs. This view is useful for inspecting the raw uncorrected signal before temperature fitting.

.. figure:: /images/software/pyradiant/spectra_2d_roi.png
   :width: 90%
   :align: center
   :alt: 2D spectra view with ROI overlays

   The 2D view in the Spectrum tab shows the full CCD image with ROI overlays for upstream, downstream, and background regions. This allows visual placement and fine-tuning of the regions used for signal extraction and background subtraction.

.. figure:: /images/software/pyradiant/kinetics_1_frame.png
   :width: 90%
   :align: center
   :alt: PyRadiant 2D view of a single frame in kinetics mode

   In kinetics mode, the 2D view shows a single time frame from a stacked CCD readout. ROIs for upstream, downstream, and background are overlaid to define which rows are extracted for each channel and how background subtraction is applied.

.. figure:: /images/software/pyradiant/kinetics_raw_ccd.png
   :width: 90%
   :align: center
   :alt: PyRadiant RAW CCD view of stacked frames

   The RAW view in kinetics mode shows the full CCD readout with multiple time frames stacked vertically. This mode is primarily for diagnostic use, helping identify saturation, shifts, or timing issues in time-resolved acquisitions.



Configuration Panel
-------------------

**Multiple Configurations**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This allows you to manage multiple setups during a single session—for example, different spectrometer or CCD hardware setups.

- Click the **"+"** button to create a new empty configuration.
- Each configuration stores an independent full set of settings:
  - ROIs, calibration files, wavelength ranges, fitting models, EPICS integration, etc.
- Switch between configurations by clicking on the **numbered buttons**.

**Loading and Saving**
~~~~~~~~~~~~~~~~~~~~~~
- Use **Save** to store all settings to an HDF5 ``.trs`` file.
- Use **Load** to restore settings from a saved ``.trs``.

.. warning::
   PyRadiant ``.trs`` files are not compatible with legacy T-Rax ``.trs`` files.

.. figure:: /images/software/pyradiant/config_selector.png
   :width: 40%
   :align: center
   :alt: Configuration management in PyRadiant

   Configuration management controls in PyRadiant. Users can add, delete, and switch between multiple configurations, each retaining its own ROI, wavelength range, calibration, and EPICS settings. Settings can be saved and restored using the dropdown and Load/Save buttons.


**ROI Selection and Wavelength Range**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Define the **fitting range**, typically 600–800 nm.
- Move and resize ROI boxes in the Spectrum 2D tab for **Upstream**, **Downstream**, and optional **Background**.
- ROIs can be adjusted interactively by dragging the boxes in the 2D CCD view or by entering precise start and end values directly into the control panel.
- Check the box to enable **background subtraction** using in-situ dark regions.

.. note::
   In-situ sampled background refers to regions of the CCD where no signal from the sample is expected—these dark regions are used to estimate and subtract the background noise directly from each spectrum.
   Enable background subtraction **only if the spectra were recorded without prior background correction**. If the background was already subtracted during acquisition (e.g., by the control software), this step is not needed.

.. figure:: /images/software/pyradiant/roi_settings.png
   :width: 40%
   :align: center
   :alt: ROI and background selection in PyRadiant

   ROI configuration section where users define the row ranges for upstream and downstream signal extraction, along with corresponding background regions. Options at the bottom enable subtraction of in-situ background from both data and calibration spectra.

**Intensity Calibration**
~~~~~~~~~~~~~~~~~~~~~~~~~
- Select a calibration ``.spe`` file recorded from a temperature calibrant (e.g., tungsten lamp).
- Choose calibration method:
  - **Temperature**: Enter the known calibrant temperature (in Kelvin).
  - **Standard**: Select a previously measured ideal spectrum file (two-column format).
- Optionally, average across frames using Start Frame and End Frame inputs.
- Click **Save Standard** to export the current file as a two-column calibration reference.

.. figure:: /images/software/pyradiant/intensity_calibration.png
   :width: 40%
   :align: center
   :alt: Intensity calibration panel in PyRadiant

   Intensity calibration panel for upstream and downstream channels. Users can load a calibration spectrum from a temperature standard, either by specifying the known temperature in Kelvin or selecting a pre-measured ideal spectrum file. The calibration can optionally average across multiple frames. The “Save Standard” button allows saving the corrected spectrum as a reusable reference file.


**Fitting Model**
~~~~~~~~~~~~~~~~~
- Choose between:
  - **Planck** (default and recommended)
  - **Wien** (faster, approximate)
  
.. figure:: /images/software/pyradiant/fit_function_selector.png
   :width: 40%
   :align: center
   :alt: Temperature fit function selection in PyRadiant

   Selection panel for the temperature fitting model. Users can choose between the full Planck equation (recommended for accuracy) or the Wien approximation (faster, but less accurate at low temperatures).

**EPICS Integration**
~~~~~~~~~~~~~~~~~~~~~
- **EPICS PVs** can be specified to:
  - Update the monitored folder path (via EPICS control)
  - Publish fitted temperature results to control screen PVs
- Enable **Connect to AD** to read data directly from EPICS Area Detector (bypasses file system).
  - AD may also be configured to control LightField and hardware acquisition.

.. figure:: /images/software/pyradiant/epics_controls.png
   :width: 50%
   :align: center
   :alt: EPICS integration controls in PyRadiant

   EPICS integration panel. Users can configure and enable connection to EPICS process variables using the “Setup EPICS” dialog. The “Connect to EPICS” option allows real-time updates from control systems, while “Connect to AD” enables PyRadiant to directly access image data from an EPICS Area Detector plugin.

Output Panel
------------

- Export ASCII tables of temperature and spectra.
- Save corrected spectra and fit parameters.
- Save current fit plot as an image.

Use Case: Viewing and Navigating Data
-------------------------------------

The most common use case, especially at the beamline:

1. **Load ``.spe`` File** from the file panel.
2. **Load ``.trs`` Settings**.
3. **View Fit** in Temperature tab. Temperatures for Upstream and Downstream will be displayed.
4. **Navigate Frames** using arrow buttons.
5. **Browse Files** using the side panel. Sort by name or time. Enable "Auto" to process new files as they appear.
6. **Optional**: Use the T Log window to view long-term temperature history.


Use Case: Creating a New Setup from Scratch
-------------------------------------------

This workflow is for users setting up PyRadiant manually, e.g. at home:

1. **Load Calibration File**: Open a ``.spe`` file recorded from a calibrated light source.
2. **Set Wavelength Range**: Specify a fit range, e.g., 600–800 nm.
3. **Define ROIs**: Use Spectrum 2D tab to adjust upstream/downstream ROI boxes and optional background.
4. **Enable Background Subtraction** (optional)
5. **Apply Calibration**:
   
   - Reload calibration file in Intensity Calibration section.
   - Choose **Temperature** or **Standard** method.
   - Enter known temperature or select standard file.
  
6. **Verify Fit**: Switch to the Temperature tab. Compare fitted temperature to input, or compare spectrum to ideal.
7. **Save Configuration**: Save to a ``.trs`` file for later reuse.


Troubleshooting
---------------

- **No temperature displayed?**
  
  - Ensure that the ROIs are correctly placed on spectral regions with signal.
  - Check that the wavelength fit range includes the region with usable data.
  - Confirm that an intensity calibration has been applied.

- **Fit looks wrong or values are off?**
  
  - Check if the **signal is saturated**—saturation can distort the spectrum shape and lead to inaccurate fits.
  - Re-check that the loaded **calibration** corresponds to the correct detector.
  - Use the **“Temperature” method** for calibration and verify the specified value matches the calibrant.
  - Ensure that the **ROI** covers the correct spectral region.
  - Verify that the **wavelength range** is within the calibrated range (e.g., 600–800 nm).
  - Confirm that the **intensity calibration** was properly applied and matches the acquisition conditions.

- **EPICS not updating or communicating?**
  
  - Make sure the correct EPICS PVs have been entered in the settings.
  - Verify that EPICS IOC and Channel Access are properly configured on the network.
  - Confirm that “Connect to EPICS” or “Connect to AD” are enabled in PyRadiant.

.. tip::
   If unexpected behavior occurs, try reloading the ``.spe`` file and re-applying the ``.trs`` configuration.

   