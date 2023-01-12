import easysim

from yacs.config import CfgNode as CN

_C = easysim.cfg

# ---------------------------------------------------------------------------- #
# Simulation config
# ---------------------------------------------------------------------------- #
_C.SIM.USE_DEFAULT_STEP_PARAMS = False

_C.SIM.TIME_STEP = 0.001

_C.SIM.INIT_VIEWER_CAMERA_POSITION = (0.1, 0.0, 1.0)

_C.SIM.INIT_VIEWER_CAMERA_TARGET = (0.0, 0.0, 0.0)

# ---------------------------------------------------------------------------- #
# Environment config
# ---------------------------------------------------------------------------- #
_C.ENV = CN()

_C.ENV.TARGET_POSITION_X = 0.1

_C.ENV.TARGET_POSITION_Y = 0.0

_C.ENV.DISPLAY_TARGET = True

_C.ENV.RANDOM_SEED = 0

##### Table #####
_C.ENV.TABLE_LENGTH = 1.1

_C.ENV.TABLE_WIDTH = 0.7

_C.ENV.TABLE_HEIGHT = _C.SIM.GROUND_PLANE.DISTANCE

_C.ENV.TABLE_X_OFFSET = -0.3

# Notes: We need all the collisions, so all the objects should have the same collision filter
_C.ENV.COLLISION_FILTER_TABLE = 1

##### Panda #####
_C.ENV.PANDA_CONTROL_TYPE = "ee_inc"

_C.ENV.PANDA_BASE_POSITION = (-0.6, 0.0, 0.0)

_C.ENV.PANDA_BASE_ORIENTATION = (0.0, 0.0, 0.0, 1.0)

_C.ENV.PANDA_INITIAL_POSITION = (0.00, 0.41, 0.00, -1.85, 0.00, 2.26, 0.79, 0.04, 0.04)

_C.ENV.COLLISION_FILTER_PANDA = 1

# Notes: These values follow the PandaPickAndPlace-V3 of panda-gym
_C.ENV.PANDA_MAX_FORCE = (87.0, 87.0, 87.0, 87.0, 12.0, 120.0, 120.0, 170.0, 170.0)

_C.ENV.PANDA_POSITION_GAIN = (0.01,) * 9

_C.ENV.PANDA_VELOCITY_GAIN = (1.0,) * 9

##### Primitive Objects #####

_C.ENV.NUM_PRIMITIVE_OBJECTS = 2

_C.ENV.COLLISION_FILTER_PRIMITIVE_OBJECT = 1

_C.ENV.PRIMITIVE_OBJECT_TYPE = "Box"

_C.ENV.PRIMITIVE_OBJECT_SIZE = 0.04

_C.ENV.PRIMITIVE_OBJECT_MASS = 1.0

_C.ENV.PRIMITIVE_OBJECT_BASE_POSITION = [(0.125, -0.1, _C.ENV.PRIMITIVE_OBJECT_SIZE / 2), (0.125, 0.1, _C.ENV.PRIMITIVE_OBJECT_SIZE / 2)]

_C.ENV.PICKED_OBJECT_IDX = 1

##### MANO Hand #####

_C.ENV.MANO_POSE_RANDOMIZATION = True

if not _C.ENV.MANO_POSE_RANDOMIZATION:

    _C.ENV.MANO_MODEL_FILENAME = "20200709-subject-01_left"

    _C.ENV.MANO_POSE_FILENAME = "gestureIL/data/mano_poses/pointing_7_left.npy"

    _C.ENV.MANO_INITIAL_TARGET = _C.ENV.PRIMITIVE_OBJECT_BASE_POSITION[_C.ENV.PICKED_OBJECT_IDX]
    
    _C.ENV.MANO_INITIAL_BASE = (
        _C.ENV.MANO_INITIAL_TARGET[0] + 0.1,
        _C.ENV.MANO_INITIAL_TARGET[1],
        _C.ENV.PRIMITIVE_OBJECT_SIZE + 0.05
    )

    _C.ENV.MANO_FINAL_TARGET = (
        _C.ENV.TARGET_POSITION_X,
        _C.ENV.TARGET_POSITION_Y,
        _C.ENV.PRIMITIVE_OBJECT_SIZE / 2
    )

    _C.ENV.MANO_FINAL_BASE = (
        _C.ENV.MANO_FINAL_TARGET[0] + 0.1,
        _C.ENV.MANO_FINAL_TARGET[1],
        _C.ENV.PRIMITIVE_OBJECT_SIZE + 0.05
    )
    
_C.ENV.COLLISION_FILTER_MANO = 1

_C.ENV.MANO_TRANSLATION_MAX_FORCE = (50.0,) * 3

_C.ENV.MANO_TRANSLATION_POSITION_GAIN = (0.2,) * 3

_C.ENV.MANO_TRANSLATION_VELOCITY_GAIN = (10.0,) * 3

_C.ENV.MANO_ROTATION_MAX_FORCE = (5.0,) * 3

_C.ENV.MANO_ROTATION_POSITION_GAIN = (0.2,) * 3

_C.ENV.MANO_ROTATION_VELOCITY_GAIN = (1.0,) * 3

_C.ENV.MANO_JOINT_MAX_FORCE = (0.5,) * 45

_C.ENV.MANO_JOINT_POSITION_GAIN = (0.1,) * 45

_C.ENV.MANO_JOINT_VELOCITY_GAIN = (1.0,) * 45

##### YCB Objects #####

##### Offscreen Rendering #####

_C.ENV.RENDER_OFFSCREEN = False

_C.ENV.RENDER_DIR = str(_C.ENV.PICKED_OBJECT_IDX) + '_test'

_C.ENV.OFFSCREEN_RENDERER_CAMERA_WIDTH = 128

_C.ENV.OFFSCREEN_RENDERER_CAMERA_HEIGHT = 128

_C.ENV.OFFSCREEN_RENDERER_CAMERA_VERTICAL_FOV = 60.0

_C.ENV.OFFSCREEN_RENDERER_CAMERA_NEAR = 0.1

_C.ENV.OFFSCREEN_RENDERER_CAMERA_FAR = 10.0

_C.ENV.OFFSCREEN_RENDERER_CAMERA_POSITION = (0.1, 0.0, 1.0)

_C.ENV.OFFSCREEN_RENDERER_CAMERA_TARGET = (0.0, 0.0, 0.0)

##### Demonstration Storing #####

_C.ENV.STORE_DEMONSTRATION = False

_C.ENV.STORE_DIR = str(_C.ENV.PICKED_OBJECT_IDX)


get_cfg = easysim.get_cfg

get_config_from_args = easysim.get_config_from_args