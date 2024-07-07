text = "X-DSPAM-Confidence:    0.8475"
ntext = text[(text.find(':'))+1:].lstrip()
print(float(ntext))
