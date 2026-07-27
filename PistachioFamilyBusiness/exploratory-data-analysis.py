



# ==============================  ==========================  ==============================
#                               ||Product Metrics Calculation||
# ==============================  ==========================  ==============================


#%%
## Weight, Price and Type of product for each year
##------------------------------------------------------------------------------------------

first_year_amount = Pistachio(df, 1402).Weight
second_year_amount =Pistachio(df, 1403).Weight
third_year_amount = Pistachio(df, 1404).Weight


first_year_price = Pistachio(df, 1402).Price

second_year_price = Pistachio(df, 1403).Price
third_year_price = Pistachio(df, 1404).Price


first_year_type = Pistachio(df, 1402).Type
second_year_type = Pistachio(df, 1403).Type
third_year_type = Pistachio(df, 1404).Type


## Subset of dataset for each type of product (per year)
##------------------------------------------------------------------------------------------
first_year_data_w = Pistachio(df , 1402).year_data_type('W')
first_year_data_d = Pistachio(df , 1402).year_data_type('D')

second_year_data_w = Pistachio(df , 1403).year_data_type('W')
second_year_data_d = Pistachio(df , 1403).year_data_type('D')

third_year_data_w = Pistachio(df , 1404).year_data_type('W')
third_year_data_d = Pistachio(df , 1404).year_data_type('D')


## Subset of dataset (per year)
##------------------------------------------------------------------------------------------
first_year_data = pd.concat([first_year_data_w ,first_year_data_d])
second_year_data = pd.concat([second_year_data_w ,second_year_data_d])
third_year_data = pd.concat([third_year_data_w ,third_year_data_d])







# ==============================  ==========================  ==============================
#                               ||Exploratory Data Analysis||
# ==============================  ==========================  ==============================


##------------------------------------------------------------------------------------------
##                                   1.Distribution Analysis
##------------------------------------------------------------------------------------------

        ## Distribution of selling weights for each type of product per year
        ##-----------------------------------------------------------------------------------
#%%
year_amount = [[first_year_data_w['amount'], first_year_data_d['amount']],
               [second_year_data_w['amount'], second_year_data_d['amount']],
               [third_year_data_w['amount'], third_year_data_d['amount']],]


def selling_weight_dist(year_amount):

    """_Distribution of selling weights for each type of product per year_""" 

    fig , axe= plt.subplots(nrows = 1, ncols = 3, figsize  = (10,4))
    axe = axe.flatten()
    for year, ax, num in zip(year_amount, axe, ['1st', '2nd', '3rd']):
        sns.distplot(year[0], color='seagreen', ax=ax)
        sns.distplot(year[1], color = 'olive', ax =ax)  
        ax.set_title(f'Distribution of Selling Weight (Kg)\n {num}_Year ')
        plt.tight_layout()
        ax.legend(['Wet', 'Dry'], title = 'Product Type')
        ax.set_xlabel('Weight')
        ax.grid(True, alpha=0.7, linestyle='--')

selling_weight_dist(year_amount)




        ## Scatter plot for Price based on weight for each type of product 
        ##-----------------------------------------------------------------------------------
#%%
Amount = [first_year_amount, second_year_amount, third_year_amount]
Price = [first_year_price, second_year_price, third_year_price]
Types = [first_year_type, second_year_type, third_year_type]

def price_weight_type_corr(Amount, Price, Types):

    """_Plotting weight based on price for each type of the product per year_"""

    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(30 , 10))
    
    for axe, weight, price, Type, year in zip(axes, Amount, Price, Types, ['1st', '2nd', '3rd']):
        sns.scatterplot(x=weight, y=price, hue=Type, palette=palette, s=100, ax=axe)
        
        axe.set_title(f'{year}_Year')
        axe.set_xlabel('Weight')
        axe.set_ylabel('Price')
        axe.legend(title='Product Type', bbox_to_anchor=(0.3, 0.95))
 
    plt.tight_layout()
    plt.show()

price_weight_type_corr(Amount, Price, Types)




        ## Barplot for Weight of each Type of the product per year 
        ##-----------------------------------------------------------------------------------
#%%
c1 = SoldProduct(df, 1402)
total_first_year_amount_w = c1.total_weight_type('W') 
total_first_year_amount_d = c1.total_weight_type('D')

c2 = SoldProduct(df, 1403)
total_second_year_amount_w = c2.total_weight_type('W') 
total_second_year_amount_d = c2.total_weight_type('D')

c3 = SoldProduct(df, 1404)
total_third_year_amount_w = c3.total_weight_type('W') 
total_third_year_amount_d = c3.total_weight_type('D')


Data_amount = pd.DataFrame({'1402':[total_first_year_amount_w, total_first_year_amount_d], 
                            '1403':[total_second_year_amount_w, total_second_year_amount_d],
                            '1404':[total_third_year_amount_w, total_third_year_amount_d]},
                             index = ['W', 'D'])

def selling_weight_type_barplot(Data_amount):

    """_Plotting total selling weight based on the product type for each year_"""    

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    for idx ,year in enumerate(['1402', '1403', '1404']): 
        a = sns.barplot(x=Data_amount.index, y=Data_amount[year], palette = palette,  ax=axes[idx] )
        for p in a.patches: 
            width = p.get_width()
            height = p.get_height()
            x, y  = p.get_xy()
            a.annotate(f'{height/(Data_amount[year].values[0]+Data_amount[year].values[1])*100:.2f}%', (x + width/2, y + height*1.02), ha='center') 
        axes[idx].set_title(f'Year {year}')
        axes[idx].set_xlabel('type')

    plt.suptitle('Selling Based on the Type of the Product')
    plt.show() 

selling_weight_type_barplot(Data_amount)









##------------------------------------------------------------------------------------------
##                                   2.Categorical Features Visualization
##------------------------------------------------------------------------------------------


        ## Pie plot for Categorical data (Selling and Paying)
        ##-----------------------------------------------------------------------------------
#%%
def feature_pie_plot(year_data, feature, year, ax = None, class_names = None):
    """_pie plot for selling and paying features_

    Args:
        year_data (_pd.Dataframe_): _All data for a year_
        feature (str): _selling-paying_
        year (int): _1402-1403-1404_
    """
    value_count = year_data[feature].value_counts() 
    sizes = value_count.values

    if class_names:
        labels = class_names
    else: 
        labels = value_count.index  
    
    colors = sns.light_palette("seagreen")
    ax.pie(
            sizes,
            colors = colors,
            shadow = True,
            #explode = [0.07, 0.1, 0.1],
            startangle = 90,
            autopct = '%.0f%%',
            wedgeprops = dict(width = 0.5), 
            )
    
    ax.set_title(f'{feature} type {year}')
    return labels
    
    

def Paying_type_pie_plot():
    fig, axe = plt.subplots(nrows = 1 , ncols = 3)
    axe = axe.flatten()
    class_names = ['Card', 'Cash', 'Item']  
    for i , (data, year) in enumerate(zip([first_year_data, second_year_data, third_year_data ], [1402, 1403, 1404])):
                labels = feature_pie_plot(year_data = data, 
                                          feature = 'paying ',
                                          year = year,
                                          ax =  axe[i], 
                                          class_names = class_names ) 
    plt.tight_layout()  
    fig.legend(labels , title ='Payment Methods', loc = 'center left' , bbox_to_anchor = (1,0, 0.5, 1))  


def Selling_type_pie_plot():
    fig, axe = plt.subplots(nrows = 1 , ncols = 3)
    axe = axe.flatten()
    class_names = ['Online', 'Relative', 'In_person']  
    for i , (data, year) in enumerate(zip([first_year_data, second_year_data, third_year_data ], [1402, 1403, 1404])):
                labels = feature_pie_plot(year_data = data, 
                                          feature = 'selling',
                                          year = year,
                                          ax =  axe[i], 
                                          class_names = class_names ) 
    plt.tight_layout()  
    fig.legend(labels , title ='Selling Methods', loc = 'center left' , bbox_to_anchor = (1,0, 0.5, 1))  

Paying_type_pie_plot()
Selling_type_pie_plot()





        ## Catplot for correlation between type of selling and other features
        ##-----------------------------------------------------------------------------------
#%%
def selling_catplot(data, 
                    feature, 
                    x_label, 
                    y_label,
                    year_name, 
                    class_names = None, 
                    ax = None): 
    
    """_Plotting one feature(amount or price) and type of the product based on the selling type with the data of one year_"""

    class_names = {'I':'Internet',
                   'T':'Relative', 
                   'R':'In_person'}
    
    data_new = data.copy()
    data_new['selling'] = data_new['selling'].map(class_names)
    
    g = sns.catplot(data_new, 
                    x='type',
                    y=feature, 
                    hue='selling', 
                    palette=palette,
                    height=6,
                    aspect=1.5,
                    alpha=0.9,
                    s=100,
                    edgecolor='black',
                    linewidth=0.5,
                    legend = True, 
                    ax = ax)
    
    ax = g.ax
    g.legend.set_title('Selling Method' )
    g.legend.set_bbox_to_anchor((0.85, 0.9))

    ## Enhance labels and title
    ax.set_xlabel(x_label, fontsize=14, )
    ax.set_ylabel(y_label, fontsize=14,)
    ax.set_title(f'{year_name}', fontsize=16, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.7, linestyle='--')
    
    return g
selling_catplot(first_year_data, feature='amount', x_label ='Type', y_label = 'Weight', year_name='1st Year')    


# selling_catplot(first_year_data, 'type', 'price',  x_label ='Type', y_label = 'Price', year_name='1st Year')    




        ## Scatter plot average price for each weight 
        ##-----------------------------------------------------------------------------------   
#%%
def weight_price_average(year_data,  year, 
                         color_dict={'W': 'olive', 'D': 'seagreen'},
                         axe = None):
    
    all_weights = sorted(year_data['amount'].unique())

    for type, color in color_dict.items():
        type_data = year_data[year_data['type'] == type]
        weight_price_type = type_data.groupby('amount')['price'].mean().sort_index()
        axe.scatter(weight_price_type.index,
                    weight_price_type.values,  
                    alpha=0.7,
                    s=100,
                    edgecolor='black',
                    c=color, 
                    label = type, 
                    )
        
    axe.set_xlabel('Weight')
    axe.set_ylabel('Price')
    axe.set_title(f'Average Price for weight in year {year}')
    axe.legend(title = 'Production Type')
    axe.grid(True, alpha=0.3)
    axe.set_xticklabels(all_weights, rotation=45)  # Rotate if many values

        



year_data = [first_year_data, second_year_data, third_year_data ]
years  = ['1402', '1403', '1404']

fig , axe = plt.subplots(nrows = 1, ncols = 3, figsize = (20, 8))
axe = axe.flatten()
for i , data , year in zip(axe ,year_data, years):
    weight_price_average(data, year, axe = i)


 










##------------------------------------------------------------------------------------------
##                                   3. Date & Time Analysis
##------------------------------------------------------------------------------------------

        ## Daily sales comparison for Price and Weight
        ##-----------------------------------------------------------------------------------
#%%
def datedistribution_comparison(year_data_w, year_data_d, year_name, feature, x_label):
    """Plot time series comparison of W and D products"""
    
    year_data_w = year_data_w.dropna(subset=['date', 'amount'])
    year_data_d = year_data_d.dropna(subset=['date', 'amount'])
    
    # Convert dates
    year_data_w['dates'] = pd.to_datetime(year_data_w['date'] , 
                                          format='%m/%d/%Y')
    year_data_d['dates'] = pd.to_datetime(year_data_d['date'], 
                                          format='%m/%d/%Y')
    
    # Group by date and sum amounts
    w_daily = year_data_w.groupby('dates')[feature].sum()
    d_daily = year_data_d.groupby('dates')[feature].sum()
    
    # Create figure
    fig, ax = plt.subplots(figsize=(14, 6))
    
    # Plot time series lines
    ax.plot(w_daily.index, w_daily.values, 
            marker='o', linewidth=2, markersize=8,
            color='olive', label='Wet (W)', alpha=0.8)
    
    ax.plot(d_daily.index, d_daily.values, 
            marker='s', linewidth=2, markersize=8,
            color='seagreen', label='Dry (D)', alpha=0.8)
    
    # Fill area under lines
    ax.fill_between(w_daily.index, w_daily.values, alpha=0.1, color='olive')
    ax.fill_between(d_daily.index, d_daily.values, alpha=0.1, color='seagreen')
    
    # Format x-axis
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d\n%b'))
    
    # Styling
    ax.set_xlabel('Date', fontsize=12, fontweight='bold')
    ax.set_ylabel(x_label, fontsize=12, fontweight='bold')
    ax.set_title(f'Daily Sales Comparison - {year_name} Year', 
                 fontsize=14, fontweight='bold')
    ax.legend(title='Product Type', fontsize=10, frameon=True, shadow=True)
    ax.grid(True, alpha=0.3, linestyle='--')
    
    plt.setp(ax.get_xticklabels(), rotation=45, ha='center')
    plt.tight_layout()
    plt.show()

datedistribution_comparison(second_year_data_w, second_year_data_d, '2nd', feature = 'price', x_label = 'Total Price')
datedistribution_comparison(third_year_data_w, third_year_data_d, '3rd', feature = 'price', x_label = 'Total Price')

datedistribution_comparison(second_year_data_w, second_year_data_d, '2nd', feature = 'amount', x_label = 'Total Weight' )
datedistribution_comparison(third_year_data_w, third_year_data_d, '3rd', feature = 'amount', x_label = 'Total Weight' )



#%%

