import csv
from ast import literal_eval

if __name__ == '__main__':
    with open('../presta_combinations.csv', 'w') as outputCsv:
        writer = csv.writer(outputCsv, delimiter=';')
        writer.writerow(['Product ID', 'Attribute (Name:Type:Position)*', 'Value (Value:Position)*'])

        with open('../scrapedData.csv') as scrapedCsv:
            reader = csv.reader(scrapedCsv, delimiter=';', quotechar='|')
            for i, row in enumerate(reader):
                if i == 0:
                    continue
                subtitleLangs = literal_eval(row[3])
                if len(subtitleLangs) == 0:
                    writer.writerow([str(i-1),'Język napisów:select:0', f'Brak:0'])
                for lang in subtitleLangs:
                    writer.writerow([str(i-1),'Język napisów:select:0', f'{lang}:0'])