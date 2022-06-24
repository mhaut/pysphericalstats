\name{KurtosisModuleCoefficient3D}
\alias{KurtosisModuleCoefficient3D}
%- Also NEED an '\alias' for EACH other topic documented here.
\title{Calculation of the kurtosis coefficient of the modules in 3D}
\description{
   This function calculates the kurtosis coefficient of the modules in 3D, which characterizes the shape of the distribution from a set of input modules.
}
\usage{
KurtosisModuleCoefficient3D(modules)
}
%- maybe also 'usage' for other objects documented here.
\arguments{
  \item{modules}{Vector containing the values of the modules}
}
\details{
   One way to obtain a set of modules from X, Y and Z coordinates of the vectors is to use the \code{\link{LoadData3D}} function.
   
   The kurtosis coefficient is a measure of whether the data are flat or peaked relative to the normal distribution.
}
\value{
   The value of the kurtosis coefficient of all input modules
}
\references{
   Website \url{http://gim.unex.es/VecStatGraphs3D/}
}
\author{Felicisimo, A.M., \email{amfeli@unex.es},
Ruiz-Cuetos, J.C., \email{bilba_t@hotmail.com}, 
Polo, M.E., \email{mepolo@unex.es}, 
Cuartero, A., \email{acuartero@unex.es}, 
Rodriguez, P.G. \email{pablogr@unex.es}}


%% ~Make other sections like Warning with \section{Warning }{....} ~

\seealso{
   \code{\link{ArithmeticMean3D}}, \code{\link{StandardError3D}}, \code{\link{ModuleStandardDeviation3D}}, 
   \code{\link{ModuleVariance3D}}, \code{\link{ModulePopulationVariance3D}},
   \code{\link{ModulePopulationStandardDeviation3D}}, \code{\link{SkewnessModuleCoefficient3D}},
   \code{\link{AllModuleStatistics3D}}.
}
\examples{
   FileName<-system.file("data/XYZcoor.txt", package="VecStatGraphs3D")
   dat<-LoadData3D(FileName, Type=1)
   modules<-dat[,1]
   KurtosisModuleCoefficient3D(modules)
}
% Add one or more standard keywords, see file 'KEYWORDS' in the
% R documentation directory.
\keyword{module}