\name{ArithmeticMean3D}
\alias{ArithmeticMean3D}
%- Also NEED an '\alias' for EACH other topic documented here.
\title{Calculation of Mean Arithmetic modules.}
\description{
   This function calculates the arithmetic mean of a set of modules
}
\usage{
ArithmeticMean3D(modules)
}
%- maybe also 'usage' for other objects documented here.
\arguments{
  \item{modules}{Vector containing the values of the modules}
}
\details{
   One way to get a set of modules from the X, Y and Z in the original position and end position
   (Coordinates X, Y and Z vector) or the colatitude and longitude, using the \code{\link{LoadData3D}} function.
}
\value{
   The arithmetic mean value of all input modules.
}
\references{
   Website \url{http://gim.unex.es/VecStatGraphs3D/}
}
\author{Ruiz-Cuetos, J.C., \email{bilba_t@hotmail.com}, Polo, M.E., \email{mepolo@unex.es}, Rodriguez, P.G. \email{pablogr@unex.es}}

%% ~Make other sections like Warning with \section{Warning }{....} ~

\seealso{
   \code{\link{NumberOfElements3D}}, \code{\link{MaxValue3D}}, \code{\link{MinValue3D}}, \code{\link{Range3D}},
   \code{\link{ModuleSum3D}}, \code{\link{StandardError3D}},
   \code{\link{ModuleStandardDeviation3D}}, \code{\link{ModuleVariance3D}}, \code{\link{ModulePopulationVariance3D}},
   \code{\link{ModulePopulationStandardDeviation3D}}.
}
\examples{
   FileName<-system.file("data/XYZcoor.txt", package="VecStatGraphs3D")
   dat<-LoadData3D(FileName, Type=1)
   modules<-dat[,1]
   ArithmeticMean3D(modules)
}
% Add one or more standard keywords, see file 'KEYWORDS' in the
% R documentation directory.
\keyword{module}