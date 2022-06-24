AllModuleStatistics3D <-
function(modules){
  n_elemetns=NumberOfElements3D(modules);
  max_value=MaxValue3D(modules);
  min_value=MinValue3D(modules);
  range_value=Range3D(modules);
  module_sum=ModuleSum3D(modules);
  m_arithmetic= ArithmeticMean3D(modules);
  s_error=StandardError3D(modules);
  s_d_module=ModuleStandardDeviation3D(modules);
  v_module=ModuleVariance3D(modules);
  s_d_module_p=ModulePopulationStandardDeviation3D(modules);
  v_module_p=ModulePopulationVariance3D(modules);
			
  print("************************************************************");
  print("****                                                    ****");
  print("****           LINEAR  STATISTICS - MODULES             ****");
  print("****                                                    ****");
  print("************************************************************");
	
  print(paste("NUMBER OF ELEMENTS = ",n_elemetns));   
  print(paste("MAX VALUE = ",max_value));   
  print(paste("MIN VALUE = ",min_value));
  print(paste("RANGE = ",range_value)); 
  print(paste("MODULES SUM = ",module_sum));
  print(paste("ARITHMETIC MEAN = ",m_arithmetic));
  print(paste("STANDARD ERROR = ",s_error));
  print(paste("MODULE STANDARD DEVIATION = ",s_d_module));
  print(paste("MODULE VARIANCE = ",v_module));
  print(paste("MODULE POPULATION VARIANCE = ",v_module_p));
  print(paste("MODULE POPULATION STANDARD DEVIATION = ",s_d_module_p));
}

