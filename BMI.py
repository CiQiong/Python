
w=input()
h=input()
bmi=w/h/h
if bmi<18.5:
    print("偏瘦 偏瘦")
elif bmi>=18.5 and bmi<25:
    print("正常 ")
elif bmi>=25 and bmi<30:
    print("偏胖 ")
else print("肥胖 ")

if bmi>=18.5 and bmi<24:
    print("正常")

elif bmi>=24 and bmi<28:
    print("偏胖")
else print("肥胖")
