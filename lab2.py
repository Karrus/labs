dict={"A":"11", "B":"12", "C":"13",                                    
    "D":"14", "E":"15", "F":"16", "G":"21",
    "H":"22", "I":"23", "J":"24","K":"25",
    "L":"26", "M":"31", "N":"32", "O":"33",
    "P":"34", "Q":"35", "R":"36", "S":"41",
    "T":"42", "U":"43", "V":"44", "W":"45",
    "X":"46", "Y":"51", "Z":"52"," ":"53"}                                     
w = input('your word: ').upper()
encode= ''
for i in w:
    if i in dict:
        encode+= dict.get(i)
print('encode word: ', encode)


list_num= []
new_txt= '' 

step= 2
for i in range(0, len(encode), 2):
    list_num.append(encode[i: step])
    step+= 2
l_keys= list(dict.keys())
l_values= list(dict.values())
    
for i in list_num:
    if i in l_values:
        a= l_values.index(i)
        new_txt+= l_keys[a] 
    else:
        new_txt+= i[0:1]
print('decode num: ',new_txt)
