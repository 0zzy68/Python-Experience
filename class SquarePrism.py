class SquarePrism(Square):
     def __init__(self, side, height):
         self.side = side
         self.height = height
 
     def face_area(self):
         base_area = super().area()
         lateral_area = self.side * self.height
         return base_area, lateral_area
 
     def area(self):
         base_area = super().area()
         lateral_area = self.side * self.height
         return 2 * base_area + 4 * lateral_area