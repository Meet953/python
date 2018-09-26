# GENERATOR FUNCTION TO GENERATE 7 RANDOM NUMBERS FOR A LOTTERY...
import random
def lottery():
      for i in range(7):
            yield random.randint(1000,9999)
for random_number in lottery():
      print"And the next number is...",random_number




