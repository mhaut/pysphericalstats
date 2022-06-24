\name{AllModuleStatistics3D}
\alias{AllModuleStatistics3D}
%- Also NEED an '\alias' for EACH other topic documented here.
\title{Calculation of All Statistics of the Modules.}
\description{
   This function calculates several statistics from a set of input modules.
}
\usage{
AllModuleStatistics3D(modules, ndig=4)
}
%- maybe also 'usage' for other objects documented here.
\arguments{
  \item{modules}{Vector containing the values of the modules}
  \item{ndig}{Integer value that indicates the decimal places. The default value is 4}
}
\details{
   One way to get a set of modules from the X, Y and Z in the original position and end position
   (Coordinates X, Y and Z vector) or the colatitude and longitude, using the \code{\link{LoadData3D}} function.
   
   The statistics calculated are: \code{Number Of Elements, Max Value, Min Value, Range, Module Sum, Mean Arithmetic, Standard Error, Module Standard Deviation, Module Variance, Module Population Variance, Module Population Standard Deviation.}
}
\value{
   The value All Module Statistics of all input modules.
}
\references{
   Website \url{http://gim.unex.es/VecStatGraphs3D/}
}

\author{Ruiz-Cuetos, J.C., \email{bilba_t@hotmail.com}, Felicisimo, A.M., \email{amfeli@unex.es}, 
Cuartero, A., \email{acuartero@unex.es}, Polo, M.E., \email{mepolo@unex.es}, 
Rodriguez, P.G. \email{pablogr@unex.es}}
%% ~Make other sections like Warning with \section{Warning }{....} ~

\seealso{
   \code{\link{NumberOfElements3D}}, \code{\link{MaxValue3D}}, \code{\link{MinValue3D}}, \code{\link{Range3D}},
   \code{\link{ModuleSum3D}}, \code{\link{ArithmeticMean3D}}, \code{\link{StandardError3D}},
   \code{\link{ModuleStandardDeviation3D}}, \code{\link{ModuleVariance3D}}, \code{\link{ModulePopulationVariance3D}},
   \code{\link{ModulePopulationStandardDeviation3D}}.
}
\examples{
   FileName<-system.file("data/XYZcoor.txt", package="VecStatGraphs3D")
   dat<-LoadData3D(FileName, Type=1)
   modules<-dat[,1]
   AllModuleStatistics3D(modules, ndig=4)
}
% Add one or more standard keywords, see file 'KEYWORDS' in the
% R documentation directory.
\keyword{module}