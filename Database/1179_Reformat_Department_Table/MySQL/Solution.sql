SELECT id,
max(Jan_Revenue) AS Jan_Revenue,
max(Feb_Revenue) AS Feb_Revenue,
max(Mar_Revenue) AS Mar_Revenue,
max(Apr_Revenue) AS Apr_Revenue,
max(May_Revenue) AS May_Revenue,
max(Jun_Revenue) AS Jun_Revenue,
max(Jul_Revenue) AS Jul_Revenue,
max(Aug_Revenue) AS Aug_Revenue,
max(Sep_Revenue) AS Sep_Revenue,
max(Oct_Revenue) AS Oct_Revenue,
max(Nov_Revenue) AS Nov_Revenue,
max(Dec_Revenue) AS Dec_Revenue
FROM (SELECT id,
IF(month = 'Jan', revenue, NULL) AS Jan_Revenue,
IF(month = 'Feb', revenue, NULL) AS Feb_Revenue,
IF(month = 'Mar', revenue, NULL) AS Mar_Revenue,
IF(month = 'Apr', revenue, NULL) AS Apr_Revenue,
IF(month = 'May', revenue, NULL) AS May_Revenue,
IF(month = 'Jun', revenue, NULL) AS Jun_Revenue,
IF(month = 'Jul', revenue, NULL) AS Jul_Revenue,
IF(month = 'Aug', revenue, NULL) AS Aug_Revenue,
IF(month = 'Sep', revenue, NULL) AS Sep_Revenue,
IF(month = 'Oct', revenue, NULL) AS Oct_Revenue,
IF(month = 'Nov', revenue, NULL) AS Nov_Revenue,
IF(month = 'Dec', revenue, NULL) AS Dec_Revenue
FROM Department) AS a GROUP BY id;
