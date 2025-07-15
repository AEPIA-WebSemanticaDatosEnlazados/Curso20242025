import json

def process_authors(authors):
    authors_parsed = []
    for author in authors:
        if isinstance(author, list) and len(author) >= 1:
            surname = author[0].strip()
            rest = " ".join(a.strip() for a in author[1:] if a.strip())
            full_name = f"{surname} {rest}".strip()
            authors_parsed.append(full_name)
    return authors_parsed

def transform_json(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file, open(output_file, 'w', encoding='utf-8') as out:
        for line in file:
            record = json.loads(line)
            if "authors_parsed" in record:
                record["authors_parsed"] = process_authors(record["authors_parsed"])
            out.write(json.dumps(record) + '\n')

if __name__ == "__main__":
    input = "arxiv-reduced.json"  
    output = "output.json"
    transform_json(input, output)
