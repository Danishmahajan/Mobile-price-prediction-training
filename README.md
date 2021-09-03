# Mobile-Price-Range-Prediction:
I created this Project in my 6 weeks training during 3rd year of B.tech.

#### Aim: In this Project,On the basis of the mobile Specification like Battery power,Pixel-height,Bluetooth, Ram etc we are predicting Price range of the mobile.
<hr>

#### The DataSet used is model was :

* In this data:
>id:ID<br>
>battery_power:Total energy a battery can store in one time measured in mAh<br>
>blue:Has bluetooth or not<br>
>clock_speed:speed at which microprocessor executes instructions<br>
>dual_sim:Has dual sim support or not<br>
>fc:Front Camera mega pixels<br>
>four_g:Has 4G or not<br>
>int_memory:Internal Memory in Gigabytes<br>
>m_dep:Mobile Depth in cm<br>
>mobile_wt:Weight of mobile phone<br>
>n_cores:Number of cores of processor<br>
>pc:Primary Camera mega pixels<br>
>px_height:Pixel Resolution Height<br>
>px_width:Pixel Resolution Width<br>
>ram:Random Access Memory in Megabytes<br>
>sc_h:Screen Height of mobile in cm<br>
>sc_w:Screen Width of mobile in cm<br>
>talk_time:longest time that a single battery charge will last when you are<br>
>three_g:Has 3G or not<br>
>touch_screen:Has touch screen or not<br>
>wifi:Has wifi or not<br>

<hr>

### USE:
* This kind of prediction will help companies estimate price of mobiles to give tough competion to other mobile manufacturer
* Also it will be usefull for Consumers to verify that they are paying best price for a mobile.
<hr>

### Applied Models:
* Linear Regression
* KNN
* Logistic Regression
* Decision tree
* Random forest
<hr>

### The Following Keysteps that are performed in my created model: 
> The DataSet used is model was :https://www.kaggle.com/c/mobile-price-prediction/data?select=train_data.csv <br>
> Exploratry Data Analysis<br>
> Data visualisation<br>
> Feature  selection<br>
> I used KNN algorithm in the model , In this I got maximum accuracy.<br>
> Created a Pickle file.<br>
<hr>

* The Final model takes the following inputs:

> Brand<br>
> Model<br>
> Battery power<br>
> Memory space<br>
> Ram<br>
> Pixel_height<br>
> Pixel-width<br>
> Condition Of Phone
<hr>
* The Project was Deployed at Heroku Platform :
 Link :https://mobile-price--range-predict2.herokuapp.com/
