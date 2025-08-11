from setuptools import setup, find_packages

requires = [
    "zmq",
    "pytz",
    "loguru",
    "alembic",
    "pydantic",
    "overrides",
    "websockets",
    "psycopg-pool",
    "pcycopg-binary",
]

setup(
    name="cbot",
    version="0.0.1",
    author="Maksim Konovalov",
    author_email="maksim@mkv.ee",
    description=(""),
    packages=["cbot", "tests"],
    install_requires=requires,
    long_description="README",
)
