Arrows3D <-
function(a, b, colo = "blue", headLength = 0.3, headWidth = 0.5, width = 1, transparent =FALSE, plane = "XY"){
  
  require(rgl)
  #a<-c(0,0,0)
  if(plane=="XY"){
    hN<-c(0,0,1)
  }
  if(plane=="YZ"){
    hN<-c(1,0,0)
  }
  if(plane=="XZ"){
    hN<-c(0,1,0)
  }
 
  aL=sqrt(sum((b-a)*(b-a)))
  aU=(b-a)/aL;
  hP=c(aU[2]*hN[3]-aU[3]*hN[2],-1*(aU[1]*hN[3]-aU[3]*hN[1]),aU[1]*hN[2]-aU[2]*hN[1])
  hP=hP/sqrt(sum(hP*hP));

  quads3d(rbind(b,b-aU*headLength+hP*headLength/2*headWidth,b-aU*headLength,b-aU*headLength-hP*headLength/2*headWidth),color=colo,lit=transparent)
  lines3d(rbind(a,b-aU*headLength),color=colo,lwd=width)				
}

