# Rhea wheeled biped robot

<img src="../../images/rhea_render.jpg" align="right" width="300">

<!-- [![PyPI version](https://img.shields.io/pypi/v/rhea_description)](https://pypi.org/project/rhea_description/) -->

<!-- :warning: **This module has been deprecated in favor of [`robot_descriptions`](https://github.com/robot-descriptions/robot_descriptions.py).** -->

URDF description for the Rhea wheeled biped. 

## Python module

This module helps retrieve Rhea's model from a Python program. Import it by:

```python
import rhea_description
```

It then provides the following paths:

<dl>
    <dt>
        <code>rhea_description.path</code>
    </dt>
    <dd>
        Path to the "rhea_description" folder itself.
    </dd>
    <dt>
        <code>rhea_description.meshes_path</code>
    </dt>
    <dd>
        Path to the "meshes" folder.
    </dd>
    <dt>
        <code>rhea_description.urdf_path</code>
    </dt>
    <dd>
        Path to the URDF file of the model.
    </dd>
</dl>

## Acknowledgements

Repository structure copied from [Upkie](https://github.com/tasts-robots/upkie_description).