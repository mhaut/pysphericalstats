\name{RayleighTest3D}
\alias{RayleighTest3D}
%- Also NEED an '\alias' for EACH other topic documented here.
\title{Rayleigh Test. Formal test of uniformity.}
\description{
   This function performs the Rayleigh test of uniformity.
}
\usage{
RayleighTest3D(coord, Alpha = 0.05)
}
%- maybe also 'usage' for other objects documented here.
\arguments{
  \item{coord}{Matrix containing the values of the coordinates}
  \item{Alpha}{Value used to obtain the Rayleigh Value of the Chi2 Table. The values can be 0.05, 0.025, 0.01, 0.005, 0.001, 0.0005.
			The default is 0.05.}
}
\details{
   This test detects a single modal direction in a sample of angles when the mean angles is unspecified. 
   The hypothesis of uniformity is rejected if the mean module is very large. This test assumes that a larger 
   mean module implies a more concentration around the mean, and therefore less probability that the data is 
   uniformly distributed.
   
   One way to get a set of coordinates  X, Y and Z of the origin position and end position 
   (coordinates X, Y and Z of the vector) or of the colatitude and longitude, it is using the \code{\link{LoadData3D}} function.
}
\value{
   Returns the probability value, and indicates whether or not to accept the hypothesis of uniformity.
}
\references{
  Fisher N.I. , Lewis T. , Embleton, B.J.J. (1987) Statistical analysis of spherical data. Cambridge. Cambridge University Press.

  Website \url{http://gim.unex.es/VecStatGraphs3D/}
}
\author{Ruiz-Cuetos, J.C., \email{bilba_t@hotmail.com}, Polo, M.E., \email{mepolo@unex.es}, Rodriguez, P.G. \email{pablogr@unex.es}}

%% ~Make other sections like Warning with \section{Warning }{....} ~

\seealso{
   \code{\link{AllAngleStatistics}}, \code{\link{AllModuleStatistics3D}}.
}
\examples{
   FileName<-system.file("data/XYZcoor.txt", package="VecStatGraphs3D")
   dat<-LoadData3D(FileName, Type=3)
   coordinates<-dat[,4:6]
   RayleighTest3D(coordinates, Alpha = 0.05)
}
% Add one or more standard keywords, see file 'KEYWORDS' in the
% R documentation directory.
\keyword{test}