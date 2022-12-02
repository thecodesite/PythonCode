## How to make a loop that pauses for 5 minutes after each set of 25 iterations until its done?
#https://stackoverflow.com/questions/5628055/execute-statement-every-n-iterations-in-python

for x in 100:
    #what to do every time (100 times): replace this line with your every-iteration functions.
    if x % 5 == 0:
        #what to do every 5th time: replace this line with your nth-iteration functions.
        
## Loops over nested list
tags = [['A','V'],['D','J']]
text = 'AXYJ'
tags_founded = []
for nested_list in tags:
    for i in nested_list:
        if i in text:
            tags_founded.append(i)
tags_founded

## Loops over nested list using dictionary to print/store dictionary keys
def find_tags(tags, text):
    """This find_tags() function allows you
    to extract top keywords and associate
    them with a specific tag. Input: Dictionary
    of tags and the string whose tags will
    be extracted. Output: list of tags
    found."""
    tags_founded = []
    for key, value in tags.items():
        for i in value:
            if i in text:
                tags_founded.append(key)
    return tags_founded
