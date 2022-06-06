def fizzbuzz(upto):
  generate_string = ""
  while upto > 0:
    upto_string = str(upto)
    if upto % 15 == 0:
      upto_string = "FizzBuzz"
    elif upto % 3 == 0:
      upto_string = "Fizz"
    elif upto % 5 == 0:
      upto_string = "Buzz"
    
    generate_string = upto_string if len(generate_string) == 0 else f"{upto_string}, {generate_string}"
    upto -= 1

  return generate_string


print(fizzbuzz(100))