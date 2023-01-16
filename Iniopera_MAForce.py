
###################################################################################################
###Dearden et al. 2022
###Python script to extract coordinates of empties at each point during jaw opening for Iniopera mechanical advantage estimates###
###RPDearden - last updated 07/04/2022
###################################################################################################


#Load stuff
import bpy

#Name empties
Jaw_Artic= bpy.data.objects['Empty.Jaw.Artic']
AM_Meck= bpy.data.objects['Empty.AddMand.Mk']
AM_NcAnt= bpy.data.objects['Empty.AddMand.NcAnt']
AM_NcPost= bpy.data.objects['Empty.AddMand.NcPost']
#Cbr= bpy.data.objects['Empty.coracobr']
Teeth_ant= bpy.data.objects['Empty.teeth.ant']
Teeth_mid= bpy.data.objects['Empty.teeth.mid']
Teeth_post= bpy.data.objects['Empty.teeth.post']

#Make Gape angle
Text = bpy.data.objects['Angle']
degree_sign = u"\N{DEGREE SIGN}"

#Make Output file and write header
header = 'Gape;Jaw_Artic_X;Jaw_Artic_Y;Jaw_Artic_Z;AM_Meck_X;AM_Meck_Y;AM_Meck_Z;AM_NcAnt_X;AM_NcAnt_Y;AM_NcAnt_Z;AM_NcPost_X;AM_NcPost_Y;AM_NcPost_Z;Teeth_ant_X;Teeth_ant_Y;Teeth_ant_Z;Teeth_mid_X;Teeth_mid_Y;Teeth_mid_Z;Teeth_post_X;Teeth_post_Y;Teeth_post_Z \n'
#Cbr_X;Cbr_Y;Cbr_Z;
output_file = open('../rpdearden/Documents/Manuscripts/2_Sub_or_In_rev/Iniopera_muscles/Resubmission_PNAS/Iniop_Resub_Analyses/3_Iniop_Biteforce/InioperaMAForce_output.txt', 'w')
output_file.write(header)
output_file.close()

#Sets gape distances, number of frames, and counter
resting_gape = 0
gape = 0
gape_max = 80
start = 1
end = 160
counter = 1
counter = start

#Print results to file
while counter < (end + 1):
    bpy.context.scene.frame_set(counter)
    file_path = '../rpdearden/Documents/Manuscripts/2_Sub_or_In_rev/Iniopera_muscles/Resubmission_PNAS/Iniop_Resub_Analyses/3_Iniop_Biteforce/Iniop_Biteforce'
    file_name = file_path + str(counter) + 'jpg'
    gape = (gape_max / end) * counter
    Text.data.body = ' Gape angle: ' + str(gape) + degree_sign
    counter = counter + 1
    
    #Below uses world to translation to give coordinates in world  space rather than local space
    output_file = open('../rpdearden/Documents/Manuscripts/2_Sub_or_In_rev/Iniopera_muscles/Resubmission_PNAS/Iniop_Resub_Analyses/3_Iniop_Biteforce/InioperaMAForce_output.txt', 'a')
    text = 'Nr. ' + str(gape) + ';' + str(Jaw_Artic.matrix_world.to_translation()[0]) + ';' + str(Jaw_Artic.matrix_world.to_translation()[1]) + ';' + str(Jaw_Artic.matrix_world.to_translation()[2]) + ';' + str(AM_Meck.matrix_world.to_translation()[0]) + ';' + str(AM_Meck.matrix_world.to_translation()[1]) + ';' + str(AM_Meck.matrix_world.to_translation()[2]) + ';' + str(AM_NcAnt.matrix_world.to_translation()[0]) + ';' + str(AM_NcAnt.matrix_world.to_translation()[1]) + ';' + str(AM_NcAnt.matrix_world.to_translation()[2]) + ';'+ str(AM_NcPost.matrix_world.to_translation()[0]) + ';' + str(AM_NcPost.matrix_world.to_translation()[1]) + ';' + str(AM_NcPost.matrix_world.to_translation()[2]) + ';'+ str(Teeth_ant.matrix_world.to_translation()[0]) + ';' + str(Teeth_ant.matrix_world.to_translation()[1]) + ';' + str(Teeth_ant.matrix_world.to_translation()[2]) + ';'+ str(Teeth_mid.matrix_world.to_translation()[0]) + ';' + str(Teeth_mid.matrix_world.to_translation()[1]) + ';' + str(Teeth_mid.matrix_world.to_translation()[2]) + ';'+ str(Teeth_post.matrix_world.to_translation()[0]) + ';' + str(Teeth_post.matrix_world.to_translation()[1]) + ';' + str(Teeth_post.matrix_world.to_translation()[2]) + '\n'
    #';' + str(Cbr.matrix_world.to_translation()[0]) + ';' + str(Cbr.matrix_world.to_translation()[1]) + ';' + str(Cbr.matrix_world.to_translation()[2]) +
    output_file.write(text)
    output_file.close()
    
   # bpy.data.scenes['Scene'].render.filepath = file_name
   # bpy.ops.render.render(animation=False, write_still=True, use_viewport=True)