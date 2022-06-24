\name{MeanAngle}
\alias{MeanAngle}
%- Also NEED an '\alias' for EACH other topic documented here.
\title{Calculation of the Mean Angle of the angles.}
\description{
   This function calculates the Mean Angle of a set of input angles.
}
\usage{
MeanAngle(angles)
}
%- maybe also 'usage' for other objects documented here.
\arguments{
  \item{angles}{Matrix containing the values of the angles}
}
\details{
   One way to get a set of coordinates  X, Y and Z of the origin position and end position 
   (coordinates X, Y and Z of the vector) or of the colatitude and longitude, it is using the \code{\link{LoadData3D}} function.
}
\value{
   The Value Mean Angle of all input angles. The value is expressed in sexagesimal.
}
\references{
  Fisher N.I. , Lewis T. , Embleton, B.J.J. (1987) Statistical analysis of spherical data. Cambridge. Cambridge University Press.

   Website \url{http://gim.unex.es/VecStatGraphs3D/}
}
\author{Ruiz-Cuetos, J.C., \email{bilba_t@hotmail.com}, Polo, M.E., \email{mepolo@unex.es}, Rodriguez, P.G. \email{pablogr@unex.es}}


%% ~Make other sections like Warning with \section{Warning }{....} ~

\seealso{
   \code{\link{MeanModule3D}}, \code{\link{MeanDirection3D}}, \code{\link{SphericalStandardError3D}}, \code{\link{ConcentrationParameter3D}}.
}

% Add one or more standard keywords, see file 'KEYWORDS' in the
% R documentation directory.
\keyword{internal}
