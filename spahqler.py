#!/usr/bin/env python
"""Run SPARQL on a small local dataset.

cf.
https://jena.apache.org/documentation/query/cmds.html

see also:
https://rdflib.readthedocs.io/en/stable/intro_to_sparql.html
"""
import argparse
import logging
import rdflib
import re

parser = argparse.ArgumentParser(description='Run SPARQL on a small local dataset.',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--query', '-q', required=True,
                    help='File name of stored query, or query string (presence of { used to signal string query)')
parser.add_argument('--graph', '-g', required=True,
                    help='File name of graph data')
parser.add_argument('--binding', '-b', default=[], action='append',
                    help='Initial variable bindings of the form x=<uri> or y="str"')
parser.add_argument('--graph-format', default='nt',
                    help='Format of graph data')
parser.add_argument('--format', default='nt',
                    help="Output graph format for CONSTRUCT/DESCRIBE query results")
args = parser.parse_args()

sparql = """CONSTRUCT { ?term ?p ?o . ?o rdfs:label ?o2 . } WHERE { ?term ?p ?o . OPTIONAL { ?o rdfs:label ?o2 . } }"""

# Load graph
g = rdflib.Graph()
g.parse(args.graph, format=args.graph_format)

# Get/load query
if '{' in args.query:
    query = args.query
else:
    with open(args.query, 'r') as fh:
        query = fh.read()

# Parse any parameter bindings
bindings = {}
for binding in args.binding:
    m = re.match(r'''(\w+)=([\<"])(.*)(["\>])$''', binding)
    if not m:
        raise Exception("Bad binding %s" % (binding))
    elif m.group(2) != m.group(4) and m.group(2) != '<' and m.group(4) != '>':
        raise Exception("Mismatching delimiters %s and %s in binding %s" % (m.group(2), m.group(4), binding))
    bindings[m.group(1)] = rdflib.Literal(m.group(3)) if m.group(2) == '"' else rdflib.URIRef(m.group(3))

# Run query
res = g.query(query, initBindings=bindings)

# Find result type
if res.type == 'SELECT':
    # Was SELECT -> rows
    n = 0
    for row in res:
        n += 1
        print("%-6s  %s" % ('[' + str(n) + ']', " \t".join(row)))
else:
    # Was CONSTRUCT/DESCRIBE -> triples
    print(res.serialize(encoding=None, format=args.format).decode('utf-8'))
