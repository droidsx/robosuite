# Adding a Robot

Here are all the files that one one robot is referenced in:

## Survey

These files are the important ones for adding a robot and using it in sim.

- robots/**init**.py
- input_utils.py (not strictly needed but nice for CLI testing)
- models/robots/manipulators
  - add to **init** (register the robot to the class type)
  - add a config file
- models/assets/robots and add a new folder with:
  - meshes (not needed)
  - obj_meshes (not needed)
  - no_texture_robot (not needed)
  - just ref meshes colocated with robot.xml
  - robot.xml

This might be nice for testing, we should be able to auto generate these demos in the future.

- demos/
  - demo_control.py
  - demo_device_control.py
  - demo_nvisii_modalities.py
  - demo_renderers.py

For docs can ignore and auto generate these types of docs from the robot registry later

- docs/
  - demos.md
  - modules/
    - robots.md
- robosuite/docs/source/robosuite.models.robots.manipulators.rst

# Example

Here's an example commit adding several new robots and grippers. https://github.com/ARISE-Initiative/robosuite/commit/4b4797ade722abe1a866a595f007545752e2914a#diff-74b6b1cfb8cae62aee05a9a4951d047d866ce8177cc1d4e2ad96c7eef2665f05

# From URDF

## Create Base Model

- drop URDF into mujoco
- save as .xml
- make sure you have the relevant meshes referenced in the URDF, you may need to change the paths to a local relative path
- you should have a folder named after the robot containing the meshes and the mujoco generated .xml

## Add Actuators

- add actuators according to manufacturers spec sheet
- reference them at relevant joints
