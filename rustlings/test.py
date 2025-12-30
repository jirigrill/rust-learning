from hashlib import sha256

# Create a program that finds a sha256 hash starting with 5 zeroes.
# To submit your answer, return it from the function.

def find_hash_from_nonce(nonce):
    # Type your code here
    print(type(sha256(b"{nonce}").hexdigest()))


find_hash_from_nonce("hello")
