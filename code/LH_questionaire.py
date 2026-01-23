from reportlab.pdfgen import canvas 
from reportlab.pdfbase.acroform import AcroForm
from reportlab.lib.pagesizes import letter
from pypdf import PdfReader, PdfWriter 
from pypdf.generic import NameObject  

base_pdf = "Laser_Heating_Beamtime_Form_fillable_v11_base.pdf"
final_pdf = "Laser_Heating_Beamtime_Form_fillable_v11_autolock_previewfriendly.pdf"

c = canvas.Canvas(base_pdf, pagesize=letter)
form = AcroForm(c)
width, height = letter

def draw_text(x, y, text, font="Helvetica", size=11):
    c.setFont(font, size)
    c.drawString(x, y, text)

def draw_field(name, x, y, w=260, h=18, border_style="underlined"):
    form.textfield(name=name, tooltip=name, x=x, y=y, width=w, height=h, borderStyle=border_style)

def draw_checkbox(name, x, y, label):
    form.checkbox(name=name, tooltip=label, x=x, y=y-2, size=12, buttonStyle="check")
    c.drawString(x+16, y, label)

# hidden flag
form.textfield(name="lock_flag", tooltip="lock_flag", x=2, y=2, width=1, height=1, borderWidth=0)

# PAGE 1
y = height - 72
draw_text(72, y, "Laser Heating Beamtime Pre-Experiment Questionnaire", "Helvetica-Bold", 18)
y -= 50
draw_text(72, y, "General", "Helvetica-Bold", 13)
y -= 30

draw_text(72, y, "1. Beamtime Dates")
y -= 20
draw_field("beamtime_dates", 72, y, 400)
y -= 40

draw_text(72, y, "2. Radiological Beamtime?")
y -= 20
draw_checkbox("rad_no", 72, y, "No")
draw_checkbox("rad_yes", 140, y, "Yes")
draw_checkbox("rad_part", 220, y, "Partially")
y -= 40

draw_text(72, y, "3. What technique(s) are we trying to use?")
y -= 25
draw_checkbox("tech_std", 72, y, "Standard DAC (no LH)")
draw_checkbox("tech_lhdac", 260, y, "Laser-heated DAC")
y -= 20
draw_checkbox("tech_memb", 72, y, "Membrane-driven compression")
y -= 20
draw_checkbox("tech_ddac", 72, y, "Dynamic DAC (dDAC / time-resolved)")
y -= 20
draw_checkbox("tech_res", 72, y, "Resistively heated")
draw_checkbox("tech_sc", 260, y, "Single-crystal / Multi-grain DAC")
y -= 20
draw_checkbox("tech_tor", 72, y, "Toroidal DAC")
y -= 30
draw_text(72, y, "Other (please specify):")
y -= 20
draw_field("tech_other", 72, y, 400)
y -= 50

draw_text(72, y, "4. What DAC types will you be bringing?")
y -= 25
draw_checkbox("dac_std", 72, y, "Standard symmetric DAC (Princeton type)")
y -= 20
draw_checkbox("dac_bx90", 72, y, "BX-90")
draw_checkbox("dac_mem", 260, y, "Membrane-driven DAC")
y -= 20
draw_checkbox("dac_ddac", 72, y, "Dynamic DAC (dDAC)")
draw_checkbox("dac_vac", 260, y, "DAC in vacuum jacket")
y -= 20
draw_checkbox("dac_custom", 72, y, "Custom / in-house DAC")
draw_checkbox("dac_holder", 260, y, "Need a custom holder for DAC?")
y -= 30
draw_text(72, y, "Other (please specify):")
y -= 20
draw_field("dac_other", 72, y, 400)

# PAGE 2
c.showPage()
form = AcroForm(c)
form.textfield(name="lock_flag", tooltip="lock_flag", x=2, y=2, width=1, height=1, borderWidth=0)

y = height - 72
draw_text(72, y, "Beam Specs", "Helvetica-Bold", 13)
y -= 40

draw_text(72, y, "5. Sample chamber sizes (µm) (please list)")
y -= 20
draw_field("sample_chamber", 72, y, 400)
y -= 40

draw_text(72, y, "6. Required X-ray focus, FWHM (µm × µm)")
y -= 20
draw_field("xray_focus", 72, y, 400)
y -= 30

draw_text(72, y, "Typical focus (µm × µm):", "Helvetica-Oblique", 9)
y -= 18
draw_field("typ_focus_x", 72, y, 80, 16)
draw_text(160, y+4, "×", "Helvetica", 11)
draw_field("typ_focus_y", 180, y, 80, 16)
y -= 40

draw_text(72, y, "7. Preferred X-ray energy (keV)")
y -= 20
draw_field("pref_energy", 72, y, 400)
y -= 30

draw_text(72, y, "Default energy (keV):", "Helvetica-Oblique", 9)
y -= 18
draw_field("default_energy", 72, y, 100, 16)
y -= 40

draw_text(72, y, "8. Do you anticipate needing to defocus or change beam size during experiment?")
y -= 20
draw_checkbox("def_no", 72, y, "No")
draw_checkbox("def_yes", 140, y, "Yes")
y -= 30

draw_text(72, y, "If yes, please describe:")
y -= 0
# Multiline box for Q8
draw_field("def_desc", 72, y-72, 400, 68, border_style="solid")
y -= 100

draw_text(72, y, "Mirrors", "Helvetica-Bold", 13)
y -= 30

draw_text(72, y, "9. Which mirror will be used? (default: LKB)")
y -= 20
draw_checkbox("mirror_skb", 72, y, "SKB")
draw_checkbox("mirror_lkb", 140, y, "LKB")
y -= 40

draw_text(72, y, "10. Isolation mode? (Only for radiological beamtime)")
y -= 20
draw_checkbox("iso_no", 72, y, "No")
draw_checkbox("iso_yes", 140, y, "Yes")
y -= 30

draw_text(72, y, "Expected energy, mirror, or isolation mode changes during beamtime:")
y -= 25
draw_field("mirror_changes", 72, y, 400, 40, border_style="solid")

# PAGE 3 Daily plan
c.showPage()
form = AcroForm(c)
form.textfield(name="lock_flag", tooltip="lock_flag", x=2, y=2, width=1, height=1, borderWidth=0)

y = height - 72
draw_text(72, y, "Beamtime Daily Plan", "Helvetica-Bold", 13)
y -= 35

daily_fields = ["day1", "day2", "day3", "day4", "day5plus"]
daily_labels = ["Day 1:", "Day 2:", "Day 3:", "Day 4:", "Day 5+:"]

for name, label in zip(daily_fields, daily_labels):
    draw_text(72, y, label)
    y -= 0
    draw_field(name, 72, y-92, 400, 88, border_style="solid")
    y -= 120

# PAGE 4
c.showPage()
form = AcroForm(c)
form.textfield(name="lock_flag", tooltip="lock_flag", x=2, y=2, width=1, height=1, borderWidth=0)

y = height - 72
draw_text(72, y, "Capabilities", "Helvetica-Bold", 13)
y -= 40

draw_text(72, y, "11. Online ruby system?")
y -= 20
draw_checkbox("ruby_no", 72, y, "No")
draw_checkbox("ruby_yes", 140, y, "Yes")
y -= 40

draw_text(72, y, "12. Other high temperature method(s)")
y -= 20
draw_checkbox("ht_res", 72, y, "Resistive heating")
y -= 30

draw_text(72, y, "Please describe:")
y -= 20
draw_field("ht_desc", 72, y, 400)
y -= 50

draw_text(72, y, "13. Do you need any of the following?")
y -= 25
draw_checkbox("need_vac", 72, y, "Vacuum pump")
draw_checkbox("need_chill", 260, y, "Chiller")
y -= 20
draw_checkbox("need_tc", 72, y, "Thermocouple interface")
y -= 30

draw_text(72, y, "Other (please specify):")
y -= 20
draw_field("need_other", 72, y, 400)
y -= 50

draw_text(72, y, "14. How do you want to heat?")
y -= 20
draw_checkbox("heat_sq", 72, y, "Square modulated")
draw_checkbox("heat_cont", 260, y, "Continuous")
y -= 25

draw_text(72, y, "Please describe:")

# Multiline box for Q14 description
draw_field("trigger_scheme", 72, y-72, 400, 68, border_style="solid")

c.save()

# ---------- Postprocess: set multiline flags and inject JS ----------
reader = PdfReader(base_pdf)
writer = PdfWriter()
for page in reader.pages:
    writer.add_page(page)

acro = reader.trailer["/Root"].get("/AcroForm")
if acro:
    writer._root_object.update({NameObject("/AcroForm"): acro})

def iter_fields(field_refs):
    for fref in field_refs:
        fobj = fref.get_object()
        yield fobj
        kids = fobj.get("/Kids")
        if kids:
            yield from iter_fields(kids)

writer_acro = writer._root_object.get("/AcroForm")
field_refs = writer_acro.get("/Fields", []) if writer_acro else []

MULTILINE = 4096
DONOTSCROLL = 1 << 24
target_names = {"day1", "day2", "day3", "day4", "day5plus", "def_desc", "trigger_scheme"}

for fobj in iter_fields(field_refs):
    t = fobj.get("/T")
    if t and str(t) in target_names:
        ff = int(fobj.get("/Ff", 0))
        ff = (ff | MULTILINE) & (~DONOTSCROLL)
        fobj.update({
            NameObject("/Ff"): NumberObject(ff),
            NameObject("/DA"): TextStringObject("/Helv 10 Tf 0 g"),
        })



with open(final_pdf, "wb") as f:
    writer.write(f)

final_pdf