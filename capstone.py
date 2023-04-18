import pandas as pd
from matplotlib import pyplot as plt


class data_analysis:
    def __init__ (self):
        print("importing files...")
        open_pl = pd.read_csv("openpowerlifting.csv", low_memory=False)
        # valid_date = open_pl['Date'].notnull()
        # valid_date = valid_date[valid_date['Date'] != ""]
        since_2015 = open_pl[open_pl['Date'] >="2015-01-01"]
        neater_data = since_2015[['Name', "Sex", "Event", "Equipment", "Age", 
                               "Division", "WeightClassKg", "TotalKg", "Dots", 
                               "Tested", "Date"]]
        self.sbd = neater_data[neater_data['Event'] == 'SBD']
        self.sbd = self.sbd[['Name', "Sex", "Equipment", "Age", 
                               "Division", "WeightClassKg", "TotalKg", "Dots", 
                               "Tested", "Date"]]
    def print_menu(self):
        print("\n")
        print("Please select an option from the menu below:")
        print("Option 1: Show the top 20 lifters in the SBD event")
        print("Option 2: Show the top 20 lifters in the SBD event by age")
        print("Option 3: Show graph comparing equipped and raw lifters")
        print("Option 4: Show graph comparing totals with age")
        choice = input("Which option would you like to select? (1 through 4, or 0 to quit): ")
        print("\n")
        self.execute_menu(choice)
    def execute_menu(self, choice):
        if choice == "1":
            print("\n")
            print(self.sbd.sort_values(by=['TotalKg'])[:20])
        if choice == "2":
            age = input("What age would you like to see the top 20 lifters for? ")
            print("\n")
            age_lifters = self.sbd[self.sbd['Age'] == int(age)]
            print(self.sbd.sort_values(by=['TotalKg'])[:20])
        if choice == "3":
            plt.plot(self.sbd['Equipment'], self.sbd['TotalKg'])
            plt.show()
        if choice == "4":
            plt.plot(self.sbd['Age'], self.sbd['TotalKg'])
            plt.show()
        if choice == "0":
            print("Thank you for using the data analysis program!")
        else:
            print("Please enter a valid choice (1 through 4, or 0 to quit)")
            self.print_menu()


myData = data_analysis()
print("Welcome to the data analysis program!")
myData.print_menu()
