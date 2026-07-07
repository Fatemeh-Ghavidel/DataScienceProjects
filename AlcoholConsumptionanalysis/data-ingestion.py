

#%%
class DataIngestion:
    def __init__(self, data):
        """_Data overview_

        Args:
            data (_pd.DataFrame_): _Initial data_
        """
        self.data = data
        
    def DataTypeSummary(self):
        """_Overall Information of data_"""
        
        return self.data.info()


    def StaticalSummary(self):
        """_A brief statical information of data_"""
        
        print(f'\nNumericalStatistic:\n{self.data.describe()}')
        print(( f'\nCategoricalStatistic:\n {self.data.describe(include = object)}'))


    def DataNullValue(self):
        """_The number of Nan values for each feature_
        
        Returns:
            _pd.core.series.Series_: _A table of features and the numbe
            
            r of Nan values'_
        """
        print(f'\nNumber of NaNs:\n{self.data.isnull().sum()}')




datacheck = DataIngestion(data)
datacheck.DataTypeSummary()
datacheck.StaticalSummary()
datacheck.DataNullValue()
 
#%%
