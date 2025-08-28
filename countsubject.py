fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()

count = 0
for line in fhand :
    if line.startswith('subject: ') :
        count = count + 1
print('There was/were', count, 'subject line(s) in', fname)