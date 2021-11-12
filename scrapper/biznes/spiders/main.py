import csv
import json
import re
import urllib

import scrapy

j = 0
numberOfPagesGlobal = 0
numberOfProducts = 0
page = 0
names = []
names.append('name')
descriptions = []
productUrls = []
descriptions.append('description')
isPartOfCourseraPluses = []
isPartOfCourseraPluses.append('isPartOfCourseraPlus')
subtitleLanguages = []
subtitleLanguages.append('subtitleLanguages')
productDifficultyLevels = []
productDifficultyLevels.append('productDifficultyLevels')
audiences = []
audiences.append('audiences')
enrollments = []
enrollments.append('enrollments')
partners = []
partners.append('partners')
languages = []
languages.append('languages')
numProductRatings = []
numProductRatings.append('numProductRatings')
allLanguageCodes = []
allLanguageCodes.append('allLanguageCodes')
avgProductRatings = []
avgProductRatings.append('avgProductRatings')
skills = []
skills.append('skills')

class CourseraSpider(scrapy.Spider):
    name = "coursera"

    def start_requests(self):
        url = 'https://www.coursera.org/search?query=python&index=prod_all_launched_products_term_optimization'
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        global numberOfProducts
        if numberOfProducts == 0:
            global page
            if page == 0:
                numberOfPages = response.css('h2.rc-NumberOfResultsSection span::text').get()
                numberOfPages = re.findall(r'\d+', numberOfPages)[0]
                numberOfPages = int(numberOfPages)
                if numberOfPages % 10 != 0:
                    numberOfPages = numberOfPages + 10 - (numberOfPages % 10)
                numberOfPages = int(numberOfPages / 10)
                global numberOfPagesGlobal
                numberOfPagesGlobal = numberOfPages
            data_set = response.css('script#__NEXT_DATA__::text').get()
            json_object = json.loads(data_set)
            json_object = json_object['props']['pageProps']['resultsState'][2]['content']['_rawResults'][0]['hits']
            for i in json_object:
                if i['entityType']=='COURSE':
                    names.append(i['name'])
                    productUrl = 'https://www.coursera.org'
                    productUrl += i['objectUrl']
                    productUrls.append(productUrl)
                    global j
                    # urllib.request.urlretrieve(i['imageUrl'], "productImage" + str(j) + ".jpg")
                    j += 1

                    isPartOfCourseraPluses.append(i['isPartOfCourseraPlus'])
                    subtitleLanguages.append(i['subtitleLanguage'])
                    productDifficultyLevels.append(i['productDifficultyLevel'])
                    audiences.append(i['audience'])
                    enrollments.append(i['enrollments'])
                    partners.append(i['partners'])
                    languages.append(i['language'])
                    numProductRatings.append(i['numProductRatings'])
                    allLanguageCodes.append(i['allLanguageCodes'])
                    avgProductRatings.append(i['avgProductRating'])
                    skills.append(i['skills'])

            page = page + 1

        else:

            description = response.css('div.content-inner *::text').get()
            descriptions.append(description)

        if page < numberOfPagesGlobal:
            url = 'https://www.coursera.org/search?query=python&page=' + str(
                page + 1) + '&index=prod_all_launched_products_term_optimization'
            yield response.follow(url, self.parse)
        elif numberOfProducts<j:
            url = productUrls[numberOfProducts]
            numberOfProducts += 1
            yield response.follow(url, self.parse)
        else:
            print(len(names))
            with open('scrapedData.csv', 'w', newline='', encoding="utf-8") as csvfile:
                ProductWriter = csv.writer(csvfile, delimiter=';',
                                           quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for i in range(len(names)):
                    ProductWriter.writerow([names[i],
                                            descriptions[i],
                                            isPartOfCourseraPluses[i],
                                            subtitleLanguages[i],
                                            productDifficultyLevels[i],
                                            audiences[i],
                                            enrollments[i],
                                            partners[i],
                                            languages[i],
                                            numProductRatings[i],
                                            allLanguageCodes[i],
                                            avgProductRatings[i],
                                            skills[i]
                                            ])