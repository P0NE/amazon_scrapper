import csv


class Check:

    def __init__(self, mail, url, price):
        self.url = url
        self.price = price
        self.mail = mail
        # persit into database but for now in csv file
        with open('check.csv', 'a') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow([self.mail, self.url, self.price])
