DrawModuleAndAngleDistribution3D <-
function(dat,Long = FALSE, hW = 0.5, hL = 0.3, plane, BarSlider = FALSE){
  require(tcltk)
  require(rgl)
  value=5;
  hWstart=hW;
  hLstart=hL;
  valAux=value;
  cont=1;

  while(cont!=5){
    
    open3d(windowRect=c(100,100,800,800))
    bg3d("white")  

    module=dat[,1];
    Cx=dat[,4];
    Cy=dat[,5];
    Cz=dat[,6];
  
    R=sqrt((sum(Cx)*sum(Cx))+(sum(Cy)*sum(Cy))+(sum(Cz)*sum(Cz)));
    meanX<-sum(Cx)/R;
    meanY<-sum(Cy)/R;
    meanZ<-sum(Cz)/R;
  
    #meanModule <- sqrt((meanX*meanX)+(meanY*meanY)+(meanZ*meanZ));
    meanModule <- ArithmeticMean3D(dat[,1])
    #meanModule <- MeanModule3D(dat[,4:6])
  
    meanDirection <- (MeanDirection3D(dat[,4:6]))
    #radianC <- ToRadians(MeanAngle(colatitud))
    #radianA <- ToRadians(MeanAngle(azimuth))
  
    if(meanDirection[1] < 0){
      meanDirection[1]<-meanDirection[1]+180
    }
    if(meanX < 0) {
      meanDirection[2]<-meanDirection[2]+180
    }
    if(meanDirection[2] < 0){
      meanDirection[2]<-meanDirection[2]+360
    }
  
    #print(meanModule)
    #print(meanDirection[1])
    #print(meanDirection[2])
  
    Ax <- meanModule*sin(ToRadians3D(meanDirection[1]))*cos(ToRadians3D(meanDirection[2])) 
    Ay <- meanModule*sin(ToRadians3D(meanDirection[1]))*sin(ToRadians3D(meanDirection[2])) 
    Az <- meanModule*cos(ToRadians3D(meanDirection[1]))
  
    #print(Ax)
    #print(Ay)
    #print(Az)
  
    spheres3d(0,0,0,radius=max(module),color="black",front="line",back="line",lwd=1,smooth=TRUE,lit=TRUE,line_antialias = FALSE,alpha=0.2)

    x <- c(0,max(module),0,0)
    y <- c(0,0,max(module),0)
    z <- c(0,0,0,max(module))
    labels <- c("", "X", "Y", "Z")
    i <- c(1,2,1,3,1,4)

    text3d(x,y,z,labels,adj=0.8,cex=1.5,font=2,color="black")
    segments3d(x[i],y[i],z[i],lwd=3)
  
    #cero<-seq(length=length(Cx),from=0,by=0)
    #cero<-array(cero,dim=c(length(Cx),3))
    #Arrows3D(cero,c(Cx,Cy,Cz),headWidth = hW, headLength = hL, plane = plane) 
  
    pb <- tkProgressBar(title = "Drawing ...", min = 0, max = length(Cx), width = 300)  
    for(i in 1:length(Cx)){
      Arrows3D(c(0,0,0),c(Cx[i],Cy[i],Cz[i]),headWidth = hW, headLength = hL, plane = plane)
      setTkProgressBar(pb, i, label=paste( round(i/length(Cx)*100, 0),"% done"))
    }
    close(pb)

    #cero<-seq(length=length(Cx),from=0,by=0)
    #
    #xx<-array(c(cero,Cx),dim=c(length(Cx),2)) 
    #yy<-array(c(cero,Cy),dim=c(length(Cx),2))
    #zz<-array(c(cero,Cz),dim=c(length(Cx),2))
    #
    ##Traspuesta
    #xx<-aperm(xx)
    #yy<-aperm(yy)
    #zz<-aperm(zz)
  
    #Representacion de Meadia Angulo
    Arrows3D(c(0,0,0),c(Ax,Ay,Az),colo="red",width=2.5, headWidth = 1.5*hW, headLength = 1.5*hL, plane = plane)

    if(Long==TRUE){
      f <- select3d()
      keep <- f(Cx,Cy,Cz)
      mod<-sqrt(Cx[keep]*Cx[keep] + Cy[keep]*Cy[keep] + Cz[keep]*Cz[keep]); 
      text3d(Cx[keep],Cy[keep],Cz[keep], texts=round(mod,2),font=1, cex=0.8)
    }
    #rgl.postscript("persp3db.pdf","pdf")
 
    #while(valAux==value){
    
    if(BarSlider==TRUE){
      valAux<-Slider(value);
    }
    #}
    val<-5-valAux
    value<-valAux
    if(val!=0){
      hW<-hWstart
      hL<-hLstart
      if(val<0){
        hW=hW*(Mod(val)*2)
        hL=hL*(Mod(val)*2)
      }
      else{
        hW=hW/(Mod(val)*2)
        hL=hL/(Mod(val)*2)
      }
    }
    else{
      hW<-hWstart
      hL<-hLstart
    }
    cont=cont+1
    if(BarSlider==FALSE){
      cont=5
    }
    else{
       rgl.close()
    }
  }
}

