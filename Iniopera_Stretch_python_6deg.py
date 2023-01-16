###################################################################################################
#
#	Muscle extension script for Iniopera with a 6 degree starting gape, Dearden et al. 2022
#
###################################################################################################

#This script is modified from Lautenschlager (2015) by RPD
#Last edited 21/04/22

#This also requires armatures to be added to the cylinders (might have been lost between blender 2.7 and 2.8
#I think Lautenschlager used two armatures with a hinge at the jaw joint
#However, I don't see why this is necessary - all the armatures do is allow the cylinder to stretch and all measurements come from the cylinder itself.
#Instead I set up cylinders 008 and 037 with a single armature along its length


#Load stuff
import bpy
from math import sqrt

#RPD Names cylinders for different muscles
MAA1 = bpy.data.objects['M.Add_A_Tube'] #Anterior MAA
MAA2= bpy.data.objects['M.Add_P_Tube'] #Posterior MAA
SoMAA1 = bpy.data.objects['Suborb.M.Add_A_Tube'] #Anterior Suborb MAA
SoMAA2= bpy.data.objects['Suborb.M.Add_P_Tube'] #Posterior Suborb MAA


Text = bpy.data.objects['Angle']
degree_sign = u"\N{DEGREE SIGN}"

#RPD Names bars in bar charts for muscles
bar_MAA1 = bpy.data.objects['Bar_1'] #Anterior MAA
bar_MAA2 = bpy.data.objects['Bar_2'] #Posterior MAA
bar_SoMAA1 = bpy.data.objects['Bar_3'] #Anterior Suborb MAA
bar_SoMAA2 = bpy.data.objects['Bar_4'] #Posterior Suborb MAA



#RPD# Works out the diagonal distance across the body by doing sqrt(x^2+y^2+z^2) to give the starting dimensions

orig_dim_MAA1 = sqrt(MAA1.dimensions.z**2 + MAA1.dimensions.y**2 + MAA1.dimensions.x**2)
orig_dim_MAA2 = sqrt(MAA2.dimensions.z**2 + MAA2.dimensions.y**2 + MAA2.dimensions.x**2)
orig_dim_SoMAA1 = sqrt(SoMAA1.dimensions.z**2 + SoMAA1.dimensions.y**2 + SoMAA1.dimensions.x**2)
orig_dim_SoMAA2 = sqrt(SoMAA2.dimensions.z**2 + SoMAA2.dimensions.y**2 + SoMAA2.dimensions.x**2)



#Make output file with muscle headers
header = 'Gape; MAAnt(MAA1); MAPost(MAA2); SoMAAnt(SoMAA1); SoMAPost(SoMAA2);\n'
output_file = open('../rpdearden/Documents/Manuscripts/2_Sub_or_In_rev/Iniopera_muscles/Resubmission_PNAS/Iniop_Resub_Analyses/2_Iniop_Gape/results_6deg/Iniopera_SF_output_6deg.txt', 'w')

output_file.write(header)
output_file.close()

#Set stretch factors
stretch_factor1 = 1.0
stretch_factor2 = 1.3
stretch_factor3 = 1.7

#Sets all rest lengths to 0
rest_length_MAA1 = 0
rest_length_MAA2 = 0
rest_length_SoMAA1 = 0
rest_length_SoMAA2 = 0


#Sets gape distances, number of frames, and counter
resting_gape = 6
gape = 0
gape_max = 80
start = 1
end = 160
counter = 1
counter = start

#RPD Sets material colours on the basis of the colours already there
#RPD Note I changed (0.0, 0.0, 0.0) to (0.0, 0.0, 0.0, 1.0) due to differences in Blender 2,8 onwards

material_colour_MAA1 = bpy.data.materials['a_MAA1_mat']
material_colour_MAA1.diffuse_color = (0.0, 0.0, 0.0, 1.0)
material_colour_MAA2 = bpy.data.materials['a_MAA2_mat']
material_colour_MAA2.diffuse_color = (0.0, 0.0, 0.0, 1.0)
material_colour_SoMAA1 = bpy.data.materials['a_SoMAA1_mat']
material_colour_SoMAA1.diffuse_color = (0.0, 0.0, 0.0, 1.0)
material_colour_SoMAA2 = bpy.data.materials['a_SoMAA2_mat']
material_colour_SoMAA2.diffuse_color = (0.0, 0.0, 0.0, 1.0)

material_colour_bar_MAA1 = bpy.data.materials['bar1_mat']
material_colour_bar_MAA2 = bpy.data.materials['bar2_mat']
material_colour_bar_SoMAA1 = bpy.data.materials['bar3_mat']
material_colour_bar_SoMAA2 = bpy.data.materials['bar4_mat']



#Sets off video

#RPD# Makes jpgs - I have changed file path

#RPD# This makes the gape at any given frame the required fraction of the total gape	

#RPD# This makes the label (.Text) list the current angle of gape

#RPD#Adds one to counter

#RPD# This works out the diagonal distance "current dimensions" across the body by doing Ã(x^2+y^2+z^2) to give the original lengths

#RPD# This sets z dimensions to 0 for each muscle if gape is smaller than resting gape	

#RPD# This sets the resting lengths based on their dimensions at the beginning



while counter < (end + 1):
	bpy.context.scene.frame_set(counter)
	file_path = '../rpdearden/Documents/Manuscripts/2_Sub_or_In_rev/Iniopera_muscles/Resubmission_PNAS/Iniop_Resub_Analyses/2_Iniop_Gape/results_6deg/Stretch6deg_'
	file_name = file_path + str(counter) + 'tif'
	gape = (gape_max / end) * counter
	Text.data.body = ' Gape angle: ' + str(gape) + degree_sign
	counter = counter + 1
	curr_dim_MAA1 = sqrt(MAA1.dimensions.z**2 + MAA1.dimensions.y**2 + MAA1.dimensions.x**2)
	curr_dim_MAA2 = sqrt(MAA2.dimensions.z**2 + MAA2.dimensions.y**2 + MAA2.dimensions.x**2)
	curr_dim_SoMAA1 = sqrt(SoMAA1.dimensions.z**2 + SoMAA1.dimensions.y**2 + SoMAA1.dimensions.x**2)
	curr_dim_SoMAA2 = sqrt(SoMAA2.dimensions.z**2 + SoMAA2.dimensions.y**2 + SoMAA2.dimensions.x**2)

	
	if(gape < resting_gape):	
		bar_MAA1.dimensions.z = 0 
		bar_MAA2.dimensions.z = 0 
		bar_SoMAA1.dimensions.z = 0 
		bar_SoMAA2.dimensions.z = 0 

		

	if(gape == resting_gape):
		rest_length_MAA1 = curr_dim_MAA1
		rest_length_MAA2 = curr_dim_MAA2
		rest_length_SoMAA1 = curr_dim_SoMAA1
		rest_length_SoMAA2 = curr_dim_SoMAA2

		

#RPD# Whack results back into file (path changed)
	output_file = open('../rpdearden/Documents/Manuscripts/2_Sub_or_In_rev/Iniopera_muscles/Resubmission_PNAS/Iniop_Resub_Analyses/2_Iniop_Gape/results_6deg/Iniopera_SF_output_6deg.txt', 'a')

#RPD# If gape is greater than or equal to resting gape...

	if(gape >= resting_gape):

#RPD# Creates text object "Fraction of gape; percentage open for each muscle and writes to output; 
		text = 'Nr. ' + str(gape) + ';' + str(curr_dim_MAA1 / rest_length_MAA1 * 100) + ';' + str(curr_dim_MAA2 / rest_length_MAA2 * 100) + ';' + str(curr_dim_SoMAA1 / rest_length_SoMAA1 * 100) + ';' + str(curr_dim_SoMAA2 / rest_length_SoMAA2 * 100) + '\n'
		output_file.write(text)

#RPD#This makes the colours change dependent on the stretch factor
		if curr_dim_MAA1 >= (stretch_factor1 * rest_length_MAA1):
			material_colour_MAA1.diffuse_color = material_colour_bar_MAA1.diffuse_color =  (0.0, 1.0, 0.0, 1.0)
		if curr_dim_MAA1 >= (stretch_factor2 * rest_length_MAA1):
			material_colour_MAA1.diffuse_color = material_colour_bar_MAA1.diffuse_color =  (1.0, 0.75, 0.0, 1.0)
		if curr_dim_MAA1 >= (stretch_factor3 * rest_length_MAA1):
			material_colour_MAA1.diffuse_color = material_colour_bar_MAA1.diffuse_color =  (1.0, 0.0, 0.0, 1.0)
		if curr_dim_MAA2 >= (stretch_factor1 * rest_length_MAA2):
			material_colour_MAA2.diffuse_color = material_colour_bar_MAA2.diffuse_color =  (0.0, 1.0, 0.0, 1.0)
		if curr_dim_MAA2 >= (stretch_factor2 * rest_length_MAA2):
			material_colour_MAA2.diffuse_color = material_colour_bar_MAA2.diffuse_color =  (1.0, 0.75, 0.0, 1.0)
		if curr_dim_MAA2 >= (stretch_factor3 * rest_length_MAA2):
			material_colour_MAA2.diffuse_color = material_colour_bar_MAA2.diffuse_color =  (1.0, 0.0, 0.0, 1.0)
		if curr_dim_SoMAA1 >= (stretch_factor1 * rest_length_SoMAA1):
			material_colour_SoMAA1.diffuse_color = material_colour_bar_SoMAA1.diffuse_color =  (0.0, 1.0, 0.0, 1.0)
		if curr_dim_SoMAA1 >= (stretch_factor2 * rest_length_SoMAA1):
			material_colour_SoMAA1.diffuse_color = material_colour_bar_SoMAA1.diffuse_color =  (1.0, 0.75, 0.0, 1.0)
		if curr_dim_SoMAA1 >= (stretch_factor3 * rest_length_SoMAA1):
			material_colour_SoMAA1.diffuse_color = material_colour_bar_SoMAA1.diffuse_color =  (1.0, 0.0, 0.0, 1.0)
		if curr_dim_SoMAA2 >= (stretch_factor1 * rest_length_SoMAA2):
			material_colour_SoMAA2.diffuse_color = material_colour_bar_SoMAA2.diffuse_color =  (0.0, 1.0, 0.0, 1.0)
		if curr_dim_SoMAA2 >= (stretch_factor2 * rest_length_SoMAA2):
			material_colour_SoMAA2.diffuse_color = material_colour_bar_SoMAA2.diffuse_color =  (1.0, 0.75, 0.0, 1.0)
		if curr_dim_SoMAA2 >= (stretch_factor3 * rest_length_SoMAA2):
			material_colour_SoMAA2.diffuse_color = material_colour_bar_SoMAA2.diffuse_color =  (1.0, 0.0, 0.0, 1.0)


		#RPD# This sets the dimensions of the bars. Calculate factor by doing distance from 100-150%, and dividing it by 0.5
		bar_MAA1.dimensions.z = 0.04288 * ((curr_dim_MAA1/rest_length_MAA1) - 1.0) 
		bar_MAA2.dimensions.z = 0.04288 * ((curr_dim_MAA2/rest_length_MAA2) - 1.0) 
		bar_SoMAA1.dimensions.z = 0.04288 * ((curr_dim_SoMAA1/rest_length_SoMAA1) - 1.0) 
		bar_SoMAA2.dimensions.z = 0.04288 * ((curr_dim_SoMAA2/rest_length_SoMAA2) - 1.0) 
		
		output_file.close()

#		bpy.data.scenes['Scene'].render.filepath = file_name
#		bpy.ops.render.render(animation=False, write_still=True, use_viewport=True)