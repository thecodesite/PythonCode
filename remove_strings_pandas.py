# Below are some quick examples.
# Replace string using DataFrame.replace() method.
df2 = df.replace('Py','Python with ', regex=True)

# Replace pattern of string using regular expression.
df2 = df.replace({'Courses': 'Py', 'Duration': 'days'}, 
    {'Courses': 'Python with', 'Duration': ' Days'}, regex=True)

# Replace pattern of string using regular expression.
df2=df.replace(regex=['Language'],value='Lang')

# By using str.replace()
df['Courses'] = df['Courses'].str.replace('Language','Lang')

# Replace String using apply() function with lambda.
df2 = df.apply(lambda x: x.replace({'Py':'Python with', 'Language':'Lang'}, regex=True))
