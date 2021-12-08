
library(shiny)
library(RColorBrewer)
library(ggplot2)
library(grDevices)
library(fmsb)

review<-read.csv("./data/review.csv")
rating<-read.csv("./data/rating.csv")
aspect<-read.csv("./data/aspect.csv")

server <- function(input, output) {

     
    name=eventReactive(input$go,input$name)
    state=eventReactive(input$go,input$state)
    postal_code=eventReactive(input$go,input$postal_code)
    
    exist=renderText({
        sum(review$name==name() & review$state==state() & review$postal_code==postal_code())
    })
    
    output$error <- renderText({
        if (exist()==0){
            if (name() %in% review$name[review$state==state()]){
                postal_refer = names(table(review$postal_code[review$name==name() & review$state==state()]))
                return(paste0('<font size="6"><span style=\"color:',brewer.pal(9,"Blues")[8],'\"><b>Opps!</b></span></font><br>
                      <font size="3"><b>Seems you have inputed a wrong postal code for ',name(),' in ',state(),'. <br> You can try<br></b></font>',
                              '<font size="4"><b><span style=\"color:',brewer.pal(8,"Spectral")[8],'\">',paste(postal_refer,collapse="<br>"),'</span></b></font>'))
            }
            else {
                shop_refer = names(sort(table(review$name[review$state==state()]),decreasing =T))[1:25]
                return(paste0('<font size="6"><span style=\"color:',brewer.pal(9,"Blues")[8],'\"><b>Opps!</b></span></font><br>
                      <font size="3"><b>Seems the bar name you input is not in ',state(),'.<br>You can try<br></b></font>',
                              '<font size="4"><b><span style=\"color:',brewer.pal(8,"Spectral")[8],'\">',paste(shop_refer,collapse="<br>"),'</span></b></font>'))
            }
        }
    })
    
    #Rating
    output$general <- renderText({
        if (exist()>0){
            ave=rating$stars[rating$name==name() & rating$state==state() & rating$postal_code==postal_code()]
            return(paste0('<font size="4"><b>The rating of your cocktail bar is: <br><b></font>',
                          '<font size="10"><b><span style=\"color:',brewer.pal(8,"Spectral")[8],'\">',paste(ave),'</span><b></font>'))
        }
    })
    
    output$plottext <-renderText({
        if (exist()>0){
            return(paste0('<font size="4"><b>The distribution of reviews rating: <br><b></font>'))
        }
    })
    
    output$rate <- renderPlot({
        if (exist()>0){
            ddd=subset(rating,rating$name==name() & rating$state==state() & rating$postal_code==postal_code())
            xxx=rev(c(t(ddd[-c(1:15)])))
            names(xxx)=c("1 star","2 stars","3 stars","4 stars","5 stars")
            par(bg=NA)
            p1=barplot(xxx,col = brewer.pal(9,"Blues")[3:7], border = NA)
            return(p1)
        }
    },width=600,height=400)
    
    
    
    #radar charts
    output$radar <- renderPlot({
      if (exist()>0){
        dat1 <- data.frame(
          service_rating = c(5, 0),
          food_rating = c(5, 0),
          drink_rating = c(5, 0),
          place_rating = c(5, 0),
          overall_rating = c(5, 0))
        ddd2=subset(aspect,aspect$name==name() & aspect$state==state() & aspect$postal_code==postal_code())
        dat2<-ddd2[-(1:34)]
        dat3=dat2[-c(6:10)]
        dat4=data.frame(service_rating=3.82159,food_rating=3.853123,drink_rating=3.7145,place_rating=3.90001,overall_rating=	3.924666)
        dat<-rbind(dat1,dat4,dat3)
        par(bg=NA)
        p2=radarchart(dat,axistype=1,seg=4,pcol=c(brewer.pal(9,"Blues")[5],brewer.pal(9,"Blues")[8]),cglcol='#000000',plwd=c(2,3),plty=c(2,1),cglwd=1,cglty=1,centerzero=TRUE,caxislabels = c('1','2','3','4','5'))
        return(p2)
      }
    },width=500,height=500)
    
    
    
    
    
    
    
    
    
    #suggestion
    output$service <- renderText({
        if (exist()>0){
            ser = review$service[review$name==name() & review$state==state() & review$postal_code==postal_code()]
            if (ser == "service"){
                return(paste0('<font size="4"><span style=\"color:',brewer.pal(9,"Blues")[8],'\"><b>Customers are not satisfied with the service of your bar, you may improve the rating in this aspect.<br></b></font>'))
            }
        }
    })
    
    output$wait <- renderText({
        if (exist()>0){
            wai = review$wait[review$name==name() & review$state==state() & review$postal_code==postal_code()]
            if (wai == "wait"){
                return(paste0('<font size="4"><span style=\"color:',brewer.pal(9,"Blues")[8],'\"><b>The waiting time in the bar is too long. Find ways to improve efficiency.<br></b></font>'))
            }
        }
    })
    
    output$table <- renderText({
        if (exist()>0){
            tab = review$table[review$name==name() & review$state==state() & review$postal_code==postal_code()]
            if (tab == "table"){
                return(paste0('<font size="4"><span style=\"color:',brewer.pal(9,"Blues")[8],'\"><b>There are not enough tables.<br></b></font>'))
            }
        }
    })
    
    output$staff <- renderText({
        if (exist()>0){
            sta = review$staff[review$name==name() & review$state==state() & review$postal_code==postal_code()]
            if (sta == "staff"){
                return(paste0('<font size="4"><span style=\"color:',brewer.pal(9,"Blues")[8],'\"><b>Train the waitresses and managers to be politer and service more carefully.<br></b></font>'))
            }
        }
    })
    
    output$bartender <- renderText({
        if (exist()>0){
            bar = review$bartender[review$name==name() & review$state==state() & review$postal_code==postal_code()]
            if (bar == "bartender"){
                return(paste0('<font size="4"><span style=\"color:',brewer.pal(9,"Blues")[8],'\"><b>Hire more professional bartenders who are good at making cocktails and comunicating with customers .<br></b></font>'))
            }
        }
    })
    
    output$hour <- renderText({
        if (exist()>0){
            hou = review$hour[review$name==name() & review$state==state() & review$postal_code==postal_code()]
            if (hou == "hour"){
                return(paste0('<font size="4"><span style=\"color:',brewer.pal(9,"Blues")[8],'\"><b>Adjust business hours appropriately.<br></b></font>'))
            }
        }
    })
 
    output$food <- renderText({
        if (exist()>0){
            foo = review$food[review$name==name() & review$state==state() & review$postal_code==postal_code()]
            if (foo == "food"){
                return(paste0('<font size="4"><span style=\"color:',brewer.pal(9,"Blues")[8],'\"><b>Improve the taste of chicken, and increase the variety of burgers.<br></b></font>'))
            }
        }
    })
    
    output$cheap <- renderText({
        if (exist()>0){
            che = review$cheap[review$name==name() & review$state==state() & review$postal_code==postal_code()]
            if (che == "cheap"){
                return(paste0('<font size="4"><span style=\"color:',brewer.pal(9,"Blues")[8],'\"><b>The prices of some drinks and foods are too low, adjust the prices on the menu..<br></b></font>'))
            }
        }
    })
    
    output$expensive <- renderText({
        if (exist()>0){
            exp = review$expensive[review$name==name() & review$state==state() & review$postal_code==postal_code()]
            if (exp == "expensive"){
                return(paste0('<font size="4"><span style=\"color:',brewer.pal(9,"Blues")[8],'\"><b>The prices of some drinks and foods are too high, adjust the prices on the menu..<br></b></font>'))
            }
        }
    })
    
    output$beer <- renderText({
        if (exist()>0){
            bee = review$beer[review$name==name() & review$state==state() & review$postal_code==postal_code()]
            if (bee == "beer"){
                return(paste0('<font size="4"><span style=\"color:',brewer.pal(9,"Blues")[8],'\"><b>The quality of beer needs to be improved.<br></b></font>'))
            }
        }
    })
    
    output$cocktail <- renderText({
        if (exist()>0){
            coc = review$cocktail[review$name==name() & review$state==state() & review$postal_code==postal_code()]
            if (coc == "cocktail"){
                return(paste0('<font size="4"><span style=\"color:',brewer.pal(9,"Blues")[8],'\"><b>The quality of cocktail needs to be improved.<br></b></font>'))
            }
        }
    })
    
    output$place <- renderText({
        if (exist()>0){
            pla = review$place[review$name==name() & review$state==state() & review$postal_code==postal_code()]
            if (pla == "place"){
                return(paste0('<font size="4"><span style=\"color:',brewer.pal(9,"Blues")[8],'\"><b>Adjust the atmosphere according to the preferences of target customers.<br></b></font>'))
            }
        }
    })
    
    output$music <- renderText({
        if (exist()>0){
            mus = review$music[review$name==name() & review$state==state() & review$postal_code==postal_code()]
            if (mus == "music"){
                return(paste0('<font size="4"><span style=\"color:',brewer.pal(9,"Blues")[8],'\"><b>Research customers\' preferences for background music and make a more popular playlist.<br></b></font>'))
            }
        }
    })
    
    output$quiet <- renderText({
        if (exist()>0){
            qui = review$quiet[review$name==name() & review$state==state() & review$postal_code==postal_code()]
            if (qui == "quiet"){
                return(paste0('<font size="4"><span style=\"color:',brewer.pal(9,"Blues")[8],'\"><b>Some of your costomers may prefer quiet environment.<br></b></font>'))
            }
        }
    })
    
    
    
    #Contact information
    output$ContactInformation <- renderUI({
        HTML('<br>
             If you have any questions, please contact: <br>
             
             Yijin Guan:  yguan37@wisc.edu<br>
             
             Xiaowei Zhu:  xzhu339@wisc.edu<br>
             
             Tongyue Jia:  tjia22@wisc.edu
             
             ')
    })

}
