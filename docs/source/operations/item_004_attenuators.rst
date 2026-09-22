.. _attenuators:

Setting X-ray attenuation
-------------------------

.. note:: **Returning users, please read.** After the APS-U upgrade the
   beam at 16-ID-B is roughly **two orders of magnitude brighter** at our
   typical energies, and the current detector is also more sensitive. Net
   throughput is up by about **100x** compared to pre-upgrade conditions.
   In practice this means:

   * Exposure times must be drastically shorter than what you used before.
   * Grainy, multigrain, and single-crystal samples **require the use of
     attenuators** to avoid damaging the detector.

   Old habits from pre-APS-U operation are the fastest way to saturate
   pixels or damage the Pilatus. Recalibrate your defaults.

The 16-ID-B attenuator is a stack of **five** absorber foils in series,
placed upstream of the sample. Each foil can be inserted (``In``) or
retracted (``Out``) independently. The foils are numbered **1–5** and are
arranged **most absorbing (#1) to least absorbing (#5)**, so inserting a
lower-numbered foil removes more flux than inserting a higher-numbered one.
The total transmission at the sample is the product of the transmissions
of all inserted foils at the current beam energy.

Attenuators must be set correctly for **two** distinct reasons. Both
matter, and either one on its own is enough to require attenuation:

1. **Detector protection.** Excess flux on the Pilatus 1M-F can damage the
   detector.
2. **Data validity.** Even below the damage threshold, pixels that
   *saturate* record a truncated intensity. The diffraction pattern is
   then no longer quantitative, and downstream data analysis may be
   invalid.

The flux at the detector is monitored on the **Pilatus saturation** MEDM
screen. Open it from the main **16IDB LH Table Control Panel** →
**Monitors** → **pilatus saturation**. Keep this screen open whenever you
change attenuation.

.. warning:: Removing attenuation while the shutter is open can instantly
   damage the Pilatus, saturate the pattern, or over-dose the sample.
   Always reduce attenuation **one foil at a time**, starting with the
   least-absorbing inserted foil, and re-check the Pilatus saturation
   readout before removing more.

Opening the Attenuators screen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From the **16IDB LH Table Control Panel** (see
:ref:`Start EPICS/MEDM user interface <beamline_operation>`), click the
**Attenuators** button in the row of colored buttons.

.. TODO: replace this note with a figure once an attenuators_screen.png
   is available in docs/source/images/operation/epics/.

Screen reference
^^^^^^^^^^^^^^^^

The Attenuators screen exposes one **In / Out** control per foil for
foils **1 through 5**, plus a status read-back for each.

.. csv-table::
   :header: "Field", "Meaning"
   :widths: 25, 100

   "Foils 1–5, In / Out", "Per-foil actuator. Foil **1** is the most absorbing, foil **5** is the least. Insert lower numbers first to attenuate; retract higher numbers first to open up."
   "Foil status", "Read-back showing the actual position of each foil (may lag the request by ~1 s while the pneumatic paddle moves). Trust the read-back, not the request, when deciding whether it is safe to change flux."

.. TODO: fill in the material and thickness of each of the five 16-ID-B
   foils (e.g. "#1 = 500 µm Cu, #2 = 250 µm Cu, ...") once confirmed by
   beamline staff.

Recommended procedure: increasing attenuation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Insert more attenuation **before** doing anything that could over-illuminate
the detector or the sample (opening the shutter after a long dark period,
switching to a much stronger sample, moving off a heavily attenuated
alignment position, etc.).

1. On the **Pilatus saturation** screen (Monitors → pilatus saturation),
   note the current saturation reading.
2. On the **Attenuators** screen, click **In** on the lowest-numbered
   foil that is currently ``Out`` (foil **1** is the most absorbing).
3. Wait ~1 s and confirm the foil-status read-back shows ``In``.
4. Re-check the Pilatus saturation reading. If it is still too high,
   insert the next foil (foil **2**, then **3**, …) until the saturation
   drops to a safe, unsaturated level.

Recommended procedure: decreasing attenuation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Work with the **Pilatus saturation** screen open, and step one foil at a time.

1. Retract the **highest-numbered inserted foil** (the least absorbing one
   in the beam).
2. Take a short exposure and check Pilatus saturation. If any pixel is at
   or near saturation, put the foil back in.
3. If there is still headroom and you need more flux, repeat with the
   next-highest-numbered inserted foil.

Common use cases
^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "Situation", "Suggested starting point"
   :widths: 40, 60

   "Aligning a new sample in a DAC", "Insert all five foils. The dominant risk during alignment is that a diamond anvil (a large single crystal) accidentally satisfies the Bragg condition and produces a very bright diffraction spot on the Pilatus, which can damage the detector. Retract from #5 down while watching Pilatus saturation."
   "SXD data collection (single crystal)", "Insert **all five foils** when testing the first full rotation or wide scan. Check every frame for saturation before reducing attenuation for the production run."
   "Ruby fluorescence measurement", "Heavy attenuation. Leave foils #1–#3 in at minimum. The ruby signal does not need full flux and the sample should not receive full flux during a pressure check."
   "Routine XRD on a well-characterised sample", "Return to the foil pattern that gave a good pattern last time; adjust based on peak-to-background."
   "Long dwell / weak scatterer", "Retract as many foils as the Pilatus saturation reading allows while staying comfortably below saturation."

.. TODO: replace the qualitative guidance above with beamline-scientist
   recommended foil combinations for typical 16-ID-B experiments and
   sample energies.
