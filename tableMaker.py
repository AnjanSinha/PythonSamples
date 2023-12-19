contents = open("random.txt","r")
with open("anjan.html", "w") as e:
    e.write('''<style>
    table,
    th,
    td {
        border: 1px solid black;
    }
    </style>''')
    e.write("<table>\n")   
    for lines in contents.readlines():
        ran=lines.split()
        e.write("<tr><td>%s</td><td>%s</td></tr>\n"%(ran[0],ran[1]))
    e.write("</table>\n")