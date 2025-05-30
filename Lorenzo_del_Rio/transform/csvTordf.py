import csv
from jinja2 import Environment, FileSystemLoader

# Load CSV data into a list of dicts
with open('./german-data_transformed.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

# Load the template
env = Environment(loader=FileSystemLoader('.'))  # current dir
template = env.get_template('./template_xml.j2')

# Render template
output = template.render(rows=rows)

# Save output
with open('./german_data_rdf.rdf', 'w') as f:
    f.write(output)

print("Generated german_data_rdf.rdf")