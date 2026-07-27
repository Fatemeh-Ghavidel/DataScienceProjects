

#%%
class DataOverallView:
    def __init__(self, data):

        """_Overal overview of data_

        Args:
            data (_pd.DataFrame_): _Initial data_
        """
        self.data = data

        
    def data_type_summary(self):

        """_Information of features_"""

        return self.data.info()


    def statical_summary(self):

        """_A brief statical information of data_"""

        print(f'\nNumericalStatistic:\n{self.data.describe()}')
        print(( f'\nCategoricalStatistic:\n {self.data.describe(include = object)}'))


    def data_null_value(self):

        """_Features with the number of their Nan values_"""

        print(f'\nNumber of NaNs:\n{self.data.isnull().sum()}')



#%%
datacheck = DataOverallView(df)
datacheck.data_type_summary()
datacheck.statical_summary()
datacheck.data_null_value()
 
# %%
