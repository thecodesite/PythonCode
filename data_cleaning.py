## Remove empty strings from a list of strings

# Source: https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings
# Sum up best answers:
# 1. Eliminate emtpties WITHOUT stripping:
# That is, all-space strings are retained:

slist = list(filter(None, slist))
#PROs:
#simplest;
#fastest (see benchmarks below).

#2. To eliminate empties after stripping ...
#2.a ... when strings do NOT contain spaces between words:
slist = ' '.join(slist).split()
#PROs:
#small code
#fast (BUT not fastest with big datasets due to memory, contrary to what @paolo-melchiorre results)

#2.b ... when strings contain spaces between words?
slist = list(filter(str.strip, slist))
#PROs:
#fastest;
#understandability of the code.

## Remove emojis
# Be carefull ñ and accents is removed as well
df = df.astype(str).apply(lambda x: x.str.encode('ascii', 'ignore').str.decode('ascii'))
# Another way
import pandas as pd
df = pd.DataFrame({'messages':['Hello! 👋', 'Good-Morning 😃', 'How are you ?', ' Goodé 👍', 'Ländern' ]})
df['messages'].astype(str).apply(lambda x: x.encode('latin-1', 'ignore').decode('latin-1'))

## Export CSV including Latin characters
# 'utf-8' is the standard
df.to_csv('./df.csv', encoding='utf-8-sig')
