

#%%
def target_distribution(data, targ_col):
    print("Consumption Feature Values: ", data[targ_col].unique())

    fig = plt.figure()
    sns.distplot(data[targ_col], color ='g' )
target_distribution(data, 'Walc')


####### TARGET Creation #######
    # Combine two categorical features(Walc & Dalc) to create Target

#%% ------------------> 1. Weighted sum of Walc and Dalc
# data["consumption"] = data["Walc"] * 0.5 + data["Dalc"] * 0.5
# data = data.drop(['Dalc',"Walc"], axis = 1)

#     #Transform Multiclassification to Binaryclassification problem
#     # Turning categorical target with 4 values to binary vaiable with putting threshold. 
# data["consumption" ] = (data["consumption"] > 2.5).astype(int)


#%% ------------------> 2. Prod of Walc and Dalc 
# data["consumption"] = data["Walc"] *  data["Dalc"]
# data['consumption'] = pd.cut(data['consumption'], bins = [0, 10, 25] , labels = [0,  1])



#%% ------------------> 3. Walc edge value 
data["Walc"] = (data["Walc"] > 2).astype(int)
data = data.drop(['Dalc',], axis = 1)


#%% ------------------> 4. Average 
# data['consumption'] = (((data['Dalc']+ data['Walc'])/2)>2.5).astype(int)
# data = data.drop(['Dalc',"Walc"], axis = 1)







#%% Convert yes,no --> 0,1
yes_no = ['schoolsup',	'famsup', 'paid', 'activities',	'nursery','higher',	'internet',	'romantic']
encoder = LabelEncoder()
for i in data[yes_no]:
    data[i] = encoder.fit_transform(data[i])






#%% One-hot-encoding for categorical data
get_dummie = pd.get_dummies(data[['school',	'sex','address','famsize','Pstatus','Mjob','Fjob','reason','guardian', 'age_group']])

# Concatenate dummied data with data
data = pd.concat([data, get_dummie], axis = 1)

# # Drop orignal categorical data
data = data.drop(['school','sex','address','famsize','Pstatus','Mjob','Fjob','reason'	,'guardian', 'age_group', ], axis = 1)
   

# # Drop one of the categoircal cases for binaries
data = data.drop(['sex_M', 'address_R', 'famsize_LE3', 'Pstatus_A', 'school_GP' , 'age_group_18_21'], axis = 1)







#%% Heatmap for data relationships
plt.figure(figsize = (25, 20))
thresh = 0.3
cm = data.corr()
cm_thresh = cm[(cm>.3)|(cm<-.3)]
sns.heatmap(cm_thresh, 
           annot = True, 
           cmap = 'gist_earth')

plt.tight_layout()



