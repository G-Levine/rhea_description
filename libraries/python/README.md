# Upkie wheeled biped robot

<img src="https://user-images.githubusercontent.com/1189580/169594012-2d685579-2b66-4470-9def-57bd0656b420.png" align="right" width="300">

URDF description for the [Upkie](https://www.youtube.com/watch?v=NO_TkHGS0wQ) wheeled biped. See also:

- [3D print files](https://www.printables.com/model/127831-upkie-wheeled-biped-robot/files)
- [Build instructions](https://www.printables.com/model/127831-upkie-wheeled-biped-robot)

Upkie's head derives from the chassis of the [mjbots quad](https://github.com/mjbots/quad).

## Python module

This module helps retrieve Upkie's model from a Python program. Assuming we import it by:

```python
import upkie_description
```

We can then use the following paths:

<dl>
    <dt>
        <code>upkie_description.path</code>
    </dt>
    <dd>
        Path to the ``upkie_description`` folder itself.
    </dd>
    <dt>
        <code>upkie_description.meshes_path</code>
    </dt>
    <dd>
        Path to the ``meshes`` folder.
    </dd>
    <dt>
        <code>upkie_description.urdf_path</code>
    </dt>
    <dd>
        Path to the ``upkie.urdf`` URDF file of the model.
    </dd>
</dl>
