class Rectangle(object):
    """represents a rectangle. attributes:width,height,corner"""

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    
    box.corner = Point()
    box.corner.x=0.0
    box.corner.y= 0.0


def find_center(rect):
    p = Point()
    p.x = rect.corner.x +rect.width/2.0
    p.y = rect.corner.y+rect.height/2.0
    return p
    
box.width = box.width+50
box.height= box .height+100

def grow_rectangle(rect,dwidth,dheight):
    rect.width += dwidth
    rect.height += dheight
    
    
def move_rectangle(Rectangle,dx,dy):
    box.corner = box.corner.x + dx
    box.corner = box.corner.y+ dy
    
    
print box.width 
print box.height
grow_rectangle(box,50 , 100)
print box.width
print box.height



