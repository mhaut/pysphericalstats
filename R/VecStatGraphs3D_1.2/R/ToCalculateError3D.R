ToCalculateError3D <-
function(vectors){
  num_data=dim(vectors);
  num_elements=num_data[1];
  x_coordinates=1:num_elements;
  y_coordinates=1:num_elements;
  z_coordinates=1:num_elements;
	
  x_coordinates<-vectors[,1]-vectors[,4];
  y_coordinates<-vectors[,2]-vectors[,5];
  z_coordinates<-vectors[,3]-vectors[,6];
		
  error=c(x_coordinates,y_coordinates,z_coordinates);
  dim(error)=c(num_elements,3);		
  return(error);
}

