VectorsToPolar3D <-
function(vectors){
  num_data=dim(vectors);
  polar_vectors=vectors;
			
  x=vectors[,1];
  y=vectors[,2];
  z=vectors[,3];
		
  module2D=sqrt(x*x + y*y)
  colatitud=atan(module2D/z)
  colatitud[is.na(colatitud)] <- 0;
  colatitudBool <- colatitud >= 0;
  colatitud[colatitudBool == FALSE] <- colatitud[colatitudBool == FALSE]+pi;
  colatitud=ToSexagesimal3D(colatitud)
	
  longitud=ToSexagesimal3D(atan(y/x));
  longitud[is.na(longitud)] <- 0;
  gradesBool <- x >= 0;
  longitud[gradesBool == FALSE] <- longitud[gradesBool == FALSE]+180;
  gradesBool <- longitud >= 0;
  longitud[gradesBool == FALSE] <- longitud[gradesBool == FALSE]+360;
  
  polar_vectors=matrix(nrow=length(x),ncol=2);
  polar_vectors[,1]=colatitud;
  polar_vectors[,2]=longitud;
  return(polar_vectors);
}

