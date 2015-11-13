
import example
import pdoc


with open('example.html', 'w') as f:
    f.write(pdoc.html("example"))
