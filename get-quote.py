import random

def main():
  #print("Keep it logically awesome.")

  f = open("quotes.txt", "a")
  f.write("I'm learning how to put a new line is a file using Python!")
  f.close()

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1
  rnd1 = random.randint(0, last)
  rnd2 = random.randint(0, last)

  print(quotes[rnd1].strip())
  print(quotes[rnd2].strip())

if __name__== "__main__":
  main()
