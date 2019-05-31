# Ready RODBC for use in this script
require(RODBC)

# Create a connection to SQL Server using our 64-bit DSN
myconn <- odbcConnect("VidCast")

# Ready the SQL to send to the Server
sqlSelectStatement <-
"SELECT
  vc_VidCast.vc_VidCastID
, vc_VidCast.VidCastTitle
, DATEPART(dw, StartDateTime) as StartDayOfWeek
, DATEDIFF(n, StartDateTime, EndDateTime) as ActualDuration
, ScheduleDurationMinutes
, vc_User.vc_UserID
, vc_User.UserName
FROM vc_VidCast
JOIN vc_User ON vc_User.vc_UserID = vc_VidCast.vc_UserID
"

# Send the request to the server and store the results in a variable
sqlResult <- sqlQuery(myconn, sqlSelectStatement)

# Use +/- 3 sigma to prune outliers (Symmetrically distributed)
sqlResult <- subset(sqlResult, ActualDuration > 0)
sigma <- sd(sqlResult$ActualDuration)
mu <- mean(sqlResult$ActualDuration)
upper <- mu + (3*sigma)
lower <- mu - (3*sigma)

# Thanks, Shaun, for this handy outlier fix!
sqlResult <- subset(sqlResult, ActualDuration < upper)
sqlResult <- subset(sqlResult, ActualDuration > lower)

# Create a list of days of the week for charting later
days <- c("Sun", "Mon", "Tues", "Weds", "Thurs", "Fri", "Sat")

# Create a histogram of durations (appears in the Plots tab)
hist(sqlResult$ActualDuration,
     main="How long are the VidCasts?",
     xlab="Minutes",
     ylab="VidCasts",
     border="blue",
     col="grey",
     labels=TRUE
)

# Hard coded fix for hist(): [which(sqlResult$ActualDuration < 400)],

# Plot a bar chart of video counts by day of the week 
dayCounts <- table(sqlResult$StartDayOfWeek)

barplot(dayCounts,
        main="VidCasts by Day of Week",
        ylab="Day of Week",
        xlab="Count of VidCasts",
        names.arg = days
)

# Close all connections
odbcCloseAll()

# Fin
