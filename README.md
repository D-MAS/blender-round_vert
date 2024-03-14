# blender-round_vert
## HOW TO USE
1. Open Blender
2. Go to Edit -> Preferences -> Addons

![blender_zOyvmL23Mf](https://github.com/D-MAS/blender-round_vert/assets/57054077/9a66f169-ab6b-467f-b9dd-919dd7ace3f0)

3. Click Install...
4. Navigate to the install directory
5. Check the checkbox for the plugin

![image](https://github.com/D-MAS/blender-round_vert/assets/57054077/58da7b9a-148f-4f03-a216-1a4630aa69a0)

6. In Edit Mode, click Vertex -> Round Vertices

<br><br><br><br><br><br><br><br><br>
confession, i made most of this with copilot, the only part that is genuinely mine, is in line 39 where i changed this
```py
			selected_verts = [v for v in bm.verts if v.select]
```
to
```py
			selected_verts = [v for v in bm.verts if v.select] or bm.verts
```
master programmer
