VectorsToRectangular3D <-
function(vectors){
  num_data=dim(vectors);
  rectangular_vectors=vectors;
  if(num_data==3){
	module=vectors[,1]
	colatitud=vectors[,2]
	longitud=vectors[,3]
  }
  else{
	module=1;
	colatitud=vectors[,1]
	longitud=vectors[,2]
  }
  
  x<-sin(ToRadians3D(colatitud))*cos(ToRadians3D(longitud))*module
  y<-sin(ToRadians3D(colatitud))*sin(ToRadians3D(longitud))*module
  z<-cos(ToRadians3D(colatitud))*module
  
  rectangular_vectors=matrix(nrow=length(colatitud),ncol=3);
  rectangular_vectors[,1]<-x;
  rectangular_vectors[,2]<-y;
  rectangular_vectors[,3]<-z;
  return(rectangular_vectors);
}

