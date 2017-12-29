"""
BOT SAVES PRINCESS
This is a code for a bot in a game. The player is provided with a n x n grid where n is odd. A any one corner of the square  
the princess is trapped(represented by "p"). The bot is placed at the middle of the grid (represented by "m"). The code should  
print out the steps to be taken by the bot to reach the princess (DOWN, UP, LEFT OR RIGHT).

Input:
1. Size of grid ---> n
2. Grid

Output:
path (one move per line)

Sample:
Input:
3
- - -
- m -
p - -

Output: 
DOWN   (or)  LEFT
LEFT         DOWN

Explanation:
directions to reach princess(p) by bot(m).

"""
def displayPathtoPrincess(n,grid):
    
    if a < y and b < x:
        up()
        left()
        
        if x != b and a != y:
            displayPathtoPrincess(n,grid)
           
    elif a > y and b > x:
        down()
        right()
        
        if x !=b and a !=y:
            displayPathtoPrincess(n,grid)
       
    
    elif a > y and b < x:
        down()
        left()
        
        if x !=b and a !=y:
            displayPathtoPrincess(n,grid)
    
    elif a < y and b > x:
        up()
        right()
        
        if x !=b and a !=y:
            displayPathtoPrincess(n,grid)
    

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

# Movement:
def up():
    global y
    y -= 1
    print("UP")

def down():
    global y
    y += 1
    print("DOWN")

def left():
    global x
    x -= 1
    print("LEFT")

def right():
    global x
    x += 1
    print("RIGHT")
 
# Location of princess
for i in range(0, m):
        for j in range(0, m):
            if grid[i][j] == "p":
                a = i
                b = j

# Starting position of bot
q = (m - 1) // 2
   
x = q
y = q
displayPathtoPrincess(m, grid)


