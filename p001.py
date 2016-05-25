set3 = {x for x in range(1,1000) if x%3 == 0}
set5 = {x for x in range(1,1000) if x%5==0}
finalset = ((set3-set5)|(set5 - set3)) | (set3 & set5)
print sum(finalset)