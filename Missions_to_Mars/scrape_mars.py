# Dependencies
from bs4 import BeautifulSoup
import requests

def scrape_info():

    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'

    # Retrieve page with the requests module
    response = requests.get(url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')

    # Examine the results, then determine element that contains sought info
    print(soup.prettify())

    # Extract title text
    news_title = soup.find_all('div', class_='content_title')[0].text
    print(news_title)

    # Extract paragraph texts
    news_p = soup.find_all('div', class_='rollover_description_inner')[0].text
    print(news_p)

    from splinter import Browser
    # from bs4 import BeautifulSoup
    from webdriver_manager.chrome import ChromeDriverManager

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://www.jpl.nasa.gov/spaceimages/'
    browser.visit(url)

    featured_image = soup.find_all('article')

    print(featured_image)

    featured_image_url = url + "images/wallpaper/PIA22911-1920x1200.jpg"
    print(featured_image_url)

    import pandas as pd

    url = 'https://space-facts.com/mars/'

    tables = pd.read_html(url)
    tables

    df = tables[0]
    df.head(20)

    df.columns = ['Measure', 'Result']
    df.head(20)

    df.to_html('mars_facts.html')

    # Scrape for Image #1

    # URL of page to be scraped (Page 1)
    url1 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'

    # Retrieve page with the requests module
    response = requests.get(url1)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')

    # Examine the results, then determine element that contains sought info
    print(soup.prettify())

    result1 = soup.find('div', class_='content')
    link1 = result1.a['href']
    print (link1)

    result1 = soup.find('div', class_='content')
    title1 = result1.h2.text
    print(title1)

    # Scrape for Image 2

    # URL of page to be scraped (Page 2)
    url2 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'

    # Retrieve page with the requests module
    response = requests.get(url2)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')

    result2 = soup.find('div', class_='content')
    link2 = result2.a['href']
    print (link2)

    result2 = soup.find('div', class_='content')
    title2 = result2.h2.text
    print(title2)

    # Scrape for Image 3

    # URL of page to be scraped (Page 3)
    url3 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'

    # Retrieve page with the requests module
    response = requests.get(url3)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')

    result3 = soup.find('div', class_='content')
    link3 = result3.a['href']
    print (link3)

    result3 = soup.find('div', class_='content')
    title3 = result3.h2.text
    print(title3)

    # Scrape for Image 4

    # URL of page to be scraped (Page 4)
    url4 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'

    # Retrieve page with the requests module
    response = requests.get(url4)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')

    result4 = soup.find('div', class_='content')
    link4 = result4.a['href']
    print (link4)

    result4 = soup.find('div', class_='content')
    title4 = result4.h2.text
    print(title4)

    my_dict = {title1:link1, title2:link2, title3:link3, title4:link4}
    my_series = pd.Series(my_dict)
    my_series

    hemi_df = my_series
    hemi_df.head()

    from pandas import DataFrame

    hemi_df = DataFrame (my_series,columns=['img_url'])
    print (hemi_df)

    return {
        "news_title": news_title ,
        "news_paragraph": news_p,
        "featured_image_url": featured_image_url,
        "my_series": my_series
    }

