bl_info = {
    "name": "Round Vertices",
    "blender": (4, 0, 0),
    "category": "Object",
}

import bpy
import bmesh
from bpy.props import FloatProperty
from bpy.props import BoolProperty
from bpy.types import Operator

class OBJECT_OT_round_vertices(Operator):
	bl_label = "Round Vertices"
	bl_idname = "object.round_vertices"
	bl_description = "Round vertices to the nearest step"
	bl_options = {'REGISTER', 'UNDO'}

	rounding: FloatProperty(
		name="Rounding",
		description="Rounding to the nearest value",
		default=0.01,
		min=0,
		max=1,
		step=0.001,
	)

	auto_merge: BoolProperty(
		name="Auto-Merge",
		description="Automatically merge vertices by distance",
		default=False,
	)

	def execute(self, context):
		obj = context.active_object
		if obj.mode == 'EDIT':
			bm = bmesh.from_edit_mesh(obj.data)
			# Get selected vertices
			selected_verts = [v for v in bm.verts if v.select] or bm.verts
			# Round vertices
			for v in selected_verts:
				v.co.x = round(v.co.x / self.rounding) * self.rounding
				v.co.y = round(v.co.y / self.rounding) * self.rounding
				v.co.z = round(v.co.z / self.rounding) * self.rounding
			# Auto-Merge
			if self.auto_merge:
				bmesh.ops.remove_doubles(bm, verts=selected_verts, dist=self.rounding)
			bmesh.update_edit_mesh(obj.data)
		else:
			self.report({'WARNING'}, "Object is not in edit mode")
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(OBJECT_OT_round_vertices.bl_idname)

def register():
	bpy.utils.register_class(OBJECT_OT_round_vertices)
	bpy.types.VIEW3D_MT_edit_mesh_vertices.append(menu_func)

def unregister():
	bpy.utils.unregister_class(OBJECT_OT_round_vertices)
	bpy.types.VIEW3D_MT_edit_mesh_vertices.remove(menu_func)


if __name__ == "__main__":
	register()
