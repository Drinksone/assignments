# Provide a program to read the file from URL and display the content in terminal.
# The file URL has to be input by the user.
# The program has to work from the terminal. The input and output have been taken/displayed on the terminal.


from urllib.request import urlopen                         #import urllib library
target_url=input("input url which you want to open:")

#print(url)
data = urlopen(target_url)                               #target url which we want to read
for line in data:
    print(line)                                         #print each line data
