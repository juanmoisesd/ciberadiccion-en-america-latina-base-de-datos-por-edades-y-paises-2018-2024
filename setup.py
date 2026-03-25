from setuptools import setup, find_packages
setup(
    name="ciberadiccion-en-america-latina-base-de-datos-por-edades-y-paises-2018-2024",
    version="1.0.0",
    description="Base de datos sobre ciberadicción (adicción a internet, redes sociales y videojuegos) en América Lat",
    author="de la Serna, Juan Moisés",
    url="https://github.com/juanmoisesd/ciberadiccion-en-america-latina-base-de-datos-por-edades-y-paises-2018-2024",
    packages=find_packages(),
    install_requires=["pandas>=1.3.0","requests>=2.26.0"],
    python_requires=">=3.7",
    classifiers=["Programming Language :: Python :: 3","License :: OSI Approved :: MIT License","Topic :: Scientific/Engineering"],
    keywords="age-structure, cc0, citation, cyberaddiction, dataset, demographic-transition, demography, digital-health, fair-data, iberoamerica, juan-moises-de-la-serna, latin-america, open-data, open-science, orcid, population-data, research, tech-adoption, technology, zenodo, zenodo, open-data",
)