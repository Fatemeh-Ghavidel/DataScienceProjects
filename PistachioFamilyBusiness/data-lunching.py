

#%%
class LaunchData: 
    def __init__(self, path: str) -> None:

        """_Extract data from the path_ """

        self.path = path
       
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"Path does not exist: {self.path}")
    
    def extract_file(self) -> pd.DataFrame: 

        """_Identify type of the file and call other child classes to open the file._"""
        
        if os.path.isdir(self.path):
            return OpenDirectory.open_dir(self.path)   
        elif self.path.endswith('.zip'): 
            return OpenFile.open_zipfile(self.path)
        elif self.path.endswith('.csv'): 
            return  pd.read_csv(self.path)
        else: 
            raise ValueError(f"Unsupported file type: {self.path}")
                


 
class OpenFile:  

    """_Extract data from the zip file_"""

    @staticmethod       
    def open_zipfile(path):

        """_Open the zip file and find the csv file_
        Raises:
            FileNotFoundError: _No csv file in the zip file_
            ValueError: _multiple csv files in the zip file_
        """

        with zf(path, mode='r') as to_zipfile: 
            to_zipfile.extractall(path="extracted_files")
            
        extracted_files = os.listdir(path="extracted_files")
        
        csv_files = [file for file in extracted_files if file.endswith('.csv')]
             
        if not csv_files: 
            raise FileNotFoundError('No CSV file found in extracted file.') 
        if len(csv_files) > 1:
            print(csv_files)
            raise ValueError('Multiple CSV files found, Please specify which one to use.')
        return pd.read_csv(os.path.join('extracted_files', csv_files[0]))
                  
            
                       
            
class OpenDirectory:

    """_Read data from the directory_""" 

    @staticmethod 
    def open_dir(path): 
       
       """_Open directory and find file_"""

       files = os.listdir(path)
       print('Multiple files in this directory!!')
       print(files) 
       file = input('Please specify which one to use:')
       return LaunchData(os.path.join(path, file)).extract_file()

    
           
               
#%%          
data  = LaunchData(path)
df = data.extract_file()  
df



# %%
# In general User gives the path -> LuanchData processes the path itself and launches the data provided in CSV file 

# LunchData -> take the path -> 'Extract_file method' digest the type of the path (directory or file) and call other classes wtih their methods. 

    # OpenDirectory -> opens the directory -> returns files -> user adds specific target CSV file at the end of the path and call LunchData again. 

    # OpenFile -> unzip the zipfile  
        # 1 CSV file -> open it 
        # 0 Error 
        # More than 1 -> ValueError
    
