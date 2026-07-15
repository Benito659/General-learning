## Gazpacho
Gazpacho is a fast, simple, and modern web scraping library. It was created as a lightweight alternative to heavier tools like requests and BeautifulSoup. It installs with zero external dependencies and provides a clean syntax for downloading web pages and extracting data from HTML

### Installation
```bash
    python -m pip install gazpacho
```

### Get Html Pages
- To use gazpacho to download a website we'll need to run the get function;
```python
    url= "https://pypi.org/project/pandas/#history"
    from gazpacho import get
    html = get(url)
```
- You might get an error 
- Something like "unable to get local issuer certificate"
- You're probably on a new mac that doesn't have the certificates packages installed
- You can fix this by either installing certifi with pip or by running the install command in the main python installation on your machine
- can learn more about here https://stackoverflow.com/questions/52805115/error-certificate-verify-failed-unable-to-get-local-issuer-certificate



### Soup 
- Soup object will parse the html we get from gazpacho
- we can now query it
```python
    url= "https://pypi.org/project/pandas/#history"
    from gazpacho import get, Soup
    html = get(url)
    soup = Soup(html)
    soup.find( "a", {"class":"card"})

```
- it will give us all the card that have class arguement

### Strict
- If we set partial=False then we don't allow elements that only match the "release__version" partially.
- If we set partial=True then we allow elements that have "release__version" as a substring. 
```python
    url= "https://pypi.org/project/pandas/#history"
    from gazpacho import get, Soup
    html = get(url)
    soup = Soup(html)
    cards = soup.find( "a", {"class":"card"})
    cards[0].find("p",{"class":"release__version"}, partial=False).text
```

### Attributes
- we can get attributes from elements using **attrs**
```python
    url= "https://pypi.org/project/pandas/#history"
    from gazpacho import get, Soup
    html = get(url)
    soup = Soup(html)
    cards = soup.find( "a", {"class":"card"})

    def parse_card(card):
        version = card.find("p", {"class":"release__version"}, partial=False).text
        timestamp = cards[0].find("time").attrs["datetime"]
        return {"version":version, "timestamp":timestamp}
    parse_card(cards[0])
```

### Pandas
- When you're scraping a website the goal is often to get the information into a pandas dataframe so that you can use it for further analysis.
```python
    import pandas as pd
    pd.Dataframe(
        [parse_card(c) for c in cards]
    ).assign(timestamp=lambda d:pd.to_datetime(d['timestamp']))
```