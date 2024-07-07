fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox.txt"

fh = open(fname)
count = 0
for lines in fh:
    words = lines.strip().split()
    if len(words) > 0 and words[0] == "From":
        print(words[1])
        count += 1

print("There were", count, "lines in the file with From as the first word")
