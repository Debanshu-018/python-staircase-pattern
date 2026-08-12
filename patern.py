# Q1.Inverted Pyramid
rows = 5

for i in range(rows, 0, -1):
    print(" " * (rows - i), end="")
    print("* " * i)
    
# OUTPUT
""" * * * * *
     * * * *
      * * *
       * *
        *   """

# Q2.Pyramid Pattern
rows = 5

for i in range(rows):
    print(" " * (rows - i - 1), end="")
    print("* " * (i + 1))

# OUTPUT
""" *
   * *
  * * *
 * * * *
* * * * * """


# Q3. Inverted Right Triangle
rows = 5

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

"""  * * * * *
     * * * *
     * * *
     * *
     *     """













