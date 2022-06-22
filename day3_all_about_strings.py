a = "sifu's line" #use this double quote when you need a single quote in the middle
b = 'hello world' #use this single quote when you dont need any quote inside it
c = '''hello "sifu's line" world'''# use this triple quote when you need both single and  double quote
print(a,b,c)
ind_count= "my name is sifat"
print(ind_count[2])#we can get index number of any string via this
print(ind_count[-6:-3])#negative index number start count from last and come to first number
print(ind_count[0::2])#this 2 here will skip everything after every 2 number
story = "once upon a time there was a boy who wanted to do so many things but he coudn't just because there was a admisson after him"
print(len(story))#len define how many word are there in the string
print(story.endswith("him"))#endswith check if the string ends with the latter we wanted or not

