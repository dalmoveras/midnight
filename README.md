# Midnight - A Deep Web Scraper and Search Tool
This is a work in progress. Always remember to `git pull` and submit issues.

### Pre requisites
* python3
* virtualenv
* virtualenvwrapper
* tor (tor service must be running)

### Installing
1. `mkvirtualenv midnight`
2. `git clone https://github.com/murksombra/midnight`
3. `cd midnight`
4. `pip3 install requirements.txt`


### Running the scraper
You should provide the entry point (domain.onion). If none is provided, midgnight will start from:`http://76qugh5bey5gum7l.onion`.
Please, keep in mind that .onions are living things and the provided default .onion could not be available in the future.

Run: `python3 midnight <domain.onion>`

<img width="659" alt="Screen Shot 2022-07-21 at 10 22 53 AM" src="https://user-images.githubusercontent.com/6532445/180235246-2bcd8d0c-6d2f-4927-8290-0d4ac2e47758.png">

### Running the search
Run: `python3 search.py`

<img width="823" alt="Screen Shot 2022-07-21 at 10 22 27 AM" src="https://user-images.githubusercontent.com/6532445/180235265-f8641480-84fb-4e50-9fd3-ba1ebe644851.png">
