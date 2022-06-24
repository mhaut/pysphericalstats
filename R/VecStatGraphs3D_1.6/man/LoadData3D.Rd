\name{LoadData3D}
\alias{LoadData3D}
%- Also NEED an '\alias' for EACH other topic documented here.
\title{Data loading and conversion of cartesian coordinates, incremental data, and polar coordinates.}
\description{
  This function reads data from a txt file containing data of coordinates. Data can be read as cartesian coordinates, incremental data or polar coordinates. This functions returns a matrix with all possible data conversions.
}
\usage{
LoadData3D(FileName, Type = 2)
}
%- maybe also 'usage' for other objects documented here.
\arguments{
  \item{FileName}{File name to load data}
  \item{Type}{Integer value that indicates the type of data contained in the file. Type 1 = Cartesian, Type 2= Incremental, Type 3 = Polar}
}
\details{
   Input files must be in a certain format for the data type. By default the type is incremental data (Type = 2).

   The cartesian coordinate type contains six columns, defining the coordinates of a vector. The first three columns represent the X, Y and Z coordinates of the intial data and the last three columns represents the coordinates of the final data, and each row corresponds to one of the data. If necessary, the inverse order can be used to adapt the direction to our data.
   
   The incremental data type contains three columns, the first column is the increase of X coordinate, the second column is the increase of Y coordinate and the third column is the increase of Z coordinates, and each row corresponds to one of the data. The X coordinate, Y coordinate and Z coordinate are obtained from the difference of the final node with respect to the initial node.
   
   The polar type contains two or three columns. If it contains two columns, the first column represents the colatitude and the second column represents the longitude, in this case the module by default is equal to 1. If it contains three columns, the first column represents the module, the second column represents the colatitude and the third column represents the longitude. Each row corresponds to one of the data.
   
  
   
   Typical usages are \preformatted{
    LoadData3D(FileName, \dots)
    LoadData3D(FileName, Type=2)
    ......
   }
}
\value{
   The function returns a nx13 matrix size , where n is the number of data. The column 1 represents the module, the  column 2 represents the colatitude, the column 3 represents the longitude, the column 4 represents the increase of X coordinate, the column 5 represents the increase of Y coordinate, the column 6 represents the increase of Z coordinate, the column 7 represents the type of input data, the column 8, 9 and 10 represent the X, Y and Z coordinates of the initial data, the column 11, 12 and 13 represent the X, Y and Z coordinates of the final data.
   
   The columns 8, 9, 10, 11, 12 and 13 will only have values if the input data are of Type 1 (cartesian coordinates).
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
   \code{\link{DrawDensity3D}}, \code{\link{DrawModuleAndAngleDistribution3D}},
   \code{\link{AllAngleStatistics}}, \code{\link{AllModuleStatistics3D}}, 
   \code{\link{RayleighTest3D}}.
}
\examples{
   FileName<-system.file("data/XYZcoor.txt", package="VecStatGraphs3D")
   LoadData3D(FileName, Type=1)
}
% Add one or more standard keywords, see file 'KEYWORDS' in the
% R documentation directory.
\keyword{file}