.. _pace6000_membrane_pressure:

Increasing DAC membrane pressure with the PACE6000 controller
-------------------------------------------------------------

The GE Druck **PACE6000** is a two-channel pneumatic pressure controller used at
16-ID-B to drive the gas membranes that pressurize diamond anvil cells (DACs).
Each channel has an independent setpoint, slew rate, and vent control.

.. warning:: Membrane over-pressurization can damage the DAC, the diamonds, or
   the sample. Always know the safe working pressure for the specific cell and
   membrane you are using, and increase pressure in small, controlled steps.

.. danger:: **Safety goggles are mandatory** for anyone entering the hutch or
   working near the membrane gas lines whenever the pressure in either channel
   exceeds **100 PSI**. A ruptured line or fitting at high pressure can eject
   debris or gas at eye-injuring velocities. Check the ``Pressure`` readouts
   on both channels before opening the hutch; if either channel is above
   100 PSI, put on goggles before entering.

.. important:: **Always leave the pressure unit set to PSI before changing any
   setpoint or slew rate.** This is a HPCAT convention: keeping every user on
   the same unit prevents someone from accidentally entering a value that is
   correct in bar or kPa but dangerously wrong when interpreted as PSI. Verify
   the unit selector reads ``PSI`` on both channels every time you open the
   panel, and switch it back to ``PSI`` before you leave.

Opening the PACE6000 screen
^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. From the **16IDB LH Table Control Panel** (shown below), click the green
   **PACE7** button.

   .. figure:: /images/operation/epics/16IDB_dacxrd_LH_PACE7_annotated.png
      :alt: 16IDB LH Table Control Panel with the green PACE7 button highlighted
      :width: 540px
      :align: center

      The green **PACE7** button (highlighted in red) opens the PACE6000
      controller drop-down menu.

2. In the drop-down menu, select **PACE_7**.
3. The ``PACE6000.adl`` window opens:

.. figure:: /images/operation/epics/pace7_screen.png
   :alt: PACE6000 pressure controller MEDM screen (PACE_7:PC7)
   :width: 540px
   :align: center

Screen reference
^^^^^^^^^^^^^^^^

The window shows two identical channel columns (left and right), each
controlling one output of the PACE_7:PC7 controller. Inside the hutch the
membrane gas lines are color-coded with tape:

* **Left column** on the screen ↔ **red-tape** membrane line in the hutch
* **Right column** on the screen ↔ **blue-tape** membrane line in the hutch

Trace the tape at the DAC end to confirm which channel drives your cell
before changing any setpoint.

.. csv-table::
   :header: "Field", "Meaning"
   :widths: 25, 100

   "Pressure", "Live pressure readout. The unit selector to the right (``PSI``) sets the display unit."
   "Setpoint", "Target pressure. Type a value and press **Enter** (see MEDM hint below), or use the ``<`` / ``>`` tweak buttons."
   "Tweak", "Step size used by the ``<`` / ``>`` buttons next to the setpoint (in the currently selected unit)."
   "Control", "Master enable for the channel. **Off** = the controller holds output; **On** = the controller actively drives toward the setpoint."
   "Slew Mode", "``LIN`` = ramp toward the setpoint at the configured slew rate; ``MAX`` = go as fast as the controller can (do **not** use for DAC membranes)."
   "Slew", "Slew rate in *unit/second* (matches the selected pressure unit)."
   "Effort", "Fraction of the controller's actuation range currently in use. Non-zero effort with a stagnant Pressure reading indicates a leak or a closed valve."
   "Vent", "``Stop vent`` = the vent valve is closed. Switching to the vent option opens the vent, dumping the channel pressure to atmosphere. ``Vent OK`` next to the field indicates the vent is functioning."
   "Error", "Controller error code. ``0, No err`` is the healthy state."
   "Read Rate", "Polling rate for the readbacks."
   "More", "Opens the extended PACE6000 panel with additional diagnostics."

.. hint:: When entering a new value into any MEDM field, keep the mouse cursor
   over the field and press **Enter** to accept. If the cursor leaves the field
   before Enter is pressed the value reverts.

Increasing pressure — recommended procedure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Identify the channel plumbed to your DAC membrane by following the
color-coded tape inside the hutch:

* **Red-tape** line → **left column** on the PACE7 screen
* **Blue-tape** line → **right column** on the PACE7 screen

The steps below refer to *that* channel only.

1. **Pre-flight checks**

   * The membrane gas line is connected to the DAC and finger-tight.
   * **Pressure unit is set to** ``PSI`` **on both channels** (HPCAT
     convention — see the note above). If it is not, change it *before*
     doing anything else.
   * ``Error`` reads ``0, No err``.
   * ``Vent`` is set to ``Stop vent`` (i.e. the vent is closed).
   * The current ``Pressure`` reading is sensible (near zero if the
     membrane is unpressurized).

2. **Set a safe slew rate**

   * Set **Slew Mode** to ``LIN``.
   * Enter a conservative **Slew** rate — for most cells 1–5 PSI/s is a
     reasonable starting point. Slower rates give you more time to react
     if something behaves unexpectedly.

3. **Enter a target pressure**

   * Type the new **Setpoint** and press **Enter**, or use the ``<`` /
     ``>`` tweak buttons after setting an appropriate ``Tweak`` step size.
   * Increase pressure in **small increments** (a few PSI at a time near
     phase transitions or near the cell's working limit) rather than
     jumping directly to the final value.

4. **Enable the output**

   * Switch **Control** from ``Off`` to ``On``.
   * The ``Pressure`` readout should begin approaching the setpoint at
     approximately the configured slew rate. ``Effort`` will rise while
     the controller drives the membrane.

5. **Monitor the ramp**

   * Watch the sample in the online microscope (Ruby system) / on the diffraction pattern.
   * If ``Pressure`` fails to track the setpoint but ``Effort`` stays
     high, suspect a leak or a blocked line — stop and investigate before
     increasing further.
   * If the sample or gasket behavior is not what you expect (e.g. sudden
     jump, gasket blowout), switch **Control** to ``Off`` immediately.

6. **Hold at pressure**

   * Once at the target, leave **Control** ``On`` so the controller
     maintains the setpoint against small leaks. ``Effort`` will settle
     to a small non-zero value.

Decreasing pressure
^^^^^^^^^^^^^^^^^^^

To lower pressure in a controlled way, reduce the **Setpoint** with the
controller still ``On`` — the PACE will slowly bleed gas at the configured
slew rate.

To release pressure quickly, switch **Vent** from ``Stop vent`` to the vent
option; the ``Vent OK`` indicator confirms the vent valve responded.
Return **Vent** to ``Stop vent`` when the release is complete.

.. warning:: Venting is fast. Do not vent under load unless you intend to
   fully depressurize the membrane.

Shutting down
^^^^^^^^^^^^^

1. Reduce **Setpoint** to zero (or the desired standby pressure).
2. When ``Pressure`` has settled, switch **Control** to ``Off``.
3. Leave **Vent** in ``Stop vent`` unless the membrane should be
   depressurized for the next user.

Troubleshooting
^^^^^^^^^^^^^^^

**All controls and indicators appear white / blank on the MEDM screen**

This almost always means the IOC that serves the PACE7 process variables
is not running. Start it as follows:

1. In **MobaXterm**, open the **Sessions** panel and double-click the
   ``veneno`` session. Log in with the account provided by the beamline
   scientist / local staff.
2. At the prompt, run:

   .. code-block:: bash

      source .bashrc

3. Check the IOC status:

   .. code-block:: bash

      iocPACE_7 status

4. If the status is **not running**, start it:

   .. code-block:: bash

      iocPACE_7 start

Return to the MEDM screen; the readouts and controls should populate
within a few seconds. If they do not, contact a beamline scientist.
