_HEIGHT = 0.625


class Table():
  height = _HEIGHT

  def __init__(self,
               bullet_client,
               base_position=[0, 0, 0],
               base_orientation=[0, 0, 0, 1]):
    self._p = bullet_client
    self._base_position = base_position
    self._base_orientation = base_orientation

    self._body_id = self._p.loadURDF("table/table.urdf",
                                     basePosition=self._base_position,
                                     baseOrientation=self._base_orientation)

    self._p.changeVisualShape(self._body_id, -1, rgbaColor=[1, 1, 1, 1])