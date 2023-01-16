#This is an R script to estimate the generation of force in the gape of Iniopera using output from Blender
#Richard Dearden 15/09/2020

###########Calculating values#############

#Inputs
#Inputs taken from an output file generated in Blender

#Read in file with stuff 
setwd("/Users/rpdearden/Documents/Manuscripts/2_Sub_or_In_rev/Iniopera_muscles/Resubmission_PNAS/Iniop_Resub_Analyses/5_Iniop_Volume")
dataMax <- read.csv("InioperaSuctionMax_output.txt", sep=";", stringsAsFactors=FALSE)
dataOpt <- read.csv("InioperaSuctionOpt_output.txt", sep=";", stringsAsFactors=FALSE)

#Make data frame
df <- data.frame(#1
                 Angle = c(seq(0, 56.5, by=0.5),seq(56, 0.5, by=-0.5)),
                 #Aperture = data$Aperture_Area,
                 #Aperture.Percent = NA,
                 VolumeMax = dataMax$Pharynx_Volume,
                 VolumeMax.Percent = NA,
                 VolumeOpt = c(dataOpt$Pharynx_Volume,rep(NA,114)),
                 VolumeOpt.Percent = NA
                 )

#Function to fill out dataframe line-by-line for all rows
          for(i in 1:dim(df)[1])
            {
              #Percentages of initial gape
              df[i,3] <- (df[i,2]/df[1,2])*100
              df[i,5] <- (df[i,4]/df[1,4])*100
          }

###########Plotting values################

#Plot Volume change
pdf("Suction_Blender.pdf", width=6, height=6)
plot(df$VolumeMax.Percent,type="o",col="#7D9F35", pch="o", lwd=2, lty=1,ylim=c(80,260),cex=0.6,xlab="Frame",ylab="Percent initial",main ="Iniopera Pharyngeal volume change")
points(df$VolumeOpt.Percent, col="#A8383B", pch="*",cex=0.6)
lines(df$VolumeOpt.Percent, col="#A8383B", lty=1, lwd=2)
legend(71, 440, legend=c("Pharyngeal volume", "aperture area"), col=c("#7D9F35", "#A8383B"), lty=1, cex=0.6)
dev.off()



  