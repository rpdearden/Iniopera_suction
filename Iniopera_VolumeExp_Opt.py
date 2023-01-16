###Python script to estimate volume of pharynx in Iniopera using a polyhedron###
###For optimal gape of 28 degrees
###From Dearden et al 2023


#Load stuff
import bpy
import bmesh
import object_print3d_utils
from object_print3d_utils import mesh_helpers

#Name objects
Pharynx= bpy.data.objects['PharynxVol.001']
#Aperture= bpy.data.objects['PharynxAperture']


#Make Gape angle
Text = bpy.data.objects['Angle']

#Make Output file and write header
header = 'Gape;Pharynx_Volume \n'
output_file = open('../rpdearden/Documents/Manuscripts/2_Sub_or_In_rev/Iniopera_muscles/Resubmission_PNAS/Iniop_Resub_Analyses/5_Iniop_Volume/InioperaSuctionOpt_output.txt', 'w')
output_file.write(header)
output_file.close()


#Sets gape distances, number of frames, and counter
resting_gape = 0
gape = 0
#gape_max = 25.5
gape_max = 51.5
start = 1
end = 206
counter = 1
counter = start

#Print results to file
while counter < (end + 1):
    bpy.context.scene.frame_set(counter)
    file_path = '../rpdearden/Documents/Manuscripts/2_Sub_or_In_rev/Iniopera_muscles/Resubmission_PNAS/Iniop_Resub_Analyses/5_Iniop_Volume/Iniop_vol_Opt/Iniop_Vol_Opt'
    file_name = file_path + str(counter) + 'jpg'
    gape = (gape_max / end) * counter
    Text.data.body = ' Gape angle: ' + str(gape) + 'deg.'
    counter = counter + 1
    
    #Do area and Volume
    #Calculate Volume and Area using 3D printing toolbox tool
    bmPharynx = mesh_helpers.bmesh_copy_from_object(Pharynx, apply_modifiers=True)
    Volume=bmPharynx.calc_volume()#Calculate volume
    #bmAperture = mesh_helpers.bmesh_copy_from_object(Aperture, apply_modifiers=True)
    #Area = sum(f.calc_area() for f in bmAperture.faces)
    
    #bmPharynx.faces.ensure_lookup_table() #This would be necessary to run below
    #Pharynx.data.polygons[0].select = True #Do this and tab into edit mode to check face index
    #Area=bmPharynx.faces[0].calc_area()# Calculate area of oral aperture by selecting anteriormost face [index=0]

    #Below uses world to translateion to give coordinates in world  space rather than local space
    output_file = open('../rpdearden/Documents/Manuscripts/2_Sub_or_In_rev/Iniopera_muscles/Resubmission_PNAS/Iniop_Resub_Analyses/5_Iniop_Volume/Iniop_vol_Opt/Iniop_Vol_Opt.txt','a')
    text = 'Nr. ' + str(gape) + ';' + str(Volume) + '\n'
    output_file.write(text)
    output_file.close()
    #Render it
    bpy.data.scenes['Scene'].render.filepath = file_name
    bpy.ops.render.render(animation=False, write_still=True, use_viewport=True)
    
