\name{DrawModuleAndAngleDistribution3D}
\alias{DrawModuleAndAngleDistribution3D}
%- Also NEED an '\alias' for EACH other topic documented here.
\title{Graphic representation of Module and Angle Distribution.}
\description{
   This function creates a 3D graph, that allows us to check the angular and linear magnitudes simultaneously.
}
\usage{
DrawModuleAndAngleDistribution3D(dat, Long=FALSE, hW=0.5, hL=0.3, plane, BarSlider=FALSE)
}
%- maybe also 'usage' for other objects documented here.
\arguments{
  \item{dat}{Matrix containing the values of the \code{\link{LoadData3D}}}
  \item{Long}{Logical value, if Long = TRUE we can select an area of points for to obtain its length.The default value is Long = FALSE.}
  \item{hW}{Integer value, representing the width of the head of the arrows. The default value is 0.5}
  \item{hL}{Integer value, representing the lenght of the head of the arrows. The default value is 0.3}
  \item{plane}{Possible values are XY, XZ and YZ represents the plane where they will draw the orientacion the heads of the arrows.}
  \item{BarSlider}{Logical value, if BarSlider = TRUE we may change the size of the heads of the arrows through a slider.The default value is BarSlider = FALSE.}
}
\details{
   The 3D graph draws an arrow for each of the samples. The lines will have origin in (0,0) and end at coordinates (X, Y, Z).
   
   Typical usages are \preformatted{
    DrawModuleAndAngleDistribution3D(dat, Long = FALSE, plane = "XY", ...)
    DrawModuleAndAngleDistribution3D(dat, hW = 0.6, hL = 0.4, ...)
	  DrawModuleAndAngleDistribution3D(dat, Long = FALSE, plane = "XY", BarSlider = TRUE, ...)
   }
}
\value{
  This function returns no value, creates a 3D graph that represents module and angle distribution
}
\references{
  Website \url{http://gim.unex.es/VecStatGraphs3D/}
}
\author{Ruiz-Cuetos, J.C., \email{bilba_t@hotmail.com}, Polo, M.E., \email{mepolo@unex.es}, Rodriguez, P.G. \email{pablogr@unex.es}}


%% ~Make other sections like Warning with \section{Warning }{....} ~

\seealso{
   \code{\link{DrawDensity3D}}.
}
\examples{
   FileName<-system.file("data/XYZcoor.txt", package="VecStatGraphs3D")
   dat<-LoadData3D(FileName, Type=1)
   DrawModuleAndAngleDistribution3D(dat, plane="XY");
}
% Add one or more standard keywords, see file 'KEYWORDS' in the
% R documentation directory.
\keyword{graphics}