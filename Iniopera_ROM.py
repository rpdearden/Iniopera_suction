###Python script to calculate intersection of objects###

####
####RPDearden_01/03/22
#### Adapted from here https://blender.stackexchange.com/questions/71289/using-overlap-to-check-if-two-meshes-are-intersecting

#Load stuff
import bpy
import bmesh
import object_print3d_utils
from object_print3d_utils import mesh_helpers
from mathutils.bvhtree import BVHTree

scene = bpy.context.scene

#Make Output file and write header
header = 'Degrees; Intersection; \n'
output_file = open('../rpdearden/Documents/Manuscripts/2_Sub_or_In_rev/Iniopera_muscles/ROM/InioperaROM_output.txt', 'w')
output_file.write(header)
output_file.close()

#Define objects
BasiH = bpy.data.objects['Basihyal']
CeratoH = bpy.data.objects['Ceratohyal_R']
Text = bpy.data.objects['Angle']

#set frames etc
angle_start = 0
angle = 0
angle_max = 60
start = 1
end = 30
counter = 1
counter = start

#Define materials:
mat_No_Intersect = bpy.data.materials['CeratoH_Green']
mat_Yes_Intersect = bpy.data.materials['CeratoH_Red']


#Set up counter
while counter < (end + 1):
    bpy.context.scene.frame_set(counter)
    file_path = '../rpdearden/Documents/Manuscripts/2_Sub_or_In_rev/Iniopera_muscles/ROM/InioperaROMPics'
    file_name = file_path + str(counter) + 'jpg'
    angle = (angle_max / end) * counter
    Text.data.body = 'Angle: ' + str(angle) + ' deg.'
    counter = counter + 1

    
    #Make bmeshes to hold objects
    bm_BasiH = mesh_helpers.bmesh_copy_from_object(BasiH, apply_modifiers=True)
    bm_CeratoH = mesh_helpers.bmesh_copy_from_object(CeratoH, apply_modifiers=True)
    
    #Make BVH tree from bmeshes
    BasiH_BVHtree = BVHTree.FromBMesh(bm_BasiH)
    CeratoH_BVHtree = BVHTree.FromBMesh(bm_CeratoH)
    
    #intersection?
    intersections = BasiH_BVHtree.overlap(CeratoH_BVHtree)
    
    if intersections != []:
        CeratoH.data.materials[0] = mat_Yes_Intersect
    else:
        CeratoH.data.materials[0] = mat_No_Intersect

    #Write to output file
    output_file = open('../rpdearden/Documents/Manuscripts/2_Sub_or_In_rev/Iniopera_muscles/ROM/InioperaROM_output.txt', 'a')
    
    if intersections != []:
        text = str(angle) + ';' + 'Yes' + '\n'     
    else:
        text = str(angle) + ';' + 'No' + '\n'     
    
    output_file.write(text)
    output_file.close()
    
    bpy.data.scenes['Scene'].render.filepath = file_name
    bpy.ops.render.render(animation=False, write_still=True, use_viewport=True)
    

