"""
BOT SAVES PRINCESS


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
    
for i in range(0, m):
        for j in range(0, m):
            if grid[i][j] == "p":
                a = i
                b = j



q = (m - 1) // 2
    

x = q
y = q
displayPathtoPrincess(m, grid)


