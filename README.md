# gun-violence-news-data-analysis



## Lite version

## Abstract

In this study, we develop a cluster model to cluster news text corps’ topics and use them to pull out the noise data from our violence news text test dataset. Also, we trained a hybrid neural network to detect weapons images. Experiments show that our approach can achieve eﬃcient and accurate results for topic clusters and image classification. In the weapon image detection task, our approach achieved an 83% accuracy in the testing dataset. Additionally, our project not only can be used in database cleaning but also appropriate for a security audit.

## About the Data

There are 2 datasets we used in this project, the first two test datasets are collected with a web crawler from a variety of news press websites, which is designed for the US CDC’s National Center for Injury Prevention and Control, Division of Violence Prevention. They request this program and use it to collect the news data, and they believe violent cases can then be analyzed to find media narratives and assist in the development of new narratives for youth violence and prevention.

1. Violence news text test dataset: include news reports for violence cases, the data collected by a python web crawler from many new press webpages, and the data range from September to November 2020. This dataset is not cleaned, which also includes webpage copyright text, firewall return messages, etc.
2. Weapons images test dataset: include about 606 images belong to 2 class: knife and pistol, which is collected from the news publisher web pages, and labeled manually.

## Results

### News topic clustering


$$
\begin{array}{|c|c|}
\hline \text { Predict label: } 0 & 4943 \\
\hline \text { Predict label: } 1 & 452 \\
\hline \text { Predict label:2 } & 145 \\
\hline
\end{array}
$$
![](https://cdn.jsdelivr.net/gh/Alex-NKG/Image_hosting/dm_img/20201209110049.png)

According to the result, we found most of the data are been predict to class 0, based on the label in the training dataset, we found most of the news texts are predicted to “talk. politics. guns” topic, which is satisfied with our acknowledge. We also pull out some rows which are not predicted as cluster 0: Figure 11 Testing dataset samples

![image-20201209110211960](https://cdn.jsdelivr.net/gh/Alex-NKG/Image_hosting/dm_img/20201209110211.png)

Which also proved the UMAP & K-means can help with the news text cleaning work based on its topic.



### Weapon image detection

We choose the CNN and LSTM network as our image classifiers. The parameters for each layer are list as below:
$$
\begin{array}{|l|l|l|l|}
\hline \text { Accuracy } & \text { f1 } & \text { precision } & \text { recall } \\
\hline 0.8333 & 0.8337 & 0.8337 & 0.8337 \\
\hline
\end{array}
$$

## Discussion

In the news text topic cluster experiment, we test 4 dimensions reduce methods, we compressed the matrix from 5500 columns to 2 columns, from the plot we found the SVD and autoencoder’s clusters are close to each other and their boundary is linear. The SVD is commonly used in text LDA task, but is poor performance in this experiment, we believe the main reason is that the SVD is a linear dimensionality reduction method, and UMAP is very effective for visualizing clusters data points and their relative proximities: which can keep the structure of the data in a very low dimension.

In the weapon image detect experiment, we first use a CNN network to classifier the image, the accuracy result is around 79%. After we are adding an LSTM network after the CNN, the accuracy is 83%