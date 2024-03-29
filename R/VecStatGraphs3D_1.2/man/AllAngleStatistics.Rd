\name{AllAngleStatistics}
\alias{AllAngleStatistics}
%- Also NEED an '\alias' for EACH other topic documented here.
\title{Calculation of All Statistics of the Angle.}
\description{
   This function calculates several SPHERICAL data statistics from a set of input coordinates.
}
\usage{
AllAngleStatistics(coord)
}
%- maybe also 'usage' for other objects documented here.
\arguments{
  \item{coord}{Matrix containing the values of the coordinates}
}
\details{
   One way to get a set of coordinates  X, Y and Z of the origin position and end position 
   (coordinates X, Y and Z of the vector) or of the colatitude and longitude, it is using the \code{\link{LoadData3D}} function.
   
   The statistics calculated are: \code{Spherical Standar Error, Mean Module, Concentration Parameter, Mean Direction.}
}
\value{
  The value All Angle Statistics of all input X, Y and Z coordinates.
}
\references{
  Fisher N.I. , Lewis T. , Embleton, B.J.J. (1987) Statistical analysis of spherical data. Cambridge. Cambridge University Press.

  Website \url{http://gim.unex.es/VecStatGraphs3D/}
}
\author{Ruiz-Cuetos, J.C., \email{bilba_t@hotmail.com}, Polo, M.E., \email{mepolo@unex.es}, Rodriguez, P.G. \email{pablogr@unex.es}}

\seealso{
   \code{\link{MeanModule3D}},\code{\link{MeanDirection3D}},\code{\link{SphericalStandardError3D}},
   \code{\link{ConcentrationParameter3D}}.
}
\examples{
   FileName<-system.file("data/XYZcoor.txt", package="VecStatGraphs3D")
   dat<-LoadData3D(FileName, Type=3)
   coordinates<-dat[,4:6]
   AllAngleStatistics(coordinates)
}
% Add one or more standard keywords, see file 'KEYWORDS' in the
% R documentation directory.
\keyword{angle}
