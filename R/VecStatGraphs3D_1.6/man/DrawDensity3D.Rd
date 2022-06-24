\name{DrawDensity3D}
\alias{DrawDensity3D}
%- Also NEED an '\alias' for EACH other topic documented here.
\title{Graphic representation of a point Density Map.}
\description{
   The density map was built as follows: a) vectors are moved to a common origin without changing its angle and module, 
   b) end position perform a point cloud of varying density that depends on the accumulation of vectors with similar properties, 
   c) end positions are used for to calculate the density map as a surface with values depending on the end-position 
   accumulation per area unit. Areas where there is a greater number of points (end position of the vectors) 
   will have a deeper color (red), while the areas a lesser density will have a less intense color (white).
}
\usage{
DrawDensity3D(vectors, Div = 40, Layers = 3, DrawAxes = FALSE)
}
%- maybe also 'usage' for other objects documented here.
\arguments{
  \item{vectors}{Matrix containing the values of the coordinates}
  \item{Div}{Integer value that indicates the number of divisions that will have the density map. The default value is 40}
  \item{Layers}{Integer value that indicates the number of layers that will have the density map. The default value is 3}
  \item{DrawAxes}{Logical value, if DrawAxes=TRUE draw axes, if DrawAxes=FALSE draw not axes. The default value is FALSE}
}
\details{
   Kernel descriptors are used to create the density map. To perform these calculations the MASS package is required.
   
   The parameter Div is very important because a very large value will cause the creation of the slow density map, 
   and a very small value would create a ineffective density map. 
   
   One way to get a set of coordinates  X, Y and Z of the origin position and end position 
   (coordinates X, Y and Z of the vector) or of the colatitude and longitude, it is using the \code{\link{LoadData3D}} function.
   
   
   Typical usages are \preformatted{
    DrawDensity3D(vectors, ...)
	DrawDensity3D(vectors, Div = 60, ...)
	DrawDensity3D(vectors, Layers = 4, DrawAxes = TRUE, ...)
    ......
	}
}
\value{
  This function returns no value, creates a 3D Graph that represents a density map of the input values.
}
\references{
  Website \url{http://gim.unex.es/VecStatGraphs2D/}
}
\author{Ruiz-Cuetos, J.C., \email{bilba_t@hotmail.com}, Felicisimo, A.M., \email{amfeli@unex.es}, 
Cuartero, A., \email{acuartero@unex.es}, Polo, M.E., \email{mepolo@unex.es}, 
Rodriguez, P.G. \email{pablogr@unex.es}}

%% ~Make other sections like Warning with \section{Warning }{....} ~

\seealso{
   \code{\link{DrawModuleAndAngleDistribution3D}}.
}
\examples{
   FileName<-system.file("data/XYZcoor.txt", package="VecStatGraphs3D")
   dat<-LoadData3D(FileName, Type=1)
   coordinates<-dat[,4:6]
   DrawDensity3D(coordinates, Layers=3, Div=50)
}
% Add one or more standard keywords, see file 'KEYWORDS' in the
% R documentation directory.
\keyword{graphics}