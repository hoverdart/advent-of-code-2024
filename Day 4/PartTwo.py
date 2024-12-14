def count_word(grid, word): ##I Actually Dont Think This one WOrks!!
  rows, cols = len(grid), len(grid[0])
  word_len = len(word)
  directions = [ #first number changes row (up-down, y), second number changes column (side-side, x)
      (0, 1),   # Right
      (0, -1),  # Left
      (1, 0),   # Down
      (-1, 0),  # Up
      (1, 1),   # Down-right diagonal
      (1, -1),  # Down-left diagonal
      (-1, 1),  # Up-right diagonal
      (-1, -1)  # Up-left diagonal
  ]
  combosForCross = [
    [(1,1), (1, -1)], #down-right, down-left
    [(1, 1), (-1, 1)], #down-right, up-right
    [(-1, 1), (-1, -1)],#up right, up left
    [(-1, -1), (1, -1)] #up left, down left
  ]

  def check_direction(x, y, dx, dy):
      """Check if the word exists starting at (x, y) in direction (dx, dy)."""
      for i in range(word_len):
          nx, ny = x + (i * dx), y + (i * dy)
          if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != word[i]:
              return False
      return True
    
  count = 0
  for r in range(rows):
      for c in range(cols):
          for eachList in combosForCross: #For Part 2
            if check_direction(r, c, eachList[0][0], eachList[0][1]) and check_direction(r, c, eachList[1][0], eachList[1][1]):
                count+=1
  return count
  
# Count occurrences
file = open("sampleText.txt", "r")
grid_list = [list(eachLine) for eachLine in file]
for i in range(len(grid_list)):
  grid_list[i].pop()
word = "MAS"
result = count_word(grid_list, word)
print(result)
