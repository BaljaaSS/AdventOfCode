with open('AdventOfCode/2020/Input/Input12.txt', 'r') as Input:
    Steps = [list([col[0],int(col[1:])]) for col in Input.read().splitlines()]

# %% Ferry
class Ferry:
    mapToLetter = {
        0: 'E',
        90: 'S',
        180: 'W',
        270: 'N',
        360: 'E'
    }
    mapToAngle = {
        'E': 0,
        'S': 90,
        'W': 180,
        'N': 270
    }

    def __init__(self, xCor, yCor, direction, waypoints = None):
        self.xCor = xCor
        self.yCor = yCor
        self.direction = direction
        self.waypoints = waypoints
        self.MD = self.xCor[1] +self.yCor[1]
        if(waypoints is not None):
            self.MD_WP = self.waypoints[0][1] + self.waypoints[1][1]

    def ComputeManDistance(self):
        return self.xCor[1] +self.yCor[1]

    def ComputeManDistanceForWP(self):
        return self.waypoints[0][1] + self.waypoints[1][1]

    def ChangeCord(self,step):
        if(step[0] in 'EW'):
            if (self.xCor[0] == step[0]):
                self.xCor[1] += step[1]
            else:
                self.xCor[1] = self.xCor[1] - step[1]
                if (self.xCor[1] <0):
                    self.xCor[0] = 'EW'.replace(self.xCor[0],'')
                    self.xCor[1] = abs(self.xCor[1])
        else:
            if (self.yCor[0] == step[0]):
                self.yCor[1] += step[1]
            else:
                self.yCor[1] = self.yCor[1] - step[1]
                if (self.yCor[1] <0):
                    self.yCor[0] = 'SN'.replace(self.yCor[0],'')
                    self.yCor[1] = abs(self.yCor[1])

    def Move(self, step):
        if ( step[0] == 'R'):
            angle = self.direction[1] + step[1]
            if(angle > 360):
                angle -= 360
            self.direction[0] = self.mapToLetter.get(angle)
            self.direction[1] = self.mapToAngle.get(self.direction[0])            

        if( step[0] == 'L'):
            angle = self.direction[1] - step[1]
            if(angle < 0):
                angle += 360
            self.direction[0] = self.mapToLetter.get(angle)
            self.direction[1] = self.mapToAngle.get(self.direction[0])   

        if (step[0] in 'ESWN'):
            self.ChangeCord(step)

        if ( step[0] == 'F'):
            step[0] = self.direction[0]
            self.ChangeCord(step)            

    def MoveWithWaypoint(self, step):     
        if ( step[0] == 'R'):
            angleX = self.mapToAngle.get(self.xCor[0]) + step[1]
            angleY = self.mapToAngle.get(self.yCor[0]) + step[1]
            if(angleX > 360):
                angleX -= 360
            if(angleY > 360):
                angleY -=360
            self.xCor[0] = self.mapToLetter.get(angleX)
            self.yCor[0] = self.mapToLetter.get(angleY)
            if(self.xCor[0] in 'SN'):
                var = self.yCor
                self.yCor = self.xCor
                self.xCor = var

        if( step[0] == 'L'):
            angleX = self.mapToAngle.get(self.xCor[0]) - step[1]
            angleY = self.mapToAngle.get(self.yCor[0]) - step[1]
            if(angleX < 0):
                angleX += 360
            if(angleY < 0):
                angleY += 360                
            self.xCor[0] = self.mapToLetter.get(angleX)
            self.yCor[0] = self.mapToLetter.get(angleY)
            if(self.xCor[0] in 'SN'):
                var = self.yCor
                self.yCor = self.xCor
                self.xCor = var                      

        if (step[0] in 'ESWN'):
            self.ChangeCord(step)

        if ( step[0] == 'F'):
            step[0] = self.direction[0]
            if (self.waypoints[0][0] == self.xCor[0]):
                self.waypoints[0][1] += step[1]*self.xCor[1]
            else:
                self.waypoints[0][1] = self.waypoints[0][1] - step[1]*self.xCor[1]
                if (self.waypoints[0][1] <0):
                    self.waypoints[0][0] = 'EW'.replace(self.waypoints[0][0],'')
                    self.waypoints[0][1] = abs(self.waypoints[0][1])
            
            if (self.waypoints[1][0] == self.yCor[0]):
                self.waypoints[1][1] += step[1]*self.yCor[1]
            else:
                self.waypoints[1][1] = self.waypoints[1][1] - step[1]*self.yCor[1]
                if (self.waypoints[1][1] <0):
                    self.waypoints[1][0] = 'SN'.replace(self.waypoints[1][0],'')
                    self.waypoints[1][1] = abs(self.waypoints[1][1])

# %% Part-1 and Part-2
def ComputeManhattanDistance():
    ferry1 = Ferry(['E',0], ['N',0], ['E', 0])
    ferry2 = Ferry(['E',10], ['N',1], ['E', 0], [['E',0], ['N',0]])    
    for step in Steps:
        ferry1.Move(step[:])
        ferry2.MoveWithWaypoint(step[:])
    return ferry1.ComputeManDistance(), ferry2.ComputeManDistanceForWP()

# %% Main
distance = ComputeManhattanDistance()
print("Part-1: the Manhattan distance is :", distance[0])
print("Part-2: the Manhattan distance is :", distance[1])
