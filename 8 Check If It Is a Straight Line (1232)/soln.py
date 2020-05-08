class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        length=len(coordinates)
        if (length<3):                                  #Edge case of upto 2 coords
            return True
        
        xi=float(coordinates[0][0])
        yi=float(coordinates[0][1])
        
        if coordinates[1][0] == xi:                     #Edge case values lie on x axis
            for index in range(2, length-1):
                if coordinates[index][0] == xi :
                    return True
            return False
        
        #else when values aren't horizontal
        slope = (coordinates[1][1] - yi)/(coordinates[1][0] - xi)
        for index in range(2, length-1):
            if (coordinates[index][1] - yi)/(coordinates[index][0] - xi)!=slope:
                return False
        return True