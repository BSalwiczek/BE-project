import csv

if __name__ == '__main__':
    with open('../presta_combinations.csv', 'w') as outputCsv:
        writer = csv.writer(outputCsv, delimiter=';')
        writer.writerow(['Product ID', 'Attribute (Name:Type:Position)*', 'Value (Value:Position)*'])

        for i in range(400):
            writer.writerow([str(i),'Język napisów:select:0', 'Angielski:0'])
            writer.writerow([str(i),'Język napisów:select:0', 'Polski:0'])
            writer.writerow([str(i),'Język napisów:select:0', 'Niemiecki:0'])
            writer.writerow([str(i),'Język napisów:select:0', 'Hiszpański:0'])