RayleighTest3D <-
function(coord, Alpha = 0.05){
  
  TableChicuadrado<-c(7.815,9.348,11.34,12.84,16.27,17.73)
  x<-coord[,1];
  y<-coord[,2];
  z<-coord[,3];
  n_elements=length(x);
  m_module=MeanModule3D(coord);
  m_module=3*m_module
  
  if(sum(Alpha == c(0.05, 0.025, 0.01, 0.005, 0.001, 0.0005)) == 0){
	print("Incorrect Alpha");
  }
  else{
	Tcol<-(1:6)[Alpha == c(0.05, 0.025, 0.01, 0.005, 0.001, 0.0005)]
	if(n_elements>=10){
	  if(m_module<TableChicuadrado[Tcol]){
		print(paste("Rayleigh Test:",m_module,"<",TableChicuadrado[Tcol]," Hypothesis of uniformity accepted"));
	  }
	  else{
		print(paste("Rayleigh Test:",m_module,">",TableChicuadrado[Tcol]," Hypothesis of uniformity rejected"));
	  } 
	}
	else{
	  print("Rayleigh Test: Size of sample incorrect");
	}
  }
}

