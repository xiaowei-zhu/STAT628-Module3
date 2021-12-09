d1<-read.csv("attributes.csv")

library(tidyverse)
d2<-rename(d1,StreetParking=BusinessParking,PriceRange2_2=RestaurantsPriceRange2,NoiseLevelAverage=NoiseLevel,WiFiFree=WiFi,FullBar=Alcohol,MusicFalse=Music,AmbienceClassy=Ambience)
att<-glm(stars~.,data=d2)
summary(att)

