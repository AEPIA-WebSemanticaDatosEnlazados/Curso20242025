import xml.etree.ElementTree as ET
import sys
import os

if len(sys.argv) != 3:
    print("Usage: python transform_named_individuals.py input.xml output.xml")
    sys.exit(1)

script_dir = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(script_dir, sys.argv[1])
output_file = os.path.join(script_dir, sys.argv[2])

ET.register_namespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
ET.register_namespace('owl', 'http://www.w3.org/2002/07/owl#')
ET.register_namespace('skos', 'http://www.w3.org/2004/02/skos/core#')

ns = {
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'owl': 'http://www.w3.org/2002/07/owl#',
    'skos': 'http://www.w3.org/2004/02/skos/core#'
}

tree = ET.parse(input_file)
root = tree.getroot()

for indiv in root.findall(".//{http://www.w3.org/2002/07/owl#}NamedIndividual"):
    types = indiv.findall("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}type")
    is_concept = any(
        t.attrib.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource") == "http://www.w3.org/2004/02/skos/core#Concept"
        for t in types
    )

    if is_concept:
        inscheme = indiv.find("{http://www.w3.org/2004/02/skos/core#}inScheme")
        if inscheme is not None:
            scheme_uri = inscheme.attrib.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
            if scheme_uri and '#' in scheme_uri:
                scheme_name = scheme_uri.split('#')[-1]

                about_uri = indiv.attrib.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about")
                if about_uri and '#' in about_uri and about_uri.endswith(f"#{about_uri.split('#')[-1]}"):
                    fragment = about_uri.split('#')[-1]
                    base = about_uri.split('#')[0]

                    new_about = f"{base}/{scheme_name}#{fragment}"

                    # Debug output
                    print("----")
                    print("Original rdf:about URI: ", about_uri)
                    print("inScheme URI:           ", scheme_uri)
                    print("Extracted schemeName:   ", scheme_name)
                    print("New URI:                ", new_about)

                    indiv.set("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about", new_about)

tree.write(output_file, encoding="utf-8", xml_declaration=True)
print("\nOutput written to:", sys.argv[2])
