import lookup
import datetime
from time import sleep

# sleep(.5)

d = int(datetime.date.today().strftime("%d"))
m = datetime.date.today().strftime("%b")

outfile_path = "five_psalms-%s_%d" % (m,d)

psalms = [d, d+30, d+60, d+90, d+120]

div = "\n\n%s\n\n" % ('*'*50)

print(outfile_path)

with open(outfile_path, 'w') as outfile:
    
    for chapter in psalms:

        passage = 'Psalm %s' % chapter

        text = lookup.get_esv_text(passage)

        outfile.write(text)
        outfile.write(div)

