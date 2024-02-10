def triangle(big_side,small_side_1,small_side_2):
    """
    this function is for making tringale.
    the first variable is the big side and the other two variblesare the small sides.
    """

    result=small_side_1+small_side_2
    if result>big_side:
        print(f"you can make a triangle with this sides [{big_side} , {small_side_1} , {small_side_2}]")
    else:
        print(f"you can't make a triangle with this sides [{big_side} , {small_side_1} , {small_side_2}]")


big_side=float(input("please enter the big side: "))
small_side_1=float(input("please enter the small-side-1: "))
small_side_2=float(input("please enter the small-side-2: "))


triangle(big_side , small_side_1 , small_side_2)


