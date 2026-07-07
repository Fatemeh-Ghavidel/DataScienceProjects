

#%%
def distribution_wrt_walc(data, nrows, ncols, feature):
    """Plot distribution of features with respect to Walc."""
    cols_names = [col  for col in data.columns if col != feature]
    fig, axes = plt.subplots(nrows = nrows, ncols = ncols, figsize = (20, 18))
    axes = axes.flatten()
    palette = sns.color_palette('Pastel2')
  
    for ax , col   in zip(axes , cols_names):
        sns.kdeplot(data = data , x = feature, hue = col, palette = palette, ax = ax, fill = True, alpha = 0.5)
        ax.set_title(f'Distribution by {col}')
        ax.grid()
    for i in range(len(cols_names), len(axes)):
        axes[i].set_visible(False)
    
    plt.tight_layout()
    



### Feature engineering 
#%% Age Binning
bins = [15,18,22]

labels = ["15_17","18_21",]
data["age_group"] = pd.cut(data["age"], bins = bins, labels = labels, include_lowest = True)
data = data.drop('age', axis = 1)

#%% Grade Aggregation
data['G'] = data[['G1', 'G2', 'G3']].mean(axis = 1)
data = data.drop(['G1', 'G2', 'G3'], axis = 1)









##############################-------- Student personal information --------##############################
    #%% Data
PersonCol = data[['sex' ,'school' ,'address' , 'age_group', 'reason' ,'health', 'Walc']]


    #%% Distribution of the data wrt Walc. 
    #--------------------------------------------------------------------------------------
distribution_wrt_walc(data = PersonCol, nrows=2, ncols=3, feature='Walc')


# General pattern  
#     The probability distribution of Walc for the features is demonstrated. 
#     The distribution of weekly alcohol consumption (Walc) shows a declining pattern –> low consumption (1 time per week) is the most dominant across all categories of features.
 

## By gender
#     Females: Peak consumption is at 1 time per week, with a sharp decline as consumption frequency increases.
#     Males: Show a relatively more constant consumption pattern compared to females. At higher consumption levels (3+ times/week), males outnumber females.  
    
## By Health Status
#     Students with the best health condition (health score = 5) form the largest group.
#     the number of students with differernt health conditions decrease with more consumption. 
 
## By School Type
#     GP school: Majority of students consume alcohol 1 time per week.
#     MS school: Students show higher-than-average weekly consumption, with a noticeable peak at 3 times per week. 

## By Area (Urban/Rural)
#     Urban area: Higher concentration of students.
#     Rural area: Consumption is relatively constant, ranging between 1–3 times per week.

## By Age
#    Students aged 18-21 show constant alcohol consumption pattern compared to other age group.



    #%% Correlation of the data
    #--------------------------------------------------------------------------------------
#%%
def plot_personal_info_vs_walc(data):
    """ Visualize relationships between personal information features and alcohol consumption (Walc).
    """
    
    fig, axes = plt.subplots(nrows = 2, ncols  =  2,figsize = (15, 10) )

    # Plot 1: Sex vs School colored by Walc
    sns.swarmplot(data=data, x='sex', y='school', hue='Walc',palette=palette, ax = axes[0, 0])
    axes[0, 0].set_title('School Distribution by Sex and Alcohol Consumption')

    # Plot 2: Sex vs address colored by Walc
    sns.swarmplot(data=data, x='sex', y='address', hue='Walc',palette=palette,ax = axes[0, 1] )
    axes[0, 1].set_title('Address Distribution by Sex and Alcohol Consumption')

    # Plot 3: Age Group vs Walc by Sex
    sns.boxplot(data , x = 'age_group', y = 'Walc', hue = 'sex', palette = palette, ax = axes[1,0] )
    axes[1, 0].set_title('Alcohol Consumption by Age Group and Sex')
    
    # Plot 4: Health vs Walc by Age Group
    sns.boxplot(data , x = 'health', y = 'Walc', hue = 'age_group', palette = palette, ax = axes[1,1] )
    axes[1, 1].set_title('Alcohol Consumption by Health Status and Age Group')

    
plot_personal_info_vs_walc(data)

# Males in Urban address have more consumption than Rural and man more than women in both areaes. 

# Male students in MS and GP schools have more consumption than female. Most consumptio for males is in GP school. 

# Male in the age of 15-17 with the most consumption and female in the age of 18-21 with the least consumption. 

# The carrolation of health and Walc colored by age is not very meaningful. But the
    # average of consumption in age 18-21 droped as health increased.  









##############################-------- Education condition  Information  --------##############################
    #%% Data
education_condition = data[['G', 'failures', 'absences', 'higher', 'nursery', 'studytime', 'paid' , 'schoolsup','Walc']]

    #%% Distribution of the data wrt Walc 
    #--------------------------------------------------------------------------------------
education_condition = data[['failures',  'higher', 'nursery', 'studytime', 'paid' , 'schoolsup','Walc', 'G']]
distribution_wrt_walc(data=education_condition , nrows =2, ncols=3,  feature = 'Walc')

# Study Time: Low study time is associated with higher-than-average weekly alcohol consumption.

# Failures: Students with more failures tend to have higher weekly alcohol consumption.

# Higher Education (higher = "no"): Students who do not intend to pursue higher education show higher weekly alcohol consumption compared to those who do.


    #%% Distribution of the data wrt G
    #--------------------------------------------------------------------------------------
distribution_wrt_walc(data=education_condition , nrows =2, ncols=3, feature='G')

# Study Time: More study time leads to higher average grades (G).

# Failures: Fewer failures are associated with higher aveducation_condition_2erage grades.

# Higher Education (higher = "no"): Students who do not plan to pursue higher education tend to have lower average grades.


    #%% Correlation of the data 
    #--------------------------------------------------------------------------------------
## Walc -> Failure, Higher, Nursery, Sudytime 
def plot_education_vs_walc(data , cols):
        """Plot boxplots showing relationship between educational features and alcohol consumption (Walc)."""
        for col in cols: 
            sns.catplot(data, x =col, y= 'Walc', kind = 'box', palette = palette, height=5, aspect=1.5)  
            plt.title(f'Walc Distribution by {col}') 
plot_education_vs_walc(data, cols =['failures', 'higher', 'nursery', 'studytime'])    

# More Weakly consumption correlated with More failures and less sudy time. 

# Having no nursery and no tendency for higher education leaded to Walc.   


## G -> Studytime, Failure, Higher 
def plot_education_vs_grades(cols):
        """Plot boxplots showing relationship between educational features and average grades (G)."""
        for col in cols: 
            sns.catplot(data, x =col, y= 'G', kind = 'box', palette = palette)
            plt.title(f'Grade Distribution (G) by {col}')
plot_education_vs_grades(cols = ['failures', 'higher', 'nursery', 'studytime'])    

# More G correlated to less failures, more study time , having nursery and tendency to higher education. 


## G and W colored with Failures, Higher, Nursery, Studytime 
def plot_education_G_walc_interaction(data, cols):
        """Plot swarmplots showing interaction between educational features, grades (G), and alcohol consumption (Walc)."""
        fig, axes = plt.subplots(nrows = 2, ncols =2, figsize = (15, 10))
        axes = axes.flatten()
        for col ,ax in zip(cols, axes):
            sns.swarmplot(data, y ='G', x= 'Walc', hue = col,  palette = palette, ax = ax)
            ax.set_title(f'Grades vs Alcohol Consumption by {col}')
            ax.grid(True, alpha=0.3)
            ax.legend(loc='best', fontsize=8)
plot_education_G_walc_interaction( data, cols =  ['failures','higher', 'studytime', 'nursery' ])










##############################-------- Student leisure activities information --------##############################

    #%% Data
fun_time = data[['freetime', 'goout', 'traveltime', 'internet', 'romantic', 'activities', 'Walc']]

    #%% Distribution of the data wrt Walc 
    #--------------------------------------------------------------------------------------
distribution_wrt_walc(data = fun_time, nrows=2, ncols=3, feature='Walc')
 # More going out and having more free time hihly corrolated with more weekly alcohol consumption . 

    #%% Correlation of data
# Walc with goout and freetime
def plot_leisure_walc_corr(cols):
        fig, axes = plt.subplots(nrows = 1, ncols = 2)
        for i, col in zip(range(2), cols):
            sns.boxplot(data , x = col, y = 'Walc',palette = palette, ax = axes[i])
        plt.figure()
        sns.swarmplot(data, y='freetime', x= 'Walc', hue = 'goout', palette = palette)
plot_leisure_walc_corr(['goout', 'freetime'])








##############################-------- Family Status Information --------##############################
    #%% Data
family_status = data[['famsize', 'famsup',  'Medu', 'Fedu', 'Fjob', 'Mjob', 
                      'famrel', 'guardian','Pstatus', 'Walc']]

    #%% Distribution of family status features wrt Walc 
    #--------------------------------------------------------------------------------------
distribution_wrt_walc(data = family_status, nrows=3, ncols=3, feature='Walc')



# Students from small families show relatively a stable, uniform pattern of alcohol consumption across all weekly levels.

# Constant distribution for students with no family support for consumptions more than 1 times per week.
#    -> No variation in alcohol consumption patterns.

# Constant pattern observed for mother education levels:
  ##Medu = 1 (lowest education level)
  ##Medu = 3 (middle education level)

# Different pattern for students whose parents live apart (separated/divorced).

# Constant pattern for students with lower relationship quality (low famrel scores).

# # gurdian other has different distribbution patterns than mother and father as gurdian. 




    #%% Correlation of family information and Walc
    #--------------------------------------------------------------------------------------
def plot_family_info_vs_walc(data, cols1, cols2):
    """ Plot relationships between family information features and alcohol consumption (Walc)."""
   
    # Point plots: continuous relationship with Walc
    for col  in cols1: 
        sns.catplot(data, x=col,   y='Walc',  kind = 'point', palette = palette)
    plt.title(f'Walc Distribution by {col}')
    
    # Swarm plots: categorical distribution with Walc hue
    for col in cols2: 
        sns.catplot(data=data, x='Walc', hue= col ,kind = 'box', palette=palette)
    plt.title(f'Distribution of {col} by Walc Level')

plot_family_info_vs_walc(data , cols1=['famrel', 'Mjob', 'Fjob'], cols2 = ['famsize','Pstatus' ])       
        
    
# Better family relationship showed Less alcohol consumption.

# Less alcoho consumption was observed for father job as at-home case and mother as others case.

# Family size (famsize) showed no significant relationship with alcohol consumption.

# Parents live apart (separated or divorced) showed higher alcohol consumption.




    #%% Correlation of education and job of parents with other features 
def plot_parent_education_corr(data):
    
    # Boxplot: Mother's vs Father's education by family status
    sns.catplot(data, x = 'Medu', y = 'Fedu', hue = 'Pstatus',kind = 'box',  palette=palette)
    plt.title('Parents\' Education by Family Status')

    # Scatter: Parents' education colored by family relationship quality
    sns.relplot(data, x = 'Medu', y = 'Fedu', hue = 'famrel', kind ='scatter' ,palette = palette)
    plt.title('Parents\' Education by Family Relationship Quality')

    # Scatter: Parents' education colored by alcohol consumption
    sns.relplot(data, x = 'Medu', y = 'Fedu', hue = 'Walc',  kind = 'scatter',palette = palette)
    plt.title('Parents\' Education by Student Alcohol Consumption')



def plot_parent_job_corr(data):
    
    # Boxplots: Father's job vs family relationship
    sns.catplot(data, y = 'Fjob' , x= 'famrel', kind = 'box', palette = palette)
    plt.title('Father\'s Job by Family Relationship Quality')
    
    # Boxplots: Mother's job vs family relationship
    sns.catplot(data, y = 'Mjob' , x= 'famrel', kind = 'box', palette = palette )
    plt.title('Mother\'s Job by Family Relationship Quality')

    # Scatter: Parents' jobs colored by family relationship
    sns.relplot(data,  x = 'Mjob', y = 'Fjob', hue = 'famrel', kind = 'scatter', palette = palette)
    plt.title('Parents\' Jobs by Family Relationship Quality')
    
    # Scatter: Parents' jobs colored by alcohol consumption
    sns.relplot(data, x = 'Mjob', y = 'Fjob', hue = 'Walc', kind = 'scatter', palette = palette)
    plt.title('Parents\' Jobs by Student Alcohol Consumption')

plot_parent_job_corr(data)



# %%
