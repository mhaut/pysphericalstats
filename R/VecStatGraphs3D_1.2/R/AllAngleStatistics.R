AllAngleStatistics <-
function(coord){
  x<-coord[,1];
  y<-coord[,2];
  z<-coord[,3];
  n_elements=length(x)
  
  sphericalErros<-SphericalStandardError3D(coord)
  m_direction<-MeanDirection3D(coord);
  m_module<-MeanModule3D(coord);
  vm_parameter<-ConcentrationParameter3D(coord);
		
	
  print("*************************************************************");
  print("****                                                     ****");
  print("****            SPHERICAL STATISTICS - ANGLES             ****");
  print("****                                                     ****");
  print("*************************************************************");
	
  print(paste("SPHERICAL STANDARD ERROR = ",sphericalErros));
  print(paste("MEAN MODULE = ",m_module));
  print(paste("CONCENTRATION PARAMETER = ",vm_parameter));
  print(paste("COLATITUDE = ",m_direction[1],", LATITUDE = ",m_direction[2]));
  }


