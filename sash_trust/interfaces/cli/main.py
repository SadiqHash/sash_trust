import typer
from sash_trust.interfaces.library.api import scan

app = typer.Typer()


@app.command()
def run(target: str, policy: str):
    result = scan(target, policy)
    typer.echo(f"Trust Score: {result.trust_score}")

    for finding in result.findings:
        typer.echo(f"{finding.file_path}: {finding.message}")
