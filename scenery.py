import turtle as t
import random

tree_height_1 = random.randint(50, 200)
tree_height_2 = random.randint(50, 200)

def draw_pine(height):
    """

    :precondition:
    :postcondition:
    """
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(height*0.3)
    t.left(120)
    t.forward(height*0.6)
    t.left(120)
    t.forward(height*0.6)
    t.left(120)
    t.forward(height*0.3)
    t.right(90)
    t.forward(height)
    t.left(90)

def draw_maple(height):
    """

    :precondition:
    :postcondition:
    """
    t.left(90)
    t.forward(height)
    t.right(90)
    t.circle(height*0.4)
    t.right(90)
    t.forward(height)
    t.left(90)

def draw_house(length, color):
    """

    :precondition:
    :postcondition:
    """
    t.pencolor(color)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(45)
    t.forward(length / (2 ** 0.5))
    t.left(90)
    t.forward(length / (2 ** 0.5))
    t.left(45)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.pencolor("black")


def generate_tree_1():
    """

    """
    trees = [draw_pine, draw_maple]
    tree_1 = random.choice(trees)
    tree_1(tree_height_1)
    return tree_1

def generate_tree_2():
    """

    """
    trees = [draw_pine, draw_maple]
    tree_2 = random.choice(trees)
    tree_2(tree_height_2)
    return tree_2

tree_height_3 = random.randint(50, 200)

def generate_maple():
    """

    """
    ran_int = random.randint(1, 2)
    if ran_int == 1:
        draw_maple(tree_height_3)
        t.forward(100)
        return tree_height_3
    else:
        return None



def main():


    house = input("Do you want a house? (yes/no) ")
    if house == "yes":
        length = int(input("How long do you want your house to be? "))
        color = input("What color do you want your house to be? ")
        t.setup(1500, 800)
        t.backward(200)
        tree_1 = generate_tree_1()
        t.backward(100)
        t.forward(200)
        draw_house(length, color)
        t.forward(100)
        tree_2 = generate_tree_2()
        t.forward(100)
        tree_3 = generate_maple()

        if tree_3 is not None:
            print(tree_height_1, tree_height_2, tree_3)
            if tree_1 == draw_pine:
                if tree_2 == draw_pine:
                    print((2.8*tree_height_1)+(2.8*tree_height_2)+(0.8*3.14*tree_3) + (500+length) + (2*length+length*(2**0.5)))
                elif tree_2 == draw_maple:
                    print((2.8*tree_height_1)+(0.8*3.14*tree_height_2)+(0.8*3.14*tree_3) + (500+length) + (2*length+length*(2**0.5)))
            elif tree_1 == draw_maple:
                if tree_2 == draw_pine:
                    print((0.8*3.14*tree_height_1)+(2.8*tree_height_2)+(0.8*3.14*tree_3) + (500+length) + (2*length+length*(2**0.5)))
                elif tree_2 == draw_maple:
                    print((0.8*3.14*tree_height_1)+(0.8*3.14*tree_height_2)+(0.8*3.14*tree_3) + (500+length) + (2*length+length*(2**0.5)))
        else:
            print(tree_height_1, tree_height_2)
            if tree_1 == draw_pine:
                if tree_2 == draw_pine:
                    print((2.8 * tree_height_1) + (2.8 * tree_height_2) + (400+length) + (2*length+length*(2**0.5)))
                elif tree_2 == draw_maple:
                    print((2.8 * tree_height_1) + (0.8 * 3.14 * tree_height_2) + (400+length) + (2*length+length*(2**0.5)))
            elif tree_1 == draw_maple:
                if tree_2 == draw_pine:
                    print((0.8 * 3.14 * tree_height_1) + (2.8 * tree_height_2) + (400+length) + (2*length+length*(2**0.5)))
                elif tree_2 == draw_maple:
                    print((0.8 * 3.14 * tree_height_1) + (0.8 * 3.14 * tree_height_2) + (400+length) + (2*length+length*(2**0.5)))

    else:
        t.backward(100)
        t.forward(100)
        tree_1 = generate_tree_1()
        t.forward(100)
        tree_2 = generate_tree_2()
        t.forward(100)
        tree_3 = generate_maple()
        if tree_3 is not None:
            print(tree_height_1, tree_height_2, tree_3)
            if tree_1 == draw_pine:
                if tree_2 == draw_pine:
                    print((2.8 * tree_height_1) + (2.8 * tree_height_2) + (0.8 * 3.14 * tree_3) + 400)
                elif tree_2 == draw_maple:
                    print((2.8 * tree_height_1) + (0.8 * 3.14 * tree_height_2) + (0.8 * 3.14 * tree_3) + 400)
            elif tree_1 == draw_maple:
                if tree_2 == draw_pine:
                    print((0.8 * 3.14 * tree_height_1) + (2.8 * tree_height_2) + (0.8 * 3.14 * tree_3) + 400)
                elif tree_2 == draw_maple:
                    print((0.8 * 3.14 * tree_height_1) + (0.8 * 3.14 * tree_height_2) + (0.8 * 3.14 * tree_3) + 400)
        else:
            print(tree_height_1, tree_height_2)
            if tree_1 == draw_pine:
                if tree_2 == draw_pine:
                    print((2.8 * tree_height_1) + (2.8 * tree_height_2) + 300)
                elif tree_2 == draw_maple:
                    print((2.8 * tree_height_1) + (0.8 * 3.14 * tree_height_2) + 300)
            elif tree_1 == draw_maple:
                if tree_2 == draw_pine:
                    print((0.8 * 3.14 * tree_height_1) + (2.8 * tree_height_2) + 300)
                elif tree_2 == draw_maple:
                    print((0.8 * 3.14 * tree_height_1) + (0.8 * 3.14 * tree_height_2) + 300)

main()
t.done()
