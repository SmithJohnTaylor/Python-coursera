fname = "mbox.txt"
handle = open(fname)

hours = dict()
for lines in handle:
    words = lines.strip().split()
    if len(words) > 0 and words[0] == "From":
        time = words[5].split(':')
        hours[time[0]] = hours.get(time[0],0) + 1

for k,v in sorted(hours.items()):
    print(k,v)
