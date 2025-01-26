import unittest
from unittest.mock import patch
from pubmed_paper_fetcher.fetch_papers import PubMedFetcher

class TestPubMedFetcher(unittest.TestCase):
    @patch("requests.get")
    def test_fetch_paper_ids_valid_query(self, mock_get):
        """
        Test fetching paper IDs with a valid query.
        """
        # Mock API response for a successful query
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "esearchresult": {
                "idlist": ["12345", "67890"]
            }
        }

        # Call the method
        paper_ids = PubMedFetcher.fetch_paper_ids("cancer research")

        # Assertions
        self.assertEqual(len(paper_ids), 2)
        self.assertEqual(paper_ids, ["12345", "67890"])
        mock_get.assert_called_once()

    @patch("requests.get")
    def test_fetch_paper_ids_empty_query(self, mock_get):
        """
        Test fetching paper IDs with an empty query.
        """
        with self.assertRaises(ValueError):
            PubMedFetcher.fetch_paper_ids("")

    @patch("requests.get")
    def test_fetch_paper_ids_api_error(self, mock_get):
        """
        Test handling an API error (e.g., 500 Internal Server Error).
        """
        # Mock API response for an error
        mock_get.return_value.status_code = 500
        mock_get.return_value.json.return_value = {}

        # Call the method
        paper_ids = PubMedFetcher.fetch_paper_ids("cancer research")

        # Assertions
        self.assertEqual(paper_ids, [])
        mock_get.assert_called_once()

    @patch("requests.get")
    def test_fetch_paper_ids_no_results(self, mock_get):
        """
        Test fetching paper IDs when no results are found.
        """
        # Mock API response with no results
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "esearchresult": {
                "idlist": []
            }
        }

        # Call the method
        paper_ids = PubMedFetcher.fetch_paper_ids("random string with no results")

        # Assertions
        self.assertEqual(len(paper_ids), 0)
        self.assertEqual(paper_ids, [])
        mock_get.assert_called_once()


if __name__ == "__main__":
    unittest.main()
