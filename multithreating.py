from multiprocessing import Process
import turtle
t1=turtle.Turtle()
t2=turtle.Turtle()

def circle():
    t1.circle(100)
    
def rectangle():
    for i in range(2):
        t2.forward(200)
        t2.left(90)
        t2.forward(100)
        t2.left(90)

if __name__ == '__main__':
    p1 = Process(target=circle)
    p1.start()
    p2 = Process(target=rectangle)
    p2.start()
    p1.join()
    p2.join()
