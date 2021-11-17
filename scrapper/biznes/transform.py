import csv
import random
from ast import literal_eval

def getCategories(skills):
    resultArr = []
    categories = ['Python', 'Algorithms', 'DevOps', 'Deep Learning', 'SQL','Javascript']

    for i in categories:
        if i in skills:
            resultArr.append(i)
            break

    if len(resultArr) == 0:
        resultArr.append('Other')

    return ','.join(resultArr)

if __name__ == '__main__':
    with open('../presta_transformed.csv', 'w') as outputCsv:
        writer = csv.writer(outputCsv, delimiter=';')
        writer.writerow(
            ['ProductID', 'Image', 'Image alt', 'Name', 'Tags', 'Base price', 'Final price',
             'Description', 'Discount percent', 'Available only online', 'Virtual product', 'Cecha(Nazwa:Wartość:Pozycja:Indywidualne)', 'Categories'])
        with open('../scrapedData.csv') as inputCsv:
            reader = csv.reader(inputCsv, delimiter=';', quotechar='|')
            for i, row in enumerate(reader):
                if i == 0:
                    continue
                price = random.randint(10, 500)
                writer.writerow(
                    [str(i),
                     '/var/www/html/img/products/productImage' + str(i - 1) + '.jpg',
                     row[0],
                     row[0],
                     ','.join(literal_eval(row[-1])),
                     str(price),
                     str(price + price * 0.23),
                     row[1],
                     '0' if price > 100 else '10',
                     '1',
                     '1',
                     f'Długość kursu:{random.randint(2,50)}h:1|2',
                     getCategories(literal_eval(row[-1]))])
