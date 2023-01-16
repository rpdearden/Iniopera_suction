#This is an R script to estimate the generation of force in the gape of Iniopera using output from Blender
#Richard Dearden 21/04/2022

###########Calculating values#############

#Inputs
#Inputs taken from an output file generated in Blender

#Read in file with stuff 
setwd("/Users/rpdearden/Documents/Manuscripts/2_Sub_or_In_rev/Iniopera_muscles/Resubmission_PNAS/Iniop_Resub_Analyses/3_Iniop_Biteforce")
data <- read.csv("InioperaMAForce_output.txt", sep=";", stringsAsFactors=FALSE)

#Specific tension(N/cm2)
SpecTen <- 28.9
#SA of muscle attachment surface (in cm2).
#Worked out in Blender (see methods)
AM.SA = 0.1118
#Muscle force (N)
AM.f <- AM.SA*SpecTen

#Make data frame
df <- data.frame(
                 Angle = data$Gape,  #1               
                 Jaw_ArticX = data$Jaw_Artic_X,#2
                 Jaw_ArticY = data$Jaw_Artic_Y,#3
                 Jaw_ArticZ = data$Jaw_Artic_Z,#4
                 AddMandMeckX = data$AM_Meck_X,#5
                 AddMandMeckY = data$AM_Meck_Y,#6
                 AddMandMeckZ = data$AM_Meck_Z,#7
                 AddMandNcAntX = data$AM_NcAnt_X,#8
                 AddMandNcAntY = data$AM_NcAnt_Y,#9
                 AddMandNcAntZ = data$AM_NcAnt_Z,#10
                 AddMandNcPostX = data$AM_NcPost_X,#11
                 AddMandNcPostY = data$AM_NcPost_Y,#12
                 AddMandNcPostZ = data$AM_NcPost_Z,#13
                 ToothFrontX = data$Teeth_ant_X,#14
                 ToothFrontY = data$Teeth_ant_Y,#15
                 ToothFrontZ = data$Teeth_ant_Z,#16
                 ToothMidX = data$Teeth_mid_X,#17
                 ToothMidY = data$Teeth_mid_Y,#18
                 ToothMidZ = data$Teeth_mid_Z,#19
                 ToothPostX = data$Teeth_post_X,#20
                 ToothPostY = data$Teeth_post_Y,#21
                 ToothPostZ = data$Teeth_post_Z,#22
                 AddMandAvX = NA,#23
                 AddMandAvY = NA,#24
                 AddMandAvZ = NA,#25
                 ALinX = NA,#26
                 ALinY = NA,#27
                 ALinZ = NA,#28
                 ALin.length = NA,#29
                 MAddX = NA,#30
                 MAddY = NA,#31
                 MAddZ = NA,#32
                 MAdd.length = NA,#33
                 Theta = NA,#34
                 ELinX = NA,#35
                 ELinY = NA,#36
                 ELinZ = NA,#37
                 ELin.length = NA,#38
                 OutAntX = NA,#39
                 OutAntY = NA,#40
                 OutAntZ = NA,#41
                 OutAnt.Length = NA,#42
                 OutMidX = NA,#43
                 OurMidY = NA,#44
                 OutMidZ = NA,#45
                 OutMid.Length = NA,#46
                 OutPostX = NA,#47
                 OutPostY = NA,#48
                 OutPostZ = NA,#49
                 OutPost.Length = NA,#50
                 MA.Ant = NA,#51
                 MA.Mid = NA,#52
                 MA.Post = NA,#53
                 ForceOut.Ant = NA,#54
                 ForceOut.Mid = NA,#55
                 ForceOut.Post = NA#56

                 )

#Function to fill out dataframe line-by-line for all rows
          for(i in 1:dim(df)[1])
            {
            #Work out addition of coords for MAdd  
            #Didn't actually end up using this as was wrong but was too lazy to change column numbers
            #Not incorporated so please ignore (and don't judge me plz)
            df[i,23] <- df[i,8] + df[i,11]
            df[i,24] <- df[i,9] + df[i,12]
            df[i,25] <- df[i,10] + df[i,13]
            
            #inlever vector(ALin) from articular joint to centroid of adductor XYZ
              #Inlever length (same throughout, varies a bit due to rounding I think)
              #Pythagoras to work out magnitude
              df[i,26] <- df[i,5] - df[i,2]
              df[i,27] <- df[i,6] - df[i,3]
              df[i,28] <- df[i,7] - df[i,4]
              df[i,29] <- sqrt(sum((c(df[i,26],df[i,27],df[i,28])^2)))
             
              #MA vector(MAdd) from centroid of meck adductor XYZ to added mandibular adductor vectors
              #Add X,Y, and Z of two (ant and Post) Madd vectors
              #MA length (elongates)
              #Pythagoras to work out magnitude
              df[i,30] <- (df[i,5] - df[i,8]) + (df[i,5] - df[i,11])
              df[i,31] <- (df[i,6] - df[i,9]) + (df[i,6] - df[i,12])
              df[i,32] <- (df[i,7] - df[i,10]) + (df[i,7] - df[i,13])
              df[i,33] <- sqrt(sum((c(df[i,30],df[i,31],df[i,32])^2)))
              
              #Angle between MAdd and Inlever (Theta) using formula to find angle between two vectors
              #180/pi converts from radians -> degrees
              df[i,34] <- (180/pi)*acos((sum(c(df[i,26],df[i,27],df[i,28])*c(df[i,30],df[i,31],df[i,32])))/(df[i,29]*df[i,33]))
              
              #EL effective inlever vector XYZ, calculated from above using SOH and pi/180 to go degrees -> radians
              #EL length
              df[i,35] <- df[i,26]*sin(df[i,34]*pi/180)
              df[i,36] <- df[i,27]*sin(df[i,34]*pi/180)
              df[i,37] <- df[i,28]*sin(df[i,34]*pi/180)
              df[i,38] <- sqrt(sum(c(df[i,35],df[i,36],df[i,37])^2))
               
              #Outlever anteriormost 
              #OutAnt length
              df[i,39] <- df[i,14] - df[i,2]
              df[i,40] <- df[i,15] - df[i,3]
              df[i,41] <- df[i,16] - df[i,4]
              df[i,42] <- sqrt(sum((c(df[i,39],df[i,40],df[i,41])^2))) 
              
              #Outlever middlemost 
              #OutMid length
              df[i,43] <- df[i,17] - df[i,2]
              df[i,44] <- df[i,18] - df[i,3]
              df[i,45] <- df[i,19] - df[i,4]
              df[i,46] <- sqrt(sum((c(df[i,43],df[i,44],df[i,45])^2))) 
              
              #Outlever posteriormost 
              #OutPost length
              df[i,47] <- df[i,20] - df[i,2]
              df[i,48] <- df[i,21] - df[i,3]
              df[i,49] <- df[i,22] - df[i,4]
              df[i,50] <- sqrt(sum((c(df[i,47],df[i,48],df[i,49])^2)))
              
              #Mechanical advantage
              df[i,51] <- df[i,38]/df[i,42]
              df[i,52] <- df[i,38]/df[i,46]
              df[i,53] <- df[i,38]/df[i,50]

              #Force exerted at point estimated
              df[i,54] <- AM.f*df[i,51]
              df[i,55] <- AM.f*df[i,52]
              df[i,56] <- AM.f*df[i,53]
          }

write.csv(df,"Iniopera_MA_Force_Data.csv")

###########Plotting values################

#Plot Mechanical advantages
pdf("MA_Blender.pdf", width=6, height=6)
plot(df$MA.Post,type="o",col="#7D9F35", pch="o", lty=1,ylim=c(0,0.7),cex=0.5,xlab="Frame",ylab="MA",main ="Iniopera Mechanical Advantage")
points(df$MA.Mid, col="#A8383B", pch="*",cex=0.5)
lines(df$MA.Mid, col="#A8383B", lty=1)
points(df$MA.Ant, col="#572A72", pch="+",cex=0.5)
lines(df$MA.Ant, col="#572A72", lty=1)
legend(1, 1.2, legend=c("Posterior", "Middle", "Anterior"),col=c("#7D9F35", "#A8383B", "#572A72"), lty=1, cex=0.8)
dev.off()

#Plot Force
pdf("Force_Blender.pdf", width=6, height=6)
plot(df$ForceOut.Post,type="o",col="#7D9F35", pch="o", lty=1,ylim=c(0,2),cex=0.5,xlab="Frame",ylab="Force Out (N)",main ="Iniopera Force Out")
points(df$ForceOut.Mid, col="#A8383B", pch="*",cex=0.5)
lines(df$ForceOut.Mid, col="#A8383B", lty=1)
points(df$ForceOut.Ant, col="#572A72", pch="+",cex=0.5)
lines(df$ForceOut.Ant, col="#572A72", lty=1)
legend(1, 4.5, legend=c("Posterior", "Middle", "Anterior"), col=c("#7D9F35", "#A8383B", "#572A72"), lty=1, cex=0.8)
dev.off()

# plot the first curve by calling plot() function
# First curve is plotted
#plot(xdata, y1, type="o", col="blue", pch="o", lty=1, ylim=c(0,110) )

# Add second curve to the same plot by calling points() and lines()
# Use symbol '*' for points.
#points(xdata, y2, col="red", pch="*")
#lines(xdata, y2, col="red",lty=2)

# Add Third curve to the same plot by calling points() and lines()
# Use symbol '+' for points.
#points(xdata, y3, col="dark red",pch="+")
#lines(xdata, y3, col="dark red", lty=3)


  