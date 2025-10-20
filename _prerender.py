import re
from pathlib import Path

src_dir = Path("policies_procedures")
dest_dir = Path("_includes")
dest_dir.mkdir(exist_ok=True)

yaml_pattern = re.compile(r"^---\n.*?\n---\n", re.DOTALL)

for qmd_file in src_dir.glob("*.qmd"):
    text = qmd_file.read_text(encoding="utf-8")
    stripped = re.sub(yaml_pattern, "", text, count=1)
    out_file = dest_dir / qmd_file.name
    out_file.write_text(stripped.strip() + "\n", encoding="utf-8")
    # print(f"Stripped YAML: {qmd_file} → {out_file}")
