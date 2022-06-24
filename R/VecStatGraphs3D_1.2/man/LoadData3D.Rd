\name{LoadData3D}
\alias{LoadData3D}
%- Also NEED an '\alias' for EACH other topic documented here.
\title{Data loading and conversion of polar coordinates, rectangular coordinates, and measured and real coordinates.}
\description{
  This function reads data from a txt file containing data of coordinates. Data can be read as polar coordinates, 
  rectangular coordinates or measured and real coordinates. This functions returns a matrix with all possible data 
  conversions.
}
\usage{
LoadData3D(FileName, Type = 1)
}
%- maybe also 'usage' for other objects documented here.
\arguments{
  \item{FileName}{File name to load data}
  \item{Type}{Integer value that indicates the type of data contained in the file. Type 1 = Rectangular, Type 2= Polar, Type 3 = Measured and Real}
}
\details{
   Input files must be in a certain format for the data type. By default the type is Rectangular.
   
   The rectangular type contains three columns, the first column is the X coordinate, the second column is 
   the Y coordinate and the third column is the Z coordinates, and each row corresponds to one of the data. The X coordinate, Y coordinate 
   and Z coordinate are obtained from the difference of the coordinates measured coordinates with respect to the real coordinates.
   
   The polar type contains two or three columns. If it contains two columns, the first column represents the colatitude and 
   the second column represents the length, in this case the module by default is equal to 1. If it contains three columns, the first column 
   represents the module, the second column represents the colatitude and the third column represents the length. Each row corresponds to one 
   of the data.
   
   The measured and real type contains six columns, the first three columns represent the X, Y and Z coordinates 
   of the measured data and the last three columns represents the coordinates of the actual data, and each row corresponds to one of the data.
   
   
   Typical usages are \preformatted{
    LoadData3D(FileName, \dots)
    LoadData3D(FileName, Type=2)
    ......
   }
}
\value{
   The function returns a nx13 matrix size , where n is the number of data. The column 1 represents the module,the  column 2 represents the colatitude, 
   the column 3 represents the length, the column 4 represents the X coordinate, the column 5 represents the Y coordinate,
   the column 6 represents the Z coordinate, the column 7 represents the type of input data, the column 8, 9 and 10 represent the X, Y and Z coordinates of the 
   measured data, the column 11, 12 and 13 represent the X, Y and Z coordinates of the real data.
   
   The columns 8, 9, 10, 11, 12 and 13 will only have value if the input data are of type 3 (measured and real).
}
\references{
   Website \url{http://gim.unex.es/VecStatGraphs3D/} 
}
\author{Ruiz-Cuetos, J.C., \email{bilba_t@hotmail.com}, Polo, M.E., \email{mepolo@unex.es}, Rodriguez, P.G. \email{pablogr@unex.es}}


%% ~Make other sections like Warning with \section{Warning }{....} ~

\seealso{
   \code{\link{DrawDensity3D}}, \code{\link{DrawModuleAndAngleDistribution3D}},
   \code{\link{AllAngleStatistics}}, \code{\link{AllModuleStatistics3D}}, 
   \code{\link{RayleighTest3D}}.
}
\examples{
   FileName<-system.file("data/XYZcoor.txt", package="VecStatGraphs3D")
   LoadData3D(FileName, Type=3)
}
% Add one or more standard keywords, see file 'KEYWORDS' in the
% R documentation directory.
\keyword{file}