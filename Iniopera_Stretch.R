#This is an R script to estimate the generation of force in the gape of Iniopera using output from Blender
#Richard Dearden 21/04/2022

###########Calculating values#############

#Inputs
#Inputs taken from an output file generated in Blender

#Read in file with stuff 
setwd("/Users/rpdearden/Documents/Manuscripts/2_Sub_or_In_rev/Iniopera_muscles/Resubmission_PNAS/Iniop_Resub_Analyses/2_Iniop_Gape")
data3deg <- read.csv("Iniopera_SF_output_3deg.txt", sep=";", stringsAsFactors=FALSE)
data6deg <- read.csv("Iniopera_SF_output_6deg.txt", sep=";", stringsAsFactors=FALSE)
data9deg <- read.csv("Iniopera_SF_output_9deg.txt", sep=";", stringsAsFactors=FALSE)



#Make data frame
#I boshed this so that rows would fill with NAs where needed: sure there's a more elegant way!
#AnMA = anterior MA, SoMA = Suborbital MA
#Orig. rest3.AnMAAnt = c(data3deg$MAAnt.MAA1.,rep(NA,40))
df <- data.frame(#1
                 Angle = seq(3, 80, by=0.5),
                 rest3.AnMAAnt = c(data3deg$MAAnt.MAA1.),
                 rest3.AnMAPost = c(data3deg$MAPost.MAA2.),
                 rest3.SoMAAnt = c(data3deg$SoMAAnt.SoMAA1.),
                 rest3.SoMAPost = c(data3deg$SoMAPost.SoMAA2.),
                 rest6.AnMAAnt = c(rep(NA,6),data6deg$MAAnt.MAA1.),
                 rest6.AnMAPost = c(rep(NA,6),data6deg$MAPost.MAA2.),
                 rest6.SoMAAnt = c(rep(NA,6),data6deg$SoMAAnt.SoMAA1.),
                 rest6.SoMAPost = c(rep(NA,6),data6deg$SoMAPost.SoMAA2.),
                 rest9.AnMAAnt = c(rep(NA,12),data9deg$MAAnt.MAA1.),
                 rest9.AnMAPost = c(rep(NA,12),data9deg$MAPost.MAA2.),
                 rest9.SoMAAnt = c(rep(NA,12),data9deg$SoMAAnt.SoMAA1.),
                 rest9.SoMAPost = c(rep(NA,12),data9deg$SoMAPost.SoMAA2.)
                 )


###########Plotting values################

#Plot Stretch factors
#This plots double the actual angle on x axis (due to .5 degree increments). Because I'm lazy I fixed in post...
pdf("Iniopera_gape.pdf", width=6, height=6)
#3ant
plot(df$rest3.AnMAAnt,type="p",col="#7D9F35", pch=1,ylim=c(100,220),cex=0.3,xlab="Angle",ylab="Strain Factor",main ="Iniopera Mechanical Advantage")
points(df$rest3.AnMAPost, col="#7D9F35", pch=2,cex=0.3)
#lines(df$rest3.AnMAPost, col="#7D9F35", lty=1)
#3suborb
points(df$rest3.SoMAAnt, col="#7D9F35", pch=3,cex=0.3)
#lines(df$rest3.SoMAAnt, col="#7D9F35", lty=1)
points(df$rest3.SoMAPost, col="#7D9F35", pch=4,cex=0.3)
#lines(df$rest3.SoMAPost, col="#7D9F35", lty=1)
#6ant
points(df$rest6.AnMAAnt, col="#A8383B", pch=1,cex=0.3)
#lines(df$rest6.AnMAAnt, col="#A8383B", lty=1)
points(df$rest6.AnMAPost, col="#A8383B", pch=2,cex=0.3)
#lines(df$rest6.AnMAPost, col="#A8383B", lty=1)
#6suborb
points(df$rest6.SoMAAnt, col="#A8383B", pch=3,cex=0.3)
#lines(df$rest6.SoMAAnt, col="#A8383B", lty=1)
points(df$rest6.SoMAPost, col="#A8383B", pch=4,cex=0.3)
#lines(df$rest6.SoMAPost, col="#A8383B", lty=1)
#9ant
points(df$rest9.AnMAAnt, col="#572A72", pch=1,cex=0.3)
#lines(df$rest9.AnMAAnt, col="#572A72", lty=1)
points(df$rest9.AnMAPost, col="#572A72", pch=2,cex=0.3)
#lines(df$rest9.AnMAPost, col="#572A72", lty=1)
#9suborb
points(df$rest9.SoMAAnt, col="#572A72", pch=3,cex=0.3)
#lines(df$rest9.SoMAAnt, col="#572A72", lty=1)
points(df$rest9.SoMAPost, col="#572A72", pch=4,cex=0.3)
#lines(df$rest9.SoMAPost, col="#572A72", lty=1)
#Add stuff
hist(x, freq = FALSE, add = TRUE)
legend(1, 220, legend=c("3 deg.", "6 deg.", "9 deg."),col=c("#7D9F35", "#A8383B", "#572A72"), lty=1, cex=0.8)
dev.off()