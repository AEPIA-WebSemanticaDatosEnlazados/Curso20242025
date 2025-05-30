import sys
from SPARQLWrapper import SPARQLWrapper, JSON
import requests
import certifi
import urllib3

# Endpoint config
GRAPHDB_ENDPOINT = "http://localhost:7200/repositories/CreditEvaluationData"

def execute_query_from_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            query = f.read()
    except FileNotFoundError:
        print(f"Error: file not found: {file_name}")
        return

    sparql = SPARQLWrapper(GRAPHDB_ENDPOINT)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)

    try:
        resultados = sparql.query().convert()
        print("Results:")
        for res in resultados["results"]["bindings"]:
            print({k: v["value"] for k, v in res.items()})
    except Exception as e:
        print(f"Error executing query: {e}")

# Funciones de menú

def query_1():
    print("Number of credits by class and purpose")
    sparql = SPARQLWrapper(GRAPHDB_ENDPOINT) 
    sparql.setReturnFormat(JSON)

    query = """
    PREFIX ccf: <http://data.creditclassification.biz/ontology/ccf#> 
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>

    SELECT ?altLabel  ?classDescription (COUNT(?evaluation) AS ?total)
    WHERE {
      ?evaluation a ccf:credit_evaluation ;
                  ccf:has_purpose ?purpose_code ;
                  ccf:has_class ?class .

      OPTIONAL { ?purpose_code skos:altLabel ?altLabel }
      OPTIONAL { ?class dcterms:description ?classDescription }
    }
    GROUP BY ?purpose_code ?altLabel ?class ?classDescription
    ORDER BY ?purpose_code ?class
    """

    sparql.setQuery(query)
    try:
        results = sparql.query().convert()

        print(f"{'Alt Label':<20} {'Class Description':<40} {'Count':<10}")
        print("-" * 150)

        for result in results["results"]["bindings"]:
            alt_label = result.get("altLabel", {}).get("value", "")
            class_description = result.get("classDescription", {}).get("value", "")
            count = result.get("total", {}).get("value", "")

            print(f"{alt_label:<20} {class_description:<40} {count:<10}")

    except Exception as e:
        print("An error occurred:", e)


def query_2():
    print("Info about loan term, credit classification and employment status for credits above a given amount, foreing worker status and housing")
    sparql = SPARQLWrapper(GRAPHDB_ENDPOINT) 
    sparql.setReturnFormat(JSON)

    # Step 1 – Ask for input
    credit_amount = input("Enter credit amount (e.g. 1000): ").strip()
    foreign_worker = input("Is the requestor a foreign worker? (yes/no): ").strip().lower()
    is_foreign = "http://data.creditclassification.biz/ontology/ccf/foreign_worker#A201" if foreign_worker == "yes" else "http://data.creditclassification.biz/ontology/ccf/foreign_worker#A202"

    # Step 2 – Get available housing options
    print("\nFetching housing options...")
    sparql.setQuery("""
    PREFIX ccf: <http://data.creditclassification.biz/ontology/ccf#>
    PREFIX dcterms: <http://purl.org/dc/terms/>

    SELECT DISTINCT ?housing ?desc WHERE {
      ?requestor ccf:has_housing ?housing .
      OPTIONAL { ?housing dcterms:description ?desc }
    }
    """)
    try:
        results = sparql.query().convert()
        housing_options = []
        print("\nAvailable Housing Options:")
        for i, res in enumerate(results["results"]["bindings"], start=1):
            uri = res["housing"]["value"]
            desc = res.get("desc", {}).get("value", "No description")
            housing_options.append((uri, desc))
            print(f"{i}. {desc} [{uri.split('/')[-1]}]")

        # Step 3 – Let user pick one
        choice = int(input("Select a housing option (number): ").strip())
        selected_housing_uri = housing_options[choice - 1][0]
        selected_desc = housing_options[choice - 1][1]

        print("\nRunning filtered query...\n")

        # Step 4 – Final query with user inputs
        sparql.setQuery(f"""
        PREFIX ccf: <http://data.creditclassification.biz/ontology/ccf#>
        PREFIX schema: <https://schema.org/>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>   
        PREFIX dcterms: <http://purl.org/dc/terms/>                                             

        SELECT ?loanTerm ?classDescription ?employment_status ?amountNum
        WHERE {{
          ?evaluation a ccf:credit_evaluation ;
                      ccf:has_credit_requestor ?requestor ;
                      ccf:has_class ?class ;
                      schema:loanTerm ?loanTerm ;
                      schema:amount ?amount .

          ?requestor a ccf:credit_requestor ;
                     ccf:has_foreign_worker <{is_foreign}>;
                     ccf:has_housing <{selected_housing_uri}> ;
                     ccf:has_employment_status ?employment_status .

        BIND(xsd:integer(?amount) AS ?amountNum)
        FILTER(?amountNum > {int(credit_amount)})
        OPTIONAL {{ ?class dcterms:description ?classDescription }}        
        }}
        """)

        final_results = sparql.query().convert()
        print(f"{'Loan Term':<12} {'Class':<30} {'Employment Status':<20}")
        print("-" * 65)
        for res in final_results["results"]["bindings"]:
            term_raw = res["loanTerm"]["value"]  # e.g., P24M
            months = int(term_raw.replace("P", "").replace("M", ""))
            term_text = f"{months} month" if months == 1 else f"{months} months"
            credit_class = res["classDescription"]["value"].split("/")[-1]
            employment = res["employment_status"]["value"].split("/")[-1]
            print(f"{term_text:<12} {credit_class:<30} {employment:<20}")

    except Exception as e:
        print("Error:", e)


def query_3():
    print("Query by purpose, retrieving external info for the purpose")
    sparql = SPARQLWrapper(GRAPHDB_ENDPOINT) 
    sparql.setReturnFormat(JSON)

    # Step 1: Retrieve all possible has_purpose values with their altLabels
    sparql.setQuery("""
    PREFIX ccf: <http://data.creditclassification.biz/ontology/ccf#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    SELECT DISTINCT ?purpose ?altLabel WHERE {
      ?evaluation a ccf:credit_evaluation ;
                  ccf:has_purpose ?purpose .
      OPTIONAL { ?purpose skos:altLabel ?altLabel }
    }
    ORDER BY ?altLabel
    """)
    results = sparql.query().convert()
    purposes = []
    print("\nAvailable Credit Purposes:")
    for i, res in enumerate(results["results"]["bindings"], start=1):
        uri = res["purpose"]["value"]
        label = res.get("altLabel", {}).get("value", uri.split("/")[-1])
        purposes.append((uri, label))
        print(f"{i}. {label} [{uri.split('/')[-1]}]")

    choice = int(input("Select a credit purpose (number): ").strip())
    selected_uri, selected_label = purposes[choice - 1]

    # Step 2: Count credit_evaluation entries for selected purpose
    sparql.setQuery(f"""
    PREFIX ccf: <http://data.creditclassification.biz/ontology/ccf#>

    SELECT (COUNT(?evaluation) AS ?count)
    WHERE {{
      ?evaluation a ccf:credit_evaluation ;
                  ccf:has_purpose <{selected_uri}> .
    }}
    """)
    count_result = sparql.query().convert()
    count_value = count_result["results"]["bindings"][0]["count"]["value"]
    print(f"\nTotal credit evaluations with the chosen purpose: {count_value}")

    # Step 3: Get skos:exactMatch and skos:closeMatch for the selected purpose
    sparql.setQuery(f"""
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    SELECT ?match ?type WHERE {{
        {{
            <{selected_uri}> skos:exactMatch ?match .
            BIND("exactMatch" AS ?type)
        }}
        UNION
        {{
            <{selected_uri}> skos:closeMatch ?match .
            BIND("closeMatch" AS ?type)
        }}
    }}
    """)

    matches = sparql.query().convert()

    exact_matches = []
    close_matches = []

    for res in matches["results"]["bindings"]:
        match_uri = res["match"]["value"]
        match_type = res["type"]["value"]
        if match_type == "exactMatch":
            exact_matches.append(match_uri)
        elif match_type == "closeMatch":
            close_matches.append(match_uri)

    # Step 4: Process and display match information
    if exact_matches:
        print("\nThe meaning of the chosen purpose is described in the following URLs:")
        for uri in exact_matches:
            print(f"- {uri}")
        for uri in exact_matches:
            info = fetch_external_info(uri)
            if info:
                print(f"\nFrom this source {uri}, this info about the chosen purpose has been retrieved:\n{info}")
    elif close_matches:
        print("\nThe approximate meaning of the chosen purpose is described in the following URLs:")
        for uri in close_matches:
            print(f"- {uri}")
        for uri in close_matches:
            info = fetch_external_info(uri)
            if info:
                print(f"\nFrom this source {uri}, this info about the chosen purpose has been retrieved:\n{info}")
    else:
        print("\nThere is no additional data about the meaning of the chosen purpose.")


def fetch_external_info(uri):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    headers = {'Accept': 'application/json'}
    try:
        if "wikidata.org" in uri:
            entity_id = uri.split("/")[-1]
            url = f"https://www.wikidata.org/wiki/Special:EntityData/{entity_id}.json"
            response = requests.get(url, headers=headers, verify=False)
            if response.status_code == 200:
                data = response.json()
                entity = data.get("entities", {}).get(entity_id, {})
                return entity.get("descriptions", {}).get("en", {}).get("value", "")
        elif "dbpedia.org" in uri:
            entity_id = uri.split("/")[-1]
            url = f"https://dbpedia.org/data/{entity_id}.json"
            response = requests.get(url, headers=headers, verify=False)
            if response.status_code == 200:
                data = response.json()
                resource_uri = f"http://dbpedia.org/resource/{entity_id}"
                resource_data = data.get(resource_uri, {})
                # Attempt to retrieve dcterms:description
                descriptions = resource_data.get("http://purl.org/dc/terms/description", [])
                for desc in descriptions:
                    if desc.get("lang") == "en":
                        return desc.get("value", "")
                # Fallback to dbo:abstract if dcterms:description is not available
                abstracts = resource_data.get("http://dbpedia.org/ontology/abstract", [])
                for abstract in abstracts:
                    if abstract.get("lang") == "en":
                        return abstract.get("value", "")
        return None
    except Exception as e:
        print(f"Error fetching data from {uri}: {e}")
        return None

def show_menu():
    print("\n--- Options available ---")
    print("1 - Number of credits by class and purpose")
    print("2 - Info about loan term, credit classification and employment status for credits above a given amount, foreing worker status and housing")
    print("3 - Query by purpose, retrieving external info for the purpose")
    print("0 - Exit")

    option = input("Select an option : ").strip()

    options = {
        "1": query_1,
        "2": query_2,
        "3": query_3,    
    }

    if option == "0":
        print("Exiting...")
        return
    elif option in options:
        options[option]()
    else:
        print("Invalid option")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        archivo_query = sys.argv[1]
        execute_query_from_file(archivo_query)
    else:
        print("Show menu")
        show_menu()
