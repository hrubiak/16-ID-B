from reportlab.pdfgen import canvas
from reportlab.pdfbase.acroform import AcroForm
from reportlab.lib.pagesizes import letter

DEFAULT_ENERGY = 29.2
default_note = (
    f"Default energy (keV): {DEFAULT_ENERGY:.1f}. "
    f"16-ID-B uses {DEFAULT_ENERGY:.1f} keV for 99% of its experiments, "
    "note that requesting a different energy will add some setup time "
    "for your beamline scientist."
)

DEFAULT_FOCUS = 1.5

final_pdf = "Laser_Heating_Beamtime_Form_fillable_v12.pdf"

FF_MULTILINE = 1 << 12      # 4096
FF_DONOTSCROLL = 1 << 24    # 16777216

# Acrobat choice field flags
FF_COMBO = 1 << 17     # dropdown
FF_EDIT  = 1 << 18     # allow typing

# Turn this on temporarily to see bounding boxes for every label/field
DEBUG_BOXES = False

c = canvas.Canvas(final_pdf, pagesize=letter)
form = AcroForm(c)
width, height = letter

LEFT = 72
RIGHT_WIDE = 400

# Vertical rhythm
LINE_H = 14
GAP_SMALL = 6
GAP_MED = 10
GAP_LARGE = 18


def _debug_rect(x, y, w, h):
    if not DEBUG_BOXES:
        return
    c.saveState()
    c.setLineWidth(0.5)
    c.rect(x, y, w, h, stroke=1, fill=0)
    c.restoreState()


def draw_text(x, y, text, font="Helvetica", size=11):
    c.setFont(font, size)
    c.drawString(x, y, text)
    _debug_rect(x, y - 2, min(500, len(text) * (size * 0.55)), size + 4)


def draw_field(name, x, y, w=260, h=18, border_style="underlined", font_size=11, field_flags=0, maxlen=1000):
    form.textfield(
        name=name,
        tooltip=name,
        x=x,
        y=y,
        width=w,
        height=h,
        borderStyle=border_style,
        fontSize=font_size,
        fieldFlags=field_flags,
        maxlen=maxlen,
    )
    _debug_rect(x, y, w, h)


def draw_multiline_field(name, x, y, w, h, border_style="solid", font_size=10):
    flags = (FF_MULTILINE) & (~FF_DONOTSCROLL)
    draw_field(
        name,
        x,
        y,
        w=w,
        h=h,
        border_style=border_style,
        font_size=font_size,
        field_flags=flags,
        maxlen=5000,
    )


def draw_combo_caret(x, y, w, h):
    """Visual hint so it reads like a dropdown."""
    cx = x + w - 10
    cy = y + h / 2 + 1
    c.saveState()
    c.setLineWidth(1)
    c.line(cx - 3, cy + 2, cx, cy - 2)
    c.line(cx, cy - 2, cx + 3, cy + 2)
    c.restoreState()


def draw_dropdown(name, x, y, options, w=220, h=18, font_size=10,
                  tooltip=None, editable=False, default_value=None):
    """
    options: list[str] (display strings)
    """
    flags = FF_COMBO | (FF_EDIT if editable else 0)

    if default_value is None:
        default_value = options[0] if options else ""

    form.choice(
        name=name,
        tooltip=tooltip or name,
        x=x,
        y=y,
        width=w,
        height=h,
        options=options,
        value=default_value,
        borderStyle="solid",
        fontSize=font_size,
        fieldFlags=flags,
    )
    draw_combo_caret(x, y, w, h)
    _debug_rect(x, y, w, h)


def draw_checkbox(name, x, y, label):
    form.checkbox(name=name, tooltip=label, x=x, y=y - 2, size=12, buttonStyle="check")
    c.drawString(x + 16, y, label)
    if DEBUG_BOXES:
        _debug_rect(x, y - 2, 12, 12)
        _debug_rect(x + 16, y - 2, min(300, len(label) * 6), 14)


def label_then_field(
    y,
    label,
    field_name,
    field_w=RIGHT_WIDE,
    field_h=18,
    *,
    multiline=False,
    border_style="underlined",
    font="Helvetica",
    size=11,
    field_font_size=11,
    gap_after=GAP_LARGE,
):
    draw_text(LEFT, y, label, font, size)
    y -= (LINE_H + GAP_SMALL)
    if multiline:
        draw_multiline_field(field_name, LEFT, y - field_h, field_w, field_h,
                             border_style=border_style, font_size=field_font_size)
    else:
        draw_field(field_name, LEFT, y - field_h, field_w, field_h,
                   border_style=border_style, font_size=field_font_size)
    y -= (field_h + gap_after)
    return y


def label_then_dropdown(
    y,
    label,
    field_name,
    options,
    field_w=240,
    field_h=18,
    *,
    font="Helvetica",
    size=11,
    field_font_size=10,
    gap_after=GAP_LARGE,
    editable=False,
    default_value=None,
):
    draw_text(LEFT, y, label, font, size)
    y -= (LINE_H + GAP_SMALL)
    draw_dropdown(
        field_name,
        LEFT,
        y - field_h,
        options=options,
        w=field_w,
        h=field_h,
        font_size=field_font_size,
        tooltip=label,
        editable=editable,
        default_value=default_value,
    )
    y -= (field_h + gap_after)
    return y


# Energy options (display strings only)
energy_options = [
    "17.998 keV (Zr)",
    "19.986 keV (Nb)",
    "20.000 keV (Mo)",
    "25.514 keV (Ag)",
    "27.941 keV (In)",
    "29.200 keV (Sn)",
    "30.491 keV (Sb)",
    "33.169 keV (CsI)",
    "35.985 keV (CsI)",
    "38.925 keV (La)",
    "40.443 keV (Ce)",
    "41.989 keV (Pr)",
    "50.239 keV (Gd)",
]

default_energy_str = f"{DEFAULT_ENERGY:.3f}"
default_choice = next(
    (s for s in energy_options if s.startswith(default_energy_str)),
    energy_options[0],
)

# -------------------------
# PAGE 1
# -------------------------
y = height - 72
draw_text(LEFT, y, "Laser Heating Beamtime Pre-Experiment Questionnaire", "Helvetica-Bold", 18)
y -= 50

draw_text(LEFT, y, "General", "Helvetica-Bold", 13)
y -= 30

y = label_then_field(y, "1. Beamtime Dates", "beamtime_dates",
                     field_w=RIGHT_WIDE, field_h=18)

draw_text(LEFT, y, "2. Radiological Beamtime?")
y -= (LINE_H + GAP_SMALL)
draw_checkbox("rad_no", LEFT, y, "No")
draw_checkbox("rad_yes", LEFT + 68, y, "Yes")
draw_checkbox("rad_part", LEFT + 148, y, "Partially")
y -= (18 + GAP_LARGE)

draw_text(LEFT, y, "3. What technique(s) are we trying to use?")
y -= (LINE_H + GAP_SMALL)
draw_checkbox("tech_std", LEFT, y, "Standard DAC (no LH)")
draw_checkbox("tech_lhdac", LEFT + 188, y, "Laser-heated DAC")
y -= (LINE_H + GAP_SMALL)
draw_checkbox("tech_memb", LEFT, y, "Membrane-driven compression")
y -= (LINE_H + GAP_SMALL)
draw_checkbox("tech_ddac", LEFT, y, "Dynamic DAC (dDAC / time-resolved)")
y -= (LINE_H + GAP_SMALL)
draw_checkbox("tech_res", LEFT, y, "Resistively heated")
draw_checkbox("tech_sc", LEFT + 188, y, "Single-crystal / Multi-grain DAC")
y -= (LINE_H + GAP_MED)
draw_checkbox("tech_tor", LEFT, y, "Toroidal DAC")
y -= (LINE_H + GAP_MED)

y = label_then_field(y, "Other (please specify):", "tech_other",
                     field_w=RIGHT_WIDE, field_h=18)

draw_text(LEFT, y, "4. What DAC types will you be bringing?")
y -= (LINE_H + GAP_SMALL)
draw_checkbox("dac_std", LEFT, y, "Standard symmetric DAC (Princeton type)")
y -= (LINE_H + GAP_SMALL)
draw_checkbox("dac_bx90", LEFT, y, "BX-90")
draw_checkbox("dac_mem", LEFT + 188, y, "Membrane-driven DAC")
y -= (LINE_H + GAP_SMALL)
draw_checkbox("dac_ddac", LEFT, y, "Dynamic DAC (dDAC)")
draw_checkbox("dac_vac", LEFT + 188, y, "DAC in vacuum jacket")
y -= (LINE_H + GAP_SMALL)
draw_checkbox("dac_custom", LEFT, y, "Custom / in-house DAC")
draw_checkbox("dac_holder", LEFT + 188, y, "Need a custom holder for DAC?")
y -= (LINE_H + GAP_MED)

y = label_then_field(y, "Other (please specify):", "dac_other",
                     field_w=RIGHT_WIDE, field_h=18, gap_after=0)

# -------------------------
# PAGE 2
# -------------------------
c.showPage()
form = AcroForm(c)

y = height - 72
draw_text(LEFT, y, "Beam Specs", "Helvetica-Bold", 13)
y -= 40

y = label_then_field(y, "5. Sample chamber sizes (µm) (please list)",
                     "sample_chamber", field_w=RIGHT_WIDE, field_h=18)

y = label_then_field(y, "6. Required X-ray focus, FWHM (µm × µm)",
                     "xray_focus", field_w=RIGHT_WIDE, field_h=18, gap_after=GAP_MED)

draw_text(LEFT, y, f"Typical focus (µm × µm): {DEFAULT_FOCUS}×{DEFAULT_FOCUS}", "Helvetica-Oblique", 9)
y -= (LINE_H - 2)

y -= (GAP_LARGE)

# Q7 dropdown
y = label_then_dropdown(
    y,
    "7. Preferred X-ray energy (keV)",
    "pref_energy",
    energy_options,
    field_w=260,
    field_h=18,
    field_font_size=10,
    gap_after=GAP_MED,
    editable=False,
    default_value=default_choice,
)

# Draw as two lines so it doesn't run off the page
draw_text(LEFT, y, default_note[:90], "Helvetica-Oblique", 9)
y -= LINE_H
draw_text(LEFT, y, default_note[90:], "Helvetica-Oblique", 9)
y -= GAP_LARGE

draw_text(LEFT, y, "8. Do you anticipate needing to defocus or change beam size during experiment?")
y -= (LINE_H + GAP_SMALL)
draw_checkbox("def_no", LEFT, y, "No")
draw_checkbox("def_yes", LEFT + 68, y, "Yes")
y -= (18 + GAP_MED)

y = label_then_field(y, "If yes, please describe:", "def_desc",
                     field_w=RIGHT_WIDE, field_h=68,
                     multiline=True, border_style="solid")

draw_text(LEFT, y, "Mirrors", "Helvetica-Bold", 13)
y -= 30

draw_text(LEFT, y, "9. Which mirror will be used? (default: LKB)")
y -= (LINE_H + GAP_SMALL)
draw_checkbox("mirror_skb", LEFT, y, "SKB")
draw_checkbox("mirror_lkb", LEFT + 68, y, "LKB")
y -= (18 + GAP_LARGE)

draw_text(LEFT, y, "10. Isolation mode? (Only for radiological beamtime)")
y -= (LINE_H + GAP_SMALL)
draw_checkbox("iso_no", LEFT, y, "No")
draw_checkbox("iso_yes", LEFT + 68, y, "Yes")
y -= (18 + GAP_MED)

y = label_then_field(
    y,
    "Expected energy, mirror, or isolation mode changes during beamtime:",
    "mirror_changes",
    field_w=RIGHT_WIDE,
    field_h=40,
    multiline=True,
    border_style="solid",
    gap_after=0,
)

# -------------------------
# PAGE 3
# -------------------------
c.showPage()
form = AcroForm(c)

y = height - 72
draw_text(LEFT, y, "Beamtime Daily Plan", "Helvetica-Bold", 13)
y -= 35

daily_fields = ["day1", "day2", "day3", "day4", "day5plus"]
daily_labels = ["Day 1:", "Day 2:", "Day 3:", "Day 4:", "Day 5+:"]

for name, label in zip(daily_fields, daily_labels):
    y = label_then_field(
        y,
        label,
        name,
        field_w=RIGHT_WIDE,
        field_h=88,
        multiline=True,
        border_style="solid",
    )

# -------------------------
# PAGE 4
# -------------------------
c.showPage()
form = AcroForm(c)

y = height - 72
draw_text(LEFT, y, "Capabilities", "Helvetica-Bold", 13)
y -= 40

draw_text(LEFT, y, "11. Online ruby system?")
y -= (LINE_H + GAP_SMALL)
draw_checkbox("ruby_no", LEFT, y, "No")
draw_checkbox("ruby_yes", LEFT + 68, y, "Yes")
y -= (18 + GAP_LARGE)

draw_text(LEFT, y, "12. Other high temperature method(s)")
y -= (LINE_H + GAP_SMALL)
draw_checkbox("ht_res", LEFT, y, "Resistive heating")
y -= (18 + GAP_MED)

y = label_then_field(y, "Please describe:", "ht_desc",
                     field_w=RIGHT_WIDE, field_h=18)

draw_text(LEFT, y, "13. Do you need any of the following?")
y -= (LINE_H + GAP_SMALL)
draw_checkbox("need_vac", LEFT, y, "Vacuum pump")
draw_checkbox("need_chill", LEFT + 188, y, "Chiller")
y -= (LINE_H + GAP_SMALL)
draw_checkbox("need_tc", LEFT, y, "Thermocouple interface")
y -= (18 + GAP_MED)

y = label_then_field(y, "Other (please specify):", "need_other",
                     field_w=RIGHT_WIDE, field_h=18)

draw_text(LEFT, y, "14. How do you want to heat?")
y -= (LINE_H + GAP_SMALL)
draw_checkbox("heat_sq", LEFT, y, "Square modulated")
draw_checkbox("heat_cont", LEFT + 188, y, "Continuous")
y -= (18 + GAP_MED)

y = label_then_field(
    y,
    "Please describe:",
    "trigger_scheme",
    field_w=RIGHT_WIDE,
    field_h=68,
    multiline=True,
    border_style="solid",
    gap_after=0,
)

c.save()
print(final_pdf)