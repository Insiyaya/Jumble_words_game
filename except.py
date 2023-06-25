while True:
       try:
              x = int(input("Please enter a number: "))
              break
       except ValueEr:
              print("Oops!  That was no valid number.  Try again...")
