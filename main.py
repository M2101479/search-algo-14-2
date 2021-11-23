
import time

start=time.time()

numbers= [i for i in range(1000000)]


def find(element,value):
  for index,element in enumerate(element):
    if element == value:
      return index
  


end=time.time()

print(find(numbers,int(input('Enter a number'))))
print("It took ",end-start,' seconds')

#average is 0.14838070869
#linear is faster