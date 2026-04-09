from pymed import PubMed

# Initialize PubMed with your tool name and email (required by NCBI)
pubmed = PubMed(tool="MySearchTool", email="your@email.com")

# Query the database
results = pubmed.query("machine learning in medicine", max_results=100)

# Iterate through results
for article in results:
    print(f"Title: {article.title}")
    print(f"Publication Date: {article.publication_date}")
    print(f"Abstract: {article.abstract[:100]}...")


