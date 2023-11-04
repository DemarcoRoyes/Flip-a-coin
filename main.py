import random

print("Cant decide?")
print("Flip a coin")

dec1 = input("Heads or Tails?")

random_binary = random.randint(0, 1)

def coin_result():
  if random_binary == 1:
    return("Heads")
  else:
    return("Tails")

def decision():
  if dec1 == random_binary:
    print("You Win!")
  else:
    print("Not quite")

print(f"You got {coin_result()}")
print(decision())
