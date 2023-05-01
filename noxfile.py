"""Nox configuration file.

Please refer to https://nox.thea.codes/en/stable/index.html for more info.
"""
import nox


@nox.session(
    name="static-checks",
    python=["3.8", "3.9", "3.10", "3.11"]
)
def static_checks(session):
    """Runs static checks using Ruff. Refer to [tools.ruff] pyproject.toml section."""
    session.install(".[dev]")
    session.run("ruff","check", ".", *session.posargs)


@nox.session(
    name="unit-tests",
    python=["3.8", "3.9", "3.10", "3.11"]
)
def unit_tests(session):
    """Runs Unit Tests using Pytest and pytest-cov."""
    session.install(".[dev]")
    session.run("pytest", "--cov=src", "tests/unit",  *session.posargs)


@nox.session(
    name="integration-tests",
    python=["3.8", "3.9", "3.10", "3.11"]
)
def integration_tests(session):
    """Runs Unit Tests using Pytest and pytest-cov."""
    session.install(".[dev]")
    session.run("pytest", "--cov=src", "tests/integration", *session.posargs)
