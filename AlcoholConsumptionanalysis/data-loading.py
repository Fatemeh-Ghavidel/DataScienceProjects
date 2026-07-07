

## -------------------------------------------------------------------------
# Class "UnzipFileOpenCSV" includes "Unzip" method and "Csvopen" mehtod.
# This Class works with File not a Directory,
# Assumption: User knows the file type: 
##       Unzip the zip file with Unzip function, then use Csvopen function to open CSV file.  
##       Open CSV file.  
# --------------------------------------------------------------------------

#%%
class UnzipFileOpenCSV:
    def Unzip(self, zip_file_path):
        """Open zip file and return all the CSV files."""
        if not os.path.isfile(zip_file_path):   # Make sure that path is for a file
            raise FileNotFoundError('Not a file exists')

        with ZipFile(zip_file_path, 'r') as ZipObj: # Open the zip file 
            ZipObj.extractall("extractedfiles")
            
        if not os.path.isdir("extractedfiles"): # Make sure target directory exists.
            raise FileNotFoundError('Not a Destination Directory')


        csv_files = [file for file  in os.listdir("extractedfiles") if file.endswith('.csv')]
        if len(csv_files) == 0:
                raise FileNotFoundError('Not a csv-file in destination')
    
        else: 
                print ('Multiple CSV files found, Please specify which one to use. ')
                return csv_files
                    ## Choose the specific csv file and call Csvopen

        
    def Csvopen(self, name):
        """Open target CSV file"""
        data = pd.read_csv( filepath_or_buffer = name)
        return data
    
    
#%% Open the zip file 
zip_file_path = "D:\Machine learning\database\student.zip"
open = UnzipFileOpenCSV()   
open.Unzip(zip_file_path)
data = open.Csvopen('extractedfiles\student-mat.csv')
data


#%% Open the CSV file
csv_path = r"csv_file_path"
open = UnzipFileOpenCSV()
data_1 = open.Csvopen(csv_path)
data_1




