def has_collision(obj0, obj1):  # obj has get_collision_info, returning (x, y, w, h)
    obj0 = obj0.get_collision_info()
    obj1 = obj1.get_collision_info()
    a_hit_x = obj0[0] + 2
    a_hit_y = obj0[1] + 2
    a_hit_w = obj0[2] - 2
    a_hit_h = obj0[3] - 2
    b_hit_x = obj1[0] + 2
    b_hit_y = obj1[1] + 2
    b_hit_h = obj1[2] - 2
    b_hit_w = obj1[3] - 2
    # AABB collision detection
    a_hit_x < b_hit_x + b_hit_w and a_hit_x + a_hit_w > b_hit_x and a_hit_y < b_hit_y + b_hit_h and a_hit_h + a_hit_y > b_hit_y
