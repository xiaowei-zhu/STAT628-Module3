
library(shiny)
library(ggplot2)
library(shinydashboard)

# Define UI for application that draws a histogram
shinyUI(dashboardPage(

    # Application title
    dashboardHeader(title="Cocktail Bar Business"),

    # Use name, state, zipcode to choose a bar
    dashboardSidebar(
        width = 300,
        textInput("name",label="Name", value ="Legal Sea Foods"),
        selectInput("state",label="State" ,c('MA','TX','BC','OR','GA','FL','CO','WA'),selected='MA'),
        textInput("postal_code",label="Postal Code",value="02128"),
        actionButton("go","Submit"),
        img(src='wine.jpg',width='100%')
        ),

        # Show the information of the bar
        dashboardBody(
            tabsetPanel(
                tabPanel("Star Rating",
                         htmlOutput(outputId = "error"),
                         htmlOutput(outputId = "general"),
                         br(),
                         htmlOutput(outputId = "plottext"),
                         plotOutput("rate"),width="100%"),
                tabPanel("Analysis",
                         fluidRow(
                             column(width=6,
                                    h3("This is the rating of each aspect:"),
                                    plotOutput("radar")
                             ),
                             column(width=6,
                                    h3("Specific Suggestions:"),
                                    htmlOutput(outputId = "service"),
                                    htmlOutput(outputId = "wait"),
                                    htmlOutput(outputId = "table"),
                                    htmlOutput(outputId = "staff"),
                                    htmlOutput(outputId = "bartender"),
                                    htmlOutput(outputId = "hour"),
                                    htmlOutput(outputId = "food"),
                                    htmlOutput(outputId = "cheap"),
                                    htmlOutput(outputId = "expensive"),
                                    htmlOutput(outputId = "beer"),
                                    htmlOutput(outputId = "cocktail"),
                                    htmlOutput(outputId = "place"),
                                    htmlOutput(outputId = "music"),
                                    htmlOutput(outputId = "quiet")
                                    )
                         )
                )
            ),
            #Contact Information
            htmlOutput(position = "bottom","ContactInformation")
        )
    )
)
