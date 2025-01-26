import requests
from typing import List

class PubMedFetcher:
    BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

    @staticmethod
    def fetch_paper_ids(query: str, retmax: int = 10) -> List[str]:
        """
        Fetch paper IDs from PubMed based on a query.
        :param query: Search query.
        :param retmax: Maximum number of results to return.
        :return: List of PubMed IDs.
        """
        if not query.strip():
            raise ValueError("Query cannot be empty.")

        params = {
            "db": "pubmed",
            "term": query,
            "retmax": retmax,
            "retmode": "json",
        }
        try:
            response = requests.get(PubMedFetcher.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data.get("esearchresult", {}).get("idlist", [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching papers: {e}")
            return []
