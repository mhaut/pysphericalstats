\name{VecStatGraphs3D-package}
\alias{VecStatGraphs3D-package}
\alias{VecStatGraphs3D}
\docType{package}
\title{Vector analysis using graphical and analytical methods in 3D}
\description{
   This package performs a 3D statistical analysis, both numerical and 
   graphic, of a set of vectors. Since a vector has three components (a module and two angles) 
   vector analysis is performed in two stages: modules are analyzed by means of linear 
   statistics and orientations are analyzed by spherical statistics. 
   Tests and spherical statistic parameters are accompanied by a full range of 
   graphing: vector maps, density maps,distribution modules and angles. 
   The tests, spherical statistic parameters and graphs allow us detecting another distribution 
   properties (I.e. anisotropy) and outliers.
}
\details{
\tabular{ll}{
Package: \tab VecStatGraphs3D\cr
Type: \tab Package\cr
Version: \tab 1.2\cr
Date: \tab 2012-08-09\cr
License: \tab GPL-3\cr
LazyLoad: \tab yes\cr
}

}

\author{
   Juan Carlos Ruiz Cuetos, Maria Eugenia Polo Garcia, Pablo Garcia Rodriguez.

   Maintainer: Pablo Garcia Rodriguez <pablogr@unex.es>
}
\references{
  Fisher N.I. , Lewis T. , Embleton, B.J.J. (1987) Statistical analysis of spherical data. Cambridge. Cambridge University Press.

  Website \url{http://gim.unex.es/VecStatGraphs3D/}
}

\keyword{ package }
\seealso{
   \code{\link{AllAngleStatistics}}, \code{\link{AllModuleStatistics3D}}, 
   \code{\link{DrawModuleAndAngleDistribution3D}}, \code{\link{DrawDensity3D}}, 
   \code{\link{RayleighTest3D}}.
}