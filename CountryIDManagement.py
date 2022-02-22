# opens the file with encoding
fn = 'Unique-IDs.txt'
fh = open(fn, encoding='utf-8')

# define lists and dicts
countries = []
countriesnew = []
dic = dict()
emptystring = ''

for line in fh:
    line = line.rstrip()
    # excludes lines that has IDs or are empty ones
    if not line.startswith('- ') and not line == emptystring:
        # appends the list
        countries.append(line)
    else:
        continue

for i in countries:
    # gets rid of chars after ID
    j = i[:-1]
    # splits the lines
    j = j.split(" (ID:")
    countriesnew.append(j)
