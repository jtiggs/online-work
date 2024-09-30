import pandas as pd


mouse_meta = "C:\\Users\\E7470\\Downloads\\Mouse_metadata.csv"
mouse_data = "C:\\Users\\E7470\\Downloads\\Study_results.csv"

#****************************************************
#      Read in dataframes and look at the head & length
#***************************************************

df1 = pd.read_csv(mouse_meta)
df2 = pd.read_csv(mouse_data)

print(df1.head())
print(len(df1)) # 249
print(df2.head())
print(len(df2)) # 1893

     
df=pd.merge(df1, df2)
print(df.head())
print(len(df)) # 1893

#***********************************************
#   Analyze for Dups based on 2 columns only
#**************************************************
df.columns


cleaned_df=df.drop_duplicates(subset=['Mouse ID', 'Timepoint'], keep='last')
print(len(cleaned_df))  # 1888 (droped 5 rows of dups)


#****************************************************
#           Male/Female Value_Counts
#***************************************************

mf = cleaned_df.loc[:, 'Sex']
mf2 = mf.value_counts()
mf2 # These values are incorrect because they count the same mouse for each clinic visit
# so the true numbers are far smaller

true_mf1 = un_mice.loc[:, 'Sex']
true_mf2 = true_mf1.value_counts()
true_mf2


#****************************************************
#           Analyze Timepoints
#***************************************************

testdf=cleaned_df.loc[cleaned_df["Mouse ID"] == 'k403']
testdf  # simply check one mouse for quantity of Timepoints = 0-45 in increments of 5
# Use this data for the line plot of the Tumor Size over time (Timepoints)
# Pull out x-axis and y-axis data from here

xaxis = testdf.loc[:, 'Timepoint'] # x-axis could be time
anotherxaxis = testdf.loc[:, 'Weight (g)'] # x-axis could be weight
yaxis = testdf.loc[:, 'Tumor Volume (mm3)']



# Check the content of Timepoint column
print(cleaned_df['Timepoint'].value_counts())
# Timepoints range from 0 - 45 BUT are not all equal in length, meaning some
# mice did not have all weeks of treatments and some did


# Test filtration logic for START & STOP Turmor Size on mouse 'k403'
testdf.dtypes # take a look at the dtypes of each column of mouse k403
allstats=testdf.describe() # Generate statistics on the one mouse . . . could be applied in a loop to each mouse

type(allstats) # allstats is a df, so .loc will work to pull out mins and max's

# Standard Error of the Mean (SEM):
sem=cleaned_df['Tumor Volume (mm3)'].sem()
sem # This is over all Drug Regimens COMBINED, but this could be used for each Regimen


allstats.index # use 'min' and 'max' to extract Tumor Volume
    
mouse1_min =allstats.loc['min', 'Timepoint']
mouse1_min

mouse1_max =allstats.loc['max', 'Timepoint']
mouse1_max

#Using mouse1_max and min Timepoints, extract Tumor Volumes

m1_tumorVolmin = allstats.loc[allstats['Timepoint']== mouse1_min, 'Tumor Volume (mm3)']
print(m1_tumorVolmin)
m1_tumorVolmax =  allstats.loc[allstats['Timepoint']== mouse1_max, 'Tumor Volume (mm3)']
print(m1_tumorVolmax)
type(m1_tumorVolmax)
# Now calculate Tumor size based on START to FINISH

size = float(m1_tumorVolmax) - float(m1_tumorVolmin)
size # Boooooyaaa!  Got the Tumor Size for this one mouse 'k403'

# Ins

# ************************************************
#       Find only UNIQUE mice for all studies & groupby Regimens
#**********************************************

df_unique=pd.unique(cleaned_df['Mouse ID'])
len(df_unique) # 249 completely unique mice

un_mice = cleaned_df.drop_duplicates(subset=['Mouse ID', 'Drug Regimen']).copy()
len(un_mice) #249 unique mice within all Drug Regimens
un_mice.head()


grp=un_mice.groupby(['Drug Regimen']).count()
print(grp)
justmice=grp.loc[:, 'Mouse ID']
justmice

#**************************************
#       Run Summary Statistics on Drugs
#***********************************
grp_stats=cleaned_df.groupby(['Drug Regimen']).describe()
grp_stats
Tumor_stats = grp_stats.loc[:,'Tumor Volume (mm3)']


# Standard Error of the Mean (SEM)
grp_SEM = cleaned_df.groupby(['Drug Regimen']).sem()
Tumor_sem = grp_SEM.loc[:,'Tumor Volume (mm3)']
Tumor_sem

#********************************************
#       How many unique Drug Studies?
#******************************************

DrugStudies = cleaned_df['Drug Regimen'].unique()
DrugStudies
len(DrugStudies)
# ********************************************
#   Using un_mice (unique mice within Regimens) Insert New Column for Net Tumor Size
#**********************************************

# insert a new column and set all values equal to -500 to make it ridiculous and easy to check for errors later

un_mice['Final_Tumor_Size']=-500
un_mice.head()
# Reduce the columns to only what is needed
un_mice=un_mice.loc[:,['Mouse ID', 'Drug Regimen','Final_Tumor_Size']]

# Inside of a loop maybe do something like this to replace Final Tumor Vol ...
testp=un_mice.loc[un_mice['Mouse ID']=='k403']

testp['Final_Tumor_Size']=size # from up above but can be combined into a loop
testp

