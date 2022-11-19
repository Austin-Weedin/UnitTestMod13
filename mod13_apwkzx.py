import datetime 
import unittest

class Test(unittest.TestCase):
    
    symbol = input("Enter stock symbol ")
    charType = input("enter chart type: ")
    timeSeries = input("Enter time series: ")
    startDate = input("Enter start date YYYY-MM-DD: ")
    endDate = input("Enter end date YYYY-MM-DD: ")

    def symbolTest(self):
        self.assertTrue(self.symbol.isupper())
        self.assertTrue(len(self.symbol)>=1)
        self.assertTrue(len(self.symbol)<=7)
        self.assertTrue(self.symbol.isalpha())

    def chatTest(self):
        self.assertTrue(self.charType.isnumeric())
        self.assertTrue(len(self.charType)==1)
        self.assertTrue(self.charType == "1" or self.charType == "2")

    def timeTest(self):
        self.assertTrue(self.timeSeries.isnumeric())
        self.assertTrue(len(self.timeSeries)==1)
        self.assertTrue(self.timeSeries == "1" or self.timeSeries == "2" or self.timeSeries == "3" or self.timeSeries == "4")

    def startTest(self):
        self.assertIsInstance(datetime.datetime.strptime(self.startDate, "%Y-%M-%D"),datetime.datetime,"Failed")

    def endTest(self):
        self.assertIsInstance(datetime.datetime.strptime(self.endDate, "%Y-%M-%D"),datetime.datetime,"Failed")

if __name__ == '__main__':
    unittest.main()