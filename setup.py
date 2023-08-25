from setuptools import setup

setup(
    name="CustomConventionalCommitsCz",
    version="0.1.0",
    py_modules=["cz_custom_conventional"],
    license="MIT",
    long_description="A commitizen plugin similar cz_conventional_commits that replaces the build and ci prefixes with the more generic chore prefix",
    install_requires=["commitizen"],
    entry_points={"commitizen.plugin": ["cz_custom_conventional = cz_custom_conventional:CustomConventionalCommitsCz"]},
)
