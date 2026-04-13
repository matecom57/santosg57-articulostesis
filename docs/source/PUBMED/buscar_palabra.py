from pymed import PubMed
import sys

print(sys.argv)

palabra = sys.argv[1]

pubmed = PubMed(tool="MyTool", email="my@email.address")

query = '(' + palabra + '[Title]) AND ((2026/01/01[Date - Publication] : 3000[Date - Publication]))'
#query = "(" + palabra + "[Title]) AND (2026/1/1[Date - Publication] : 3000[Date - Publication])"

# Execute the query against the API
results = pubmed.query(query, max_results=5000)

# Loop over the retrieved articles
for article in results:

    # Print the type of object we've found (can be either PubMedBookArticle or PubMedArticle)
    print(type(article))

    # Print a JSON representation of the object
    print(article.toJSON())

