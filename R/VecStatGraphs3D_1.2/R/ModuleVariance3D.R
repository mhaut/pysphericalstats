ModuleVariance3D <-
function(modules){
  m_arit=ArithmeticMean3D(modules);
  n=NumberOfElements3D(modules);
  return((sum((modules-m_arit)^2))/(n-1));
}

