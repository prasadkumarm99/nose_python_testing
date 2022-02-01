from proj.circle import Circle

def test_create_pos_int_radius():
    c = Circle(5)
    assert c.radius == 5

def test_create_pos_float_radius():
    c = Circle(2.5)
    assert c.radius == 2.5

# def test_create_neg_int_radius():
#     c = Circle



# if __name__ == "__main__":
#     nose.main()