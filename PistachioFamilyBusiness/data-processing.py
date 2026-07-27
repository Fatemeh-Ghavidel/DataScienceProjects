
#%%
class DataProcessing: 

    """_Deal with Nan Values and Convert the type of data features_"""

    def convert_to_nan(self, data) -> pd.DataFrame: 

        """_Remove '?' and replace with NaN value_

        Args:

            data:(_pd.DataFrame_): _Dataset_

        """
        df = data.replace('?', np.nan)
        return df


    def convert_data_type(self, df) -> pd.DataFrame:

        """_Change the data type of features_"""

        df = self.convert_to_nan(df)
        df['amount'] = df['amount'].astype('float64')
        df['year'] = df['year'].astype('object') 
        return df



#%%
processing = DataProcessing()
df = processing.convert_to_nan(df)
df = processing.convert_data_type(df)




# %%
