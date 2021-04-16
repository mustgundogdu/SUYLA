# SUYLA
FREE  ENUMERATING IDENTIFIERS

With suyla, it is a vital tool that aims to manipulate the http headers sent to the target system using the requests module and perform  in blind injection. 
Documentation https://docs.unsafe-inline.com/inline/suyla-tool

~The use of the tool is shown in the portswigger blind injection lab as follows.

![](https://github.com/mustgundogdu/SUYLA/blob/master/screenshouts/lab1.PNG)



After running the suyla, We give the 'url' command and determine the http method. After entering the url value, we go to the editing area of the http headers taken from the server with the edit command.
The point to be noted will be to give input to the http headers specified for the http header input by manipulating the values received from the server.

![](https://github.com/mustgundogdu/SUYLA/blob/master/screenshouts/lab2.PNG)


The values entered are the 'Cookie' value as the HTTP header and the value in the image.


![](https://github.com/mustgundogdu/SUYLA/blob/master/screenshouts/lab3.PNG)


~Then we create our payload list and add and complete the ok statement.


![](https://github.com/mustgundogdu/SUYLA/blob/master/screenshouts/lab4.PNG)


For control, we add the ‘Welcome’ word in the answer and enter the increment length in the substring query and start it.


![](https://github.com/mustgundogdu/SUYLA/blob/master/screenshouts/lab5.PNG)



~And shows us the answers.


![](https://github.com/mustgundogdu/SUYLA/blob/master/screenshouts/result.PNG)



We see that it is successful when we enter the values as password.



![](https://github.com/mustgundogdu/SUYLA/blob/master/screenshouts/resultlab.PNG)



                          REQUIREMENTS

*    os
*    sys
*    colorama
*    requests
*    json
*    re




