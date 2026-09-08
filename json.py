import json
data = '''{
"name" : "Chuck"",
"phone" : {
"type" : "intl",
"number" : "+1 7343034456"
},
"email" : {
"hide" : "yes"
}
}'''

info = json.loads(data)
print('Name:' , info["name"])
print('Hide:', info["email"]["hide"])