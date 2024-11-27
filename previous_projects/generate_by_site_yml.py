# Thanks Perplexity!

import os

dir_path = os.path.dirname(os.path.realpath(__name__))

all_organisations = []

for root, dirs, files in os.walk(f"{dir_path}/previous_projects"):
    if 'index.qmd' in files:
        file_path = os.path.join(root, 'index.qmd')
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.readlines()
            organisations_found = False
            for line in content:
                if 'organisations:' in line:
                    organisations_found = True
                    continue
                if organisations_found:
                    line = line.strip()
                    if line.startswith('- '):
                        org = line[2:].strip()  # Remove the hyphen and leading/trailing whitespace
                        all_organisations.append(org)
                    else:
                        break  # Stop if we encounter a line that

all_organisations.sort()

print(all_organisations)

all_orgs_unique = list(set(all_organisations))

all_orgs_unique.sort()

print(all_orgs_unique)

quarto_file_string = ""

header_text = """---
title: "Projects by Organisation"
toc-location: right
title-block-banner: banner.png
include-back-link: false
grid:
  sidebar-width: 0px
  body-width: 1100px
  margin-width: 300px
  gutter-width: 1.5rem
listing:
"""

quarto_file_string += header_text

for i, org in enumerate(all_orgs_unique):
    quarto_file_string += f"""
    - id: projects_{i}
      contents: "*/*/index.qmd"
      sort: "date desc"
      type: grid
      grid-columns: 2
      page-size: 1000
      categories: false
      include:
        organisations: "{org}"
      template: ../html/previous_projects/listing.ejs
    """


header_ending = """
---
\n
"""

quarto_file_string += header_ending


quarto_file_string += """```{=html}
<style>
h2 {
text-transform: uppercase;
font-weight: 400;
text-align: left;
}
</style>
```
\n
"""

for i, org in enumerate(all_orgs_unique):
    quarto_file_string += f"""## {org}
\n
:::{{#projects_{i}}}
:::
\n
"""

print(quarto_file_string)

with open("previous_projects/projects_by_organisation.qmd", 'w', encoding='utf-8') as file:
    file.write(quarto_file_string)
