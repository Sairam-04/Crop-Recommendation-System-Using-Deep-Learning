# Crop-Recommendation-System-Using-Deep-Learning

<h3>Link to the Colab notebook</h3>
<a href="https://colab.research.google.com/drive/1IhoW464xJTPcRL2jknz-tq7rzInHHpyo?usp=sharing">Crop_Recommendation.ipynb</a>


<h2>📝 Abstract:</h2><br>
<p>
Agriculture is one of the most important sectors in India and the farmers are one of the most essential members of society. In India Agriculture plays a predominant role in the economy and employment. One of the major problems among Indian farmers is that they don't choose the right crop based on their soil requirements. Due to this farmers face many problems in the productivity of crops. This problem has been addressed through precision agriculture.
</p>
<p>
Precision agriculture is a trend now-a-days. It helps the farmers to take the decision about the farming strategy. Precision Agriculture is a strategy that uses data such as soil characteristics and climate data to suggest the crop to be grown. Emerging technologies like Artificial Intelligence and IoT can help in this task. IoT sensors captures the soil characteristics and weather data, this data can be used to build a Deep Learning model which can recommend the most suitable crops to grow on a particular farm. This can help farmers to make decisions on which crops to grow on their farm.
</p><br><br>

<h2>📝 About the project</h2><br>
<h4>The Project is about building an Artificial Neural Network model and creating the web application that recommends farmers the best crop which is suitable for their farm. This is a clasification model with 22 different classes.</h4><br>
1. N - ratio of Nitrogen content in soil<br>
2. P - ratio of Phosphorous content in soil<br>
3. K - ratio of Potassium content in soil<br>
4. temperature - temperature in degree Celsius<br>
5. humidity - relative humidity in %<br>
6. ph - ph value of the soil<br>
7. rainfall - rainfall in mm<br><br>

<h2>🗄️ About the Data:</h2><br>
<h3> Dataset used for the project:<a href='https://www.kaggle.com/atharvaingle/crop-recommendation-dataset'> Crop Recommendation Data</a><br></h3>
Dataset consists of 8 columns in which 7 columns are the characteristics of the soil and the last column is the label column which consists of crop name.<br><br>
  
<img src='https://github.com/Sairam-04/Crop-Recommendation-System-Using-Deep-Learning/blob/main/Readme%20Images/data.png'>


<h2> Requirements </h2><br>
</h3>Programming Language</h3><br>

* Python 3.6-3.8<br>

<h3>Frameworks and Libraries</h3><br>

*   Virtual environment<br>
*   Keras<br>
*   Pandas<br>
*   Tensorflow<br>
*   Matplotlib<br>
*   Numpy<br>
*   Seborn<br>
*   Scikit-Learn<br>
*   Flask<br>

<h2>⚙️ Setup</h2><br>

Installing virtal environment
  <pre>$pip install virtalenv</pre>
  
Creating Virtual environment
<pre> $virtualenv environment_name</pre>

Activate virtual environment<br>
&emsp;Windows:
&emsp;<pre> $environment_name/Scripts/activate </pre>

&emsp;Linux:
&emsp;<pre>$environment_name/bin/activate </pre>
  
After activating the virtual environment:
<pre> (environment_name) $ </pre>

Installing Numpy
<pre> (environment_name) $pip install numpy</pre>

Installing Pandas
<pre> (environment_name) $pip install pandas</pre>

Installing Matplotlib
<pre> (environment_name) $pip install matplotlib</pre>

Installing Seaborn
<pre> (environment_name) $pip install seaborn</pre>

Installing Tensorflow
<pre> (environment_name) $pip install tensorflow</pre>

Installing Flask
<pre> (environment_name) $pip install flask</pre>

Installing Scikit-learn
<pre> (environment_name) $pip install -U scikit-learn </pre>
<br><br>
<h2> Training Pipeline</h2>
<img src='https://github.com/Sairam-04/Crop-Recommendation-System-Using-Deep-Learning/blob/main/Readme%20Images/pipeline.png' >

<br><br>
<h2>Flask Web Application Demo:</h2><br>

<img src='https://github.com/Sairam-04/Crop-Recommendation-System-Using-Deep-Learning/blob/main/Readme%20Images/demo1.png'>
<br><br>
<img src='https://github.com/Sairam-04/Crop-Recommendation-System-Using-Deep-Learning/blob/main/Readme%20Images/demo2.png'>

