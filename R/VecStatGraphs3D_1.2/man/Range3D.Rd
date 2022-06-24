\name{Range3D}
\alias{Range3D}
%- Also NEED an '\alias' for EACH other topic documented here.
\title{Calculation of the Range of the modules.}
\description{
   This function calculates the Range (Difference between maximum and minimum value of the module) of a set of modules
}
\usage{
Range3D(modules)
}
%- maybe also 'usage' for other objects documented here.
\arguments{
  \item{modules}{Vector containing the values of the module}
}
\details{
   One way to get a set of modules from the X, Y and Z in the original position and end position
   (Coordinates X, Y and Z vector) or the colatitude and longitude, using the \code{\link{LoadData3D}} function.
}
\value{
   The range value of all input modules.
}
\references{
  Website \url{http://gim.unex.es/VecStatGraphs3D/}
}
\author{Ruiz-Cuetos, J.C., \email{bilba_t@hotmail.com}, Polo, M.E., \email{mepolo@unex.es}, Rodriguez, P.G. \email{pablogr@unex.es}}


%% ~Make other sections like Warning with \section{Warning }{....} ~

\seealso{
   \code{\link{NumberOfElements3D}}, \code{\link{MaxValue3D}}, \code{\link{MinValue3D}}, \code{\link{AllModuleStatistics3D}},
   \code{\link{ModuleSum3D}}, \code{\link{ArithmeticMean3D}}, \code{\link{StandardError3D}},
   \code{\link{ModuleStandardDeviation3D}}, \code{\link{ModuleVariance3D}}, \code{\link{ModulePopulationVariance3D}},
   \code{\link{ModulePopulationStandardDeviation3D}}.
}
\examples{
   FileName<-system.file("data/XYZcoor.txt", package="VecStatGraphs3D")
   dat<-LoadData3D(FileName, Type=3)
   modules<-dat[,1]
   Range3D(modules)
}
% Add one or more standard keywords, see file 'KEYWORDS' in the
% R documentation directory.
\keyword{module}
