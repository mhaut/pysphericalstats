CorrectType3D <-
function(type,data_){
  if(length(data_) == 2 && type==2)
	return (TRUE);
  if(length(data_) == 3 && type==1)
	return (TRUE);
  if(length(data_) == 6 && type==3)
	return (TRUE);
  return (FALSE);
}

