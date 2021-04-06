"""
  Number of Ways To Traverse Graph

  You're given two positive integers representing the width and the height of a grid-shaped,rectangular
  graph.Write a function that returns the number of ways to reach the bottom right corner of the graph
  when starting at the top left corner.Each move you take must either go down or right.In other words,you
  can never move up or left in the graph.

  For example,given the graph illustrated below, with width = 2 and height =3, there are three ways to reach
  the bottom right corner when starting at the top left corner
     _ _
    |_|_|
    |_|_|
    |_|_|

    1. Down, Down, Right
    2. Right, Down, Down
    3. Down,Right, Down

    Note: you may assume that width * height >= 2.In other words, the graph will never be a 1X1 grid

    Sample Input
      width = 4
      height = 3

    Sample Output
      10
"""