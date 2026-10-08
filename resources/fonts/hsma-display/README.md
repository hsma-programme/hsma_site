# HSMA Display

A display font built from the lettering in the HSMA logo (`resources/Chalky HSMA-07-wide white logo.png`),
for logo-style page titles.

- `HSMADisplay-Regular` is grooved like the logo: each stroke has a narrow groove along its centre.
- `HSMADisplaySolid-Regular` is the same letters without the groove, for small sizes.

Use the `.woff2` files on the website; the `.ttf` files are for design tools.

Lowercase characters type the same capitals, so titles don't need `text-transform: uppercase`
(which would also turn λ into Λ).

## How the letters are made

The logo's letters follow a few rules: a single stroke weight (about a fifth of the cap height), lighter
diagonals, slightly rounded corners, and a groove along each stroke's centre line that stops half a stroke
short of the ends. Round letters overshoot the cap height and baseline slightly.

- S and M are traced directly from the high-resolution logo.
- Every other glyph is drawn as centre lines in `build/glyphs.py`, then thickened into the solid letter
  and grooved by the same rules, so new letters stay consistent with the logo's.

## Rebuilding

```bash
python -m venv .venv
.venv/Scripts/pip install -r resources/fonts/hsma-display/build/requirements.txt   # bin/ on macOS/Linux
.venv/Scripts/python resources/fonts/hsma-display/build/build_font.py
```

To add or change a letter, edit its centre lines in `build/glyphs.py` and rebuild.
`build/calibrate.py` overlays rebuilt letters on the logo's originals (writes `build/calib.png`) to check
they line up.
