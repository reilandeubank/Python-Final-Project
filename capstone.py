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
    def remove_duplicates(self, df):
        return df.drop_duplicates(subset=['Name'], keep='first')
    def print_menu(self):
        print()
        print("Please select an option from the menu below:")
        print("Option 1: Show the top 20 Raw lifters by Dots")
        print("Option 2: Show the top 20 Raw + Wraps totals by age")
        print("Option 3: Show graph comparing totals of Raw, Raw + Wraps, Single-ply, and Multi-ply lifters")
        print("Option 4: Show graph comparing totals with age")
        choice = input("\nWhich option would you like to select? (1 through 4, or 0 to quit): ")
        print("\n")
        self.execute_menu(choice)
    def execute_menu(self, choice):
        if choice == "1":                                   #Works 
            print("\n")
            raw = self.sbd[self.sbd['Equipment'] == 'Raw']
            sorted_raw_lifters = raw.sort_values(by=['Dots'], ascending = False)[:500]
            print(self.remove_duplicates(sorted_raw_lifters)[:20])
        elif choice == "2":                                 #Works
            age = input("What age would you like to see the top 20 lifters for? ")
            print("\n")
            raw_wraps = self.sbd[(self.sbd['Equipment'] == 'Wraps')]
            age_lifters = raw_wraps[raw_wraps['Age'] == int(age)]
            sorted = age_lifters.sort_values(by=['TotalKg'], ascending = False)
            print(self.remove_duplicates(sorted)[:20])
        elif choice == "3":                                 # Works
            equip_choices = ["Raw", "Wraps", "Single-ply", "Multi-ply"]
            data = []
            for i in range(4):
                equip = self.sbd[self.sbd['Equipment'] == equip_choices[i]]
                random = equip.sample(frac=0.1)
                equip = random.dropna(subset=['TotalKg'])
                equip = self.remove_duplicates(equip)[:10000]
                data.append(equip['TotalKg'])
            fig = plt.figure(figsize =(10, 7))
            ax = fig.add_axes([0, 0, 1, 1])
            ax.set_xlabel('X Label')
            ax.set_ylabel('Y Label')
            ax.boxplot(data)
            plt.show()
        elif choice == "4":                                # Works kind of
            random = self.sbd.sample(n=3000)
            truncated = self.remove_duplicates(random)[:2000]      
            plt.scatter(x = truncated['Age'], y = truncated['TotalKg'])
            plt.show()
        if choice == "0":
            print("Thank you for using the data analysis program!")
        else:
            self.print_menu()


myData = data_analysis()
print("Welcome to the data analysis program!")
myData.print_menu()
