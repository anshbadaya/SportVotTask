from django.shortcuts import render
import urllib.request
from bs4 import BeautifulSoup


# Create your views here.
def page_View(request):
    # Providing url
    url = "https://air-quality.com/place/india/gurugram/d2853e61?lang=en&standard=aqi_us"

    # Opening the url for reading
    html = urllib.request.urlopen(url)

    # Parsing the html file
    htmlParse = BeautifulSoup(html, 'html.parser')

    # Targeting the pollutants
    pollutants = htmlParse.find_all(class_="pollutants")

    # Getting all the needed data
    for pollutant in pollutants:
        raw_title_list = pollutant.find_all(class_="name")
        raw_value_list = pollutant.find_all(class_="value")

    # Extracting and combining data
    data_list = {}

    title_list = [title.text for title in raw_title_list]
    value_list = [value.text for value in raw_value_list]

    for index in range(len(title_list) or len(value_list)):
        data_list[title_list[index]] = value_list[index]
    print(data_list)
    return render(request, 'base_page.html', {'data_list': data_list})
