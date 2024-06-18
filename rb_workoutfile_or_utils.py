#### Generating a random 32 bits word #######
import string
import random

letters, digits, spl_chr = string.ascii_letters, string.digits, string.punctuation
secret_key = ''.join(random.choices(letters+digits+spl_chr, k=32))
print(secret_key)
