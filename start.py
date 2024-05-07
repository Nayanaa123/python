file=open("index.html","w")
title=input("enter your site title:")
heading=input("enter your site heading")
para=input("enter your site content")
colour=input("enter your background colour :")
file.write("""
<html>
           <head>
             <title>%s</title>
           </head>
           <body bgcolor='%s'>
             <h1>%s</h1>
             <p>%s</p>
           </body>
</html>
""" %(title,colour,heading,para))
print("webpage created successsfully")       