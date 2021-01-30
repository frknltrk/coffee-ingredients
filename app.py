# http://dbpedia.org/page/Category:Coffee_drinks
from rdflib import Graph
from SPARQLWrapper import SPARQLWrapper, JSON, N3
from pprint import pprint

sparql = SPARQLWrapper('https://dbpedia.org/sparql')
sparql.setReturnFormat(JSON)

def search_by_additive(additive):
    query = """
        SELECT DISTINCT ?name
            WHERE {
                ?subject rdfs:label ?name .
                ?subject dbo:ingredientName ?someIngredient .
                ?subject ?predicate dbc:Coffee_drinks .
                FILTER (lang(?name) = 'en')
                FILTER regex(?someIngredient, '%s', 'i')
            }
            ORDER BY ?name
            """

    sparql.setQuery(query%additive)
    qres = sparql.query().convert()

    print("\nCOFFEE DRINKS WITH {} IN THEM".format(additive))
    for result in qres['results']['bindings']:
        print(result['name']['value'])

search_by_additive('milk')
search_by_additive('water')
search_by_additive('chocolate')
