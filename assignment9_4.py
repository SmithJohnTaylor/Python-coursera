fname = "mbox.txt"
fh = open(fname)

sender = dict()
for lines in fh:
    words = lines.strip().split()
    if len(words) > 0 and words[0] == "From":
        sender[words[1]] = sender.get(words[1],0) + 1

senderkey = None
senderval = None
for key,value in sender.items():
    if senderkey is None or value > senderval:
        senderkey = key
        senderval = value
print(senderkey, senderval)
