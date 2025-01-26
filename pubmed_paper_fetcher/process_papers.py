import requests
import pandas as pd
from typing import List
import xml.etree.ElementTree as ET

class PaperProcessor:
    BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

    @staticmethod
    def fetch_paper_details(paper_ids: List[str]) -> pd.DataFrame:
        """
        Fetch details for a list of PubMed IDs.
        :param paper_ids: List of PubMed IDs.
        :return: DataFrame containing paper details.
        """
        if not paper_ids:
            raise ValueError("No paper IDs provided to fetch details.")

        ids = ",".join(paper_ids)
        params = {
            "db": "pubmed",
            "id": ids,
            "retmode": "xml",
        }

        try:
            response = requests.get(PaperProcessor.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            root = ET.fromstring(response.content)

            # Parse the XML
            data = []
            for article in root.findall(".//PubmedArticle"):
                try:
                    pubmed_id = article.findtext(".//PMID")
                    title = article.findtext(".//ArticleTitle")
                    publication_date = PaperProcessor._parse_publication_date(article)
                    non_academic_authors, company_affiliations = PaperProcessor._extract_affiliations(article)
                    corresponding_email = PaperProcessor._extract_corresponding_email(article)

                    data.append({
                        "PubmedID": pubmed_id,
                        "Title": title,
                        "Publication Date": publication_date,
                        "Non-academic Authors": non_academic_authors,
                        "Company Affiliations": company_affiliations,
                        "Corresponding Author Email": corresponding_email,
                    })
                except Exception as e:
                    print(f"Error parsing article: {e}")

            return pd.DataFrame(data)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching paper details: {e}")
            return pd.DataFrame()

    @staticmethod
    def _parse_publication_date(article: ET.Element) -> str:
        """Extract publication date from the XML."""
        pub_date = article.find(".//PubDate")
        if pub_date is not None:
            year = pub_date.findtext("Year", default="Unknown")
            month = pub_date.findtext("Month", default="Unknown")
            day = pub_date.findtext("Day", default="Unknown")
            return f"{year}-{month}-{day}"
        return "Unknown"

    @staticmethod
    def _extract_affiliations(article: ET.Element) -> tuple:
        """Extract non-academic authors and company affiliations."""
        affiliations = article.findall(".//AffiliationInfo")
        non_academic_authors = []
        company_affiliations = []

        for affiliation in affiliations:
            text = affiliation.findtext("Affiliation", "")
            if any(keyword in text.lower() for keyword in ["pharma", "biotech", "inc.", "ltd.", "gmbh"]):
                company_affiliations.append(text)
                # Assuming author names are not easily parsed, this is a placeholder.
                non_academic_authors.append("Unknown Author")

        return ", ".join(non_academic_authors), ", ".join(company_affiliations)

    @staticmethod
    def _extract_corresponding_email(article: ET.Element) -> str:
        """Extract corresponding author's email if available."""
        emails = article.findall(".//AffiliationInfo/Affiliation")
        for email in emails:
            if "@" in email.text:
                return email.text
        return "Not Available"
