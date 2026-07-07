


#%%
class DataVisualization: 
 
    """Overall Data Visualization"""
    def __init__(self, data):
        self.data = data

    def nRows(self, cols):
        return math.ceil(len(cols) / 3)


    def DataDistVis(self):
        """Plotting distribution of data based on datatype."""

        cat_cols = self.data.select_dtypes(include=['object', 'category']).columns.tolist()
        num_cols = self.data.select_dtypes(include=['number']).columns.tolist()
        
        configs = [
            {'cols': cat_cols, 'type': 'categorical', 'kde': False},
            {'cols': num_cols, 'type': 'numerical', 'kde': True}
        ]
        
        for config in configs:
            cols = config['cols']
            if not cols:  
                continue
                
            nrows = self.nRows(cols)
            fig, axes = plt.subplots(nrows=nrows, ncols=3, figsize=(15, 25))
            
            
            if nrows == 1:
                axes = axes.reshape(-1)
            else:
                axes = axes.flatten()
            
            # Plot each column
            for i, col_name in enumerate(cols):
                sns.histplot(data=self.data, x=col_name, ax=axes[i], kde=config['kde'], color="#A0DE7C")
                axes[i].set_title(f"Dist of {col_name}")
            
            
            for j in range(len(cols), len(axes)):
                fig.delaxes(axes[j])
                
            plt.suptitle(f"Distribution of {config['type']} features", fontsize=20, fontweight='bold', y=1.02)
            plt.tight_layout()
            plt.show()





    def BoxPlot(self, ):
        # """Plotting features with number of values between 2 and 6"""

        cols = [i for i in self.data.columns if 2 < self.data[i].nunique() < 6]
        
        if not cols:
            print("No columns found with 2 to 6 unique values.")
            return

        nrows = self.nRows(cols)
        fig, axes = plt.subplots(nrows=nrows, ncols=3, figsize=(15, 20))
        
        
        if nrows == 1:
            axes = np.atleast_1d(axes).flatten()
        else:
            axes = axes.flatten()
            
        
        for i, col_name in enumerate(cols):
            sns.boxplot(data=self.data[col_name], ax=axes[i], color="#A5E3B4")
            axes[i].set_title(f"Boxplot of {col_name}")
        
    
        for j in range(len(cols), len(axes)):
            fig.delaxes(axes[j])
            
        plt.suptitle(f"Boxplots of features with 2 to 6 unique values.", 
                     fontsize=20, fontweight="bold", y=1.02)
        plt.tight_layout()
        plt.show()





    
    def HeatmapNumerical(self):
        """Heatmap for numerical data"""
        
        num_data = self.data.select_dtypes(include=['number'])
        
        if num_data.empty:
            print("No numerical columns found to correlate.")
            return
            
        cm = num_data.corr()

        plt.figure(figsize = (12 ,10))
        mask = (cm > -0.25) & (cm < 0.25)
        sns.heatmap(
                cm ,
                mask = mask ,
                annot = True,
                cmap = 'PRGn',
                fmt ='.2f' , 
                vmin = -1 , vmax =  1, 
                square = True, 
                cbar_kws={"shrink": .8} ), 
        

        plt.tight_layout()
        plt.title('Numerical Features Heatmap (|r| > 0.25)', fontsize=16, fontweight='bold')
        
        
        

    
#%%
plot = DataVisualization(data)
plot.DataDistVis()
plot.BoxPlot()
plot.HeatmapNumerical()




 #%%
class AlcoholConsumption:
    def __init__(self, data): 
        """_Compare daily and weakly consumption  of alcohol feature_"""
        self.data = data
        
    def pieplotWalcDalc(self,alcohol_cons):
        """_Distribution of classes in daily and weakly alcohol consumption_"""
        for col, time in zip(alcohol_cons, ['Weekly', 'Daily']):
            value_count = data[col].value_counts()
            labels = value_count.index
            sizes = value_count.values
            fig, ax  = plt.subplots()
            colors = sns.light_palette("seagreen")
            wedges, texts, autotexts = ax.pie(
                sizes,
                labels = labels ,
                colors = colors ,
                startangle = 90,
                autopct = '%.0f%%',
                wedgeprops = dict(width = 0.5))
            ax.legend(wedges, labels, title ='Classes', loc = 'center left' , bbox_to_anchor = (1,0, 0.5, 1))
            plt.title(f'{time} Alcohol Consumption')
    
    
    def distplotWalcDalc(self):
        """_Distribution of Walc and Dalc features_"""
        palette = sns.dark_palette('#83c478')
        sns.displot(self.data , x = 'Walc', hue = 'Dalc', kind = 'kde' , palette = palette)
        plt.grid()
        
    def WalcDalcCorr(self): 
        """_Correlation between Walc and Dalc feartures_"""
        sns.catplot(self.data, x = 'Walc', y = 'Dalc', kind = 'point', color = '#2B8046')
        plt.grid()
        
        
        
            
AlcoholConsumption(data).pieplotWalcDalc(['Walc', 'Dalc']) 
AlcoholConsumption(data).distplotWalcDalc()
AlcoholConsumption(data).WalcDalcCorr()  




# %%

