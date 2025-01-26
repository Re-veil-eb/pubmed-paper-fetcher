import click
from pubmed_paper_fetcher.fetch_papers import PubMedFetcher
from pubmed_paper_fetcher.process_papers import PaperProcessor

@click.command()
@click.argument("query")
@click.option("-f", "--file", type=click.Path(), help="File to save the results")
@click.option("-d", "--debug", is_flag=True, help="Enable debug mode")
def main(query, file, debug):
    """
    Fetch research papers based on a user query.
    """
    if debug:
        click.echo(f"Query: {query}")

    # Fetch paper IDs
    fetcher = PubMedFetcher()
    paper_ids = fetcher.fetch_paper_ids(query)
    click.echo(f"Found {len(paper_ids)} papers.")

    # Fetch paper details
    processor = PaperProcessor()
    results = processor.fetch_paper_details(paper_ids)

    # Output results
    if file:
        results.to_csv(file, index=False)
        click.echo(f"Results saved to {file}")
    else:
        click.echo(results)

if __name__ == "__main__":
    main()
