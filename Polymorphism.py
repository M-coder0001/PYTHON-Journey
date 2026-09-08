class Polygon:
    def render(self):
        print("Rendering a polygon")

class Triangle(Polygon):
    def render(self):
        print("Rendering a triangle")
        
class Square(Polygon):
    def render(self):
        print("Rendering a square")

c1 = Polygon()
c1.render()

c2 = Triangle()
c2.render()

c3 = Square()
c3.render()
