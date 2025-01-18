#1
x=31
print(x, bin(x), hex(x))

#2
y=18
print(y, hex(y), bin(y))
#"float" object cannot be interpreted as an integer. This is because "y" is a decimal, not an integer. In step 3 once we use an integer, we will see results."

#3
z=0xA3
b=0x12
print(x,b)

#4
r=(z+b+y+x)
print("The sum is "+str(r))

#Compression
#1
original_size = 200
dic_size=20
compressed_size=147
compression=(1-((compressed_size+dic_size)/original_size))*100
print("The compression is: "+str(compression)+"%.")

#2
original_size2 = 240
dic_size2=25
compressed_size2=148
compression2=(1-((compressed_size2+dic_size2)/original_size2))*100
print("The compression2 is: "+str(compression2)+"%.")