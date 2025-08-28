from assign_5 import *
from random import randint as rd

admin = Admin("Admin", "admin@email.com")

def gen_instructor_l(inst_l):
    path = ["path-A", "path-C", "path-B", "path-D", "path-E"]
    for i in range(1, 28):
        inst_l.append(Instructor(f"Instructor {i}", f"instr{i}@email.com", path[rd(0, 4)]))
    return inst_l


def gen_learner_l(lrn_l):
    path = ["path-A", "path-B", "path-C", "path-D", "path-E"]
    for i in range(1, 28):
        lrn_l.append(Learner(f"Learner {i}", f"lrn{i}@email.com", path[rd(0, 4)]))
    return lrn_l

inst = []
lrn = []

inst = gen_instructor_l(inst)
lrn = gen_learner_l(lrn)

for i in inst:
    admin.assign_role(i, "Instructor")

for i in range(0, len(lrn)):
    admin.assign_role(lrn[i], "Student")
    if ((i + 1) % 4 == 0):
        admin.assign_role(lrn[i], "Student Facilitator")

for i in inst + lrn:
    admin.get_user_info(i)
