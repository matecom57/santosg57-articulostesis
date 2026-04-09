from pymed import PubMed
import sys

print(sys.argv[0])
print(sys.argv[1])
print(len(sys.argv))

pubmed = PubMed(tool="MyTool", email="my@email.address")

#query = "ANTs[Title/Abstract]"

pal1 = sys.argv[2]
pal2 = sys.argv[3]
pal3 = sys.argv[4]

file = sys.argv[1]

#palabra = '('+ pal1 + '[Title] AND ' + pal2 + '[Title])'

palabra = '('+ pal1 + '[Title] AND ' + pal2 + '[Title] AND ' + pal3 + '[Title])'

#query = palabra+"[Title/Abstract]"
query = palabra + ' AND (("1995/01/01"[Date - Publication] : "3000"[Date - Publication]))'
print(query)

results = pubmed.query(query, max_results=1000)

fil = open(file+'.txt', 'w')

for article in results:
# print(article.toJSON())
 fil.write(article.toJSON())

fil.close()


