\name{MeanModule3D}
\alias{MeanModule3D}
%- Also NEED an '\alias' for EACH other topic documented here.
\title{Calculation of the Mean Module of the angles.}
\description{
   This function calculates the Mean Module from a set of input coordinates.
}
\usage{
MeanModule3D(coord)
}
%- maybe also 'usage' for other objects documented here.
\arguments{
  \item{coord}{Matrix containing the values of the coordinates}
}
\details{
   One way to get a set of coordinates  X, Y and Z of the origin position and end position 
   (coordinates X, Y and Z of the vector) or of the colatitude and longitude, it is using the \code{\link{LoadData3D}} function.
}
\value{
   The value Mean module of all input coordinates.
}
\references{
  Fisher N.I. , Lewis T. , Embleton, B.J.J. (1987) Statistical analysis of spherical data. Cambridge. Cambridge University Press.

  Website \url{http://gim.unex.es/VecStatGraphs3D/}
}
\author{Ruiz-Cuetos, J.C., \email{bilba_t@hotmail.com}, Polo, M.E., \email{mepolo@unex.es}, Rodriguez, P.G. \email{pablogr@unex.es}}


%% ~Make other sections like Warning with \section{Warning }{....} ~

\seealso{
   \code{\link{AllAngleStatistics}}, \code{\link{MeanDirection3D}}, \code{\link{SphericalStandardError3D}}, 
   \code{\link{ConcentrationParameter3D}}.
}
\examples{
   FileName<-system.file("data/XYZcoor.txt", package="VecStatGraphs3D")
   dat<-LoadData3D(FileName, Type=3)
   coordinates<-dat[,4:6]
   MeanModule3D(coordinates)
}
% Add one or more standard keywords, see file 'KEYWORDS' in the
% R documentation directory.
\keyword{angle}
