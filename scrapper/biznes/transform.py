import csv
import random
from ast import literal_eval

def getCategories(skills):
    resultArr = []
    categories = ['DevOps', 'Algorithms', 'Web Development', 'Deep Learning', 'SQL','Javascript']

    for i in categories:
        if i in skills:
            resultArr.append(i)
            break

    if len(resultArr) == 0:
        resultArr.append('Java')

    return ','.join(resultArr)

if __name__ == '__main__':
    with open('../presta_transformed.csv', 'w') as outputCsv:
        writer = csv.writer(outputCsv, delimiter=';')
        writer.writerow(
            ['ProductID', 'Image', 'Image alt', 'Name', 'Tags', 'Base price', 'Final price',
             'Description', 'Discount percent', 'Virtual product', 'Cecha(Nazwa:Wartość:Pozycja:Indywidualne)', 'Categories', 'Amount'])
        with open('../scrappedData.csv') as inputCsv:
            reader = csv.reader(inputCsv, delimiter=';', quotechar='|')
            for i, row in enumerate(reader):
                print(row)
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
                     '20' if i == 22 else if price > 100 else '10',
                     '1',
                     f'Długość kursu:{random.randint(2,50)}h:1|2',
                     getCategories(literal_eval(row[-1])),
                     '1000000',
                     ]
                )
