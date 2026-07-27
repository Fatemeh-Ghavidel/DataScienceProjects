


#%%
class Pistachio:
    def __init__(self, data: pd.DataFrame, year: int): 
        
        """
        _Initialize Pistachio data processor for a specific year._
        
        Args:
            data: DataFrame containing pistachio sales data
            year: Target year to analyze
        """
        self.data = data
        self.year = year
        # Filter data for the specified year
        self.year_mask = self.data['year'] == self.year 

        if not self.year_mask.any(): 
            raise ValueError(f"No data found for year {year}")
        
        self.year_data = self.data[self.year_mask].copy()


    def year_data_type(self, product_type: str) -> pd.DataFrame:
        
        """
        _Get data for a specific product type in the selected year._
        
        Args:
            product_type: 'W' for wet, 'D' for dry
            
        Returns:
            DataFrame filtered by type
        """
        if product_type not in ['W', 'D']: 
           raise ValueError("product_type must be 'W' or 'D'")
           
        return self.year_data[self.year_data['type'] == product_type]
    


    @property
    def Weight(self) -> pd.Series:

        """_Weights of selling product per year (Kg)_"""

        return self.year_data['amount']

    @property
    def Price(self) -> pd.Series: 

        """_Prices of selling product per year (Toman)_"""

        return self.year_data['price']


    @property
    def Type(self) -> pd.Series:

        """_Types of selling products per year_"""

        return self.year_data['type']
    




class SoldProduct(Pistachio):

    """_Calculate aggregated values based on product type._"""
    
    def total_weight_type(self, product_type:str) -> float:

        """
        _Total selling weight for a specific product type._
        
        Args:
            _product_type: 'W' for wet, 'D' for dry_
            
        Returns:
            _Total weight in Kg_
        """

        type_data = self.year_data[self.year_data['type'] == product_type ]
        return float(type_data['amount'].sum())


    def total_weight(self) -> float:
        
        """
        _Total selling weight with weighting logic._
        
        Note: _Dry products are weighted 3x in calculation._
        Formula: _(D_weight * 3) + W_weight_
        
        Returns:
            _Adjusted total weight_
        """

        return self.total_weight_type('D') * 3 + + self.total_weight_type('W')

    
    def total_price_type(self, product_type: str) -> float:
        
        """
        _Total price for a specific product type._
        
        Args:
            _product_type: 'W' for wet, 'D' for dry_
            
        Returns:
            _Total price in Toman_
        """

        type_data = self.year_data[self.year_data['type'] == product_type]
        return float(type_data['price'].sum())
    

    def total_price(self): 
        
        """
        _Total price for product._
        
        Args:
            product_type: _'W' for wet, 'D' for dry_
            
        Returns:
            _Total price in Toman_
        """

        return self.total_price_type('W') + self.total_price_type('D')


    def summary(self) -> dict:

        """
        Generate summary statistics for the year.
        
        Returns:
            Dictionary with weight and price summaries
        """

        return {
            'year': self.year,
            'total_weight_wet': self.total_weight_type('W'),
            
            'total_weight_dry': self.total_weight_type('D'),
            'adjusted_total_weight': self.total_weight(),
            'total_price_wet': self.total_price_type('W'),
            'total_price_dry': self.total_price_type('D'),
            'total_price': self.total_price()
        }


#%%
pistachio = SoldProduct(df, year=1404)
print(pistachio.summary())


#%%
