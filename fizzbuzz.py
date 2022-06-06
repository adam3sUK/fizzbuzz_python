from pickletools import UP_TO_NEWLINE


def generate(upto):
  generate_string = ""
  while upto > 0:
    upto_string = str(upto)
    if upto % 3 == 0:
      upto_string = "Fizz"
    elif upto % 5 == 0:
      upto_string = "Buzz"

    if len(generate_string) == 0:
      generate_string = upto_string
    else:
      generate_string = f"{upto_string}, {generate_string}"
    upto -= 1
  return generate_string