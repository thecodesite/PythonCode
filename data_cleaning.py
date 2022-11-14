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
