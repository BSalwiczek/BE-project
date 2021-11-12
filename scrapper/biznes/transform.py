import csv
import random
from ast import literal_eval

if __name__ == '__main__':
    with open('../presta_transformed.csv', 'w') as outputCsv:
        writer = csv.writer(outputCsv, delimiter=';')
        writer.writerow(
            ['ProductID', 'Image' ,'Image alt', 'Name', 'Category', 'Base price', 'Final price', 'Quantity', 'Status',
             'Description'])
        with open('../scrapedData_copy.csv') as inputCsv:
            reader = csv.reader(inputCsv, delimiter=';')
            for i, row in enumerate(reader):
                if i == 0:
                    continue
                price = random.randint(10, 500)
                writer.writerow(
                    [str(i - 1), '/var/www/html/img/products/productImage' + str(i - 1) + '.jpg', row[0], row[0], '('+','.join(literal_eval(row[-1]))+')',
                     str(price), str(price + price * 0.23), str(10000), '0', row[1]])
