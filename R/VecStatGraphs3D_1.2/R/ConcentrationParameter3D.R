ConcentrationParameter3D <-
function(coord){
  x<-coord[,1];
  y<-coord[,2];
  z<-coord[,3];
  n_elements=length(x);
        
  mean_module=(MeanModule3D(coord));
  if(mean_module<0.53){
	parameter=(2*mean_module)+(mean_module^3)+(5*(mean_module^5)/6);
  }
  if((mean_module>=0.53)&(mean_module<=0.85)){
	parameter=-0.4+(1.39*mean_module)+(0.43/(1-mean_module));
  }
  if(mean_module>=0.85){
	parameter=1/((mean_module^3)-(4*mean_module^2)+3*mean_module);
	}
  return(parameter);
}

