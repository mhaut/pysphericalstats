LoadData3D <-
function(FileName, Type = 1){
  data_=ReadFromFile3D(FileName);
  if(length(data_) > 1){
    if(CorrectType3D(Type,data_) == FALSE){
      switch (Type,print("Error, the file is not of Rectangular type"),
              print("Error, the file is not of Polar coordinates type"),
              print("Error, the file is not of (X origin, Y origin, Z origin) - (X end, Y end, Z end) type"));
    }    
    else {       
      if(Type==1){
          polar_vectors=VectorsToPolar3D(data_);	
          rectangular_vectors=data_;
	  }
      if(Type==2){
          rectangular_vectors=VectorsToRectangular3D(data_);
          if(dim(data_)==3){
			polar_vectors=data_[,(2:3)];
		  }
		  else{
			polar_vectors=data_;
		  }
	  }
      if(Type==3){
		error=ToCalculateError3D(data_);
        polar_vectors=VectorsToPolar3D(error);
        rectangular_vectors=error;
      }
      
	  x<-rectangular_vectors[,1];
	  y<-rectangular_vectors[,2];
	  z<-rectangular_vectors[,3];
	  module=sqrt(x*x + y*y + z*z);
		
      num_data=dim(data_);
      res=matrix(nrow=num_data[1],ncol=13); 
      res[,1]=module;
	  res[,2]=polar_vectors[,1];
      res[,3]=polar_vectors[,2];
      res[,4]=rectangular_vectors[,1];
      res[,5]=rectangular_vectors[,2];
	  res[,6]=rectangular_vectors[,3];
      res[1,7]=Type;
      res[2,7]=1111;
      if(Type==3){
        res[2,7]=9999;
        res[,8]=data_[,1];
        res[,9]=data_[,2];
        res[,10]=data_[,3];
		res[,11]=data_[,4];
        res[,12]=data_[,5];
        res[,13]=data_[,6];
      }
      return(res);
    }
  }    
}

