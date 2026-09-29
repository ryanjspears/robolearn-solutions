from robot import arm, gripper, world, sim
import numpy as np

print("Start configuration:", arm.q)

# 1. Move to the ready pose: [base, shoulder, elbow, wrist] in radians
READY = [0.0, 0.5, 1.5, 1.14]
arm.set_joint_targets(READY)
sim.wait(1.0)            # physics has to run for the arm to move!
print("After 1 s:", np.round(arm.q, 3))

# 2. TODO: turn the base to face the cup.
#    Hint: world.cup.position -> [x, y, z]



# 3. TODO: close the gripper, then open it again.

