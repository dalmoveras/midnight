# Midnight

## A Deep Web Datamining and Search Tool

### Pre requisites
* python3
* virtualenv
* virtualenvwrapper
* tor

### Installing
1. `mkvirtualenv midnight`
2. `git clone https://github.com/murksombra/midnight`
3. `cd midnight`
4. `pip3 install requirements.txt`


### Running the scrapper
You should provide the entry point (domain.onion). If none is provided, midgnight will start from:`http://76qugh5bey5gum7l.onion`.
Please, keep in mind that .onions are living things and the provided default .onion could not be available in the future.

Run: `python3 midnight <domain.onion>`

### Running the search
Run: `python3 search.py`

