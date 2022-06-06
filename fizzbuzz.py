def fizzbuzz(upto):
  generated_list = []
  while upto > 0:
    to_insert = str(upto)
    if upto % 15 == 0:
      to_insert = "FizzBuzz"
    elif upto % 3 == 0:
      to_insert = "Fizz"
    elif upto % 5 == 0:
      to_insert = "Buzz"

    generated_list.insert(0,to_insert)
    upto -= 1

  return ', '.join(generated_list)