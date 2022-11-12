world=[[],[],[],[]]
collision_group = dict()
def add_object(o, depth):
    world[depth].append(o)

def add_objects(ol,depth):
    world[depth] += ol

def all_objects():
    for layer in world:
        for o in layer:
            yield o #yield된 함수를 호출한 곳이 for문 같은 것이면 generator

def remove_object(o,depth):
    for layer in world:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            del o
            return
    raise ValueError('Trying destroy non existing object')
    # world[depth].remove(o) # 단순히 리스트로부터 삭제하는 것
    # del o #메모리까지 삭제

def clear():
    for o in all_objects():
        del o
    for layer in world:
        layer.clear()
def add_collison_pairs(a,b,group):
    if group not in collision_group:
        print('add new group')
        collision_group[group]=[[],[]]

    if a:
        if type(a)==list:
            collision_group[group][0]+= a
        else:
            collision_group[group][0].append(a)

    if b:
        if type(b)==list:
            collision_group[group][1]+= b
        else:
            collision_group[group][1].append(b)


def all_collision_pairs():
    for group,pairs_list in collision_group.items():
        for a in pairs_list[0]:
            for b in pairs_list[1]:
                yield a,b,group

def remove_collision_object(o):
    for pairs in collision_group.values():
        if o in pairs[0]: pairs[0].remove(o)
        elif o in pairs[1]:pairs[1].remove(o)