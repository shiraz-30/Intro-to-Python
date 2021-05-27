f = open('input.txt', 'r')

print(f.read()) # reads the file
print(f.read(5)) # reads the first 5 bytes of the txt file

"""
read function takes argument -> s -> it reads s bytes of the file
tell function -> gets the current file pointer/ cursor position
seek(p) function -> to bring the cursor at any custom position p 
"""
print(f.tell())
print(f.seek(2))
print(f.read(5))
print(f.tell())
f.seek(0)
print(f.readline(3))
