# coding: utf-8
import numpy as np
import pandas as pd
from sklearn import cluster
from sklearn.metrics import silhouette_samples, silhouette_score
import matplotlib.pyplot as plt
import matplotlib.cm as cm
urlx = 'C://Users//liuyang//Desktop//France//TrafficAccidentsInFrance//MachineLearing//caract.csv'
url1 = 'C://Users//liuyang//Desktop//France//TrafficAccidentsInFrance//MachineLearing//caracteristics.csv'
url = 'C://Users//liuyang//Desktop//France//TrafficAccidentsInFrance//MachineLearing//target.csv'
urlReal = 'C://Users//liuyang//Desktop//France//TrafficAccidentsInFrance//MachineLearing//targetReal.csv'
urlT = 'C://Users//liuyang//Desktop//France//TrafficAccidentsInFrance//MachineLearing//targetTest.csv'
url11 = 'C://Users//liuyang//Desktop//France//TrafficAccidentsInFrance//MachineLearing//caracteristicsTest.csv'
X = pd.read_csv(urlx,encoding="LATIN_1",low_memory=False)#iso8859_15
Y = pd.read_csv(url,encoding="LATIN_1",low_memory=False)#iso8859_15
XT = pd.read_csv(url11,encoding="LATIN_1",low_memory=False)#iso8859_15
X_train=X[['lum', 'int', 'atm','col', 'lat', 'long', 'catr', 'circ', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1', 'killed']]

range_n_clusters = [2,3,4,5,6,7]

for n_clusters in range_n_clusters:
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_size_inches(18, 7)
    ax1.set_xlim([-0.1, 1])
    ax1.set_ylim([0, len(X_train) + (n_clusters + 1) * 10])


    
    clusterer = cluster.KMeans(n_clusters=n_clusters, random_state=10)
    cluster_labels = clusterer.fit_predict(X_train)


    silhouette_avg = silhouette_score(X_train, cluster_labels)
    print("For n_clusters =", n_clusters,
          "The average silhouette_score is :", silhouette_avg)

    sample_silhouette_values = silhouette_samples(X_train, cluster_labels)

    y_lower = 10

    for i in range(n_clusters):

        print(i)
        ith_cluster_silhouette_values = \
            sample_silhouette_values[cluster_labels == i]

        ith_cluster_silhouette_values.sort()

        size_cluster_i = ith_cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_i

        color = cm.nipy_spectral(float(i) / n_clusters)
        ax1.fill_betweenx(np.arange(y_lower, y_upper),
                          0, ith_cluster_silhouette_values,
                          facecolor=color, edgecolor=color, alpha=0.7)

        # Label the silhouette plots with their cluster numbers at the middle
        ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

        # Compute the new y_lower for next plot
        y_lower = y_upper + 10  # 10 for the 0 samples

    ax1.set_title("The silhouette plot for the various clusters.")
    ax1.set_xlabel("The silhouette coefficient values")
    ax1.set_ylabel("Cluster label")

    # The vertical line for average silhouette score of all the values
    ax1.axvline(x=silhouette_avg, color="red", linestyle="--")

    ax1.set_yticks([])  # Clear the yaxis labels / ticks
    ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

    # 2nd Plot showing the actual clusters formed
    colors = cm.nipy_spectral(cluster_labels.astype(float) / n_clusters)
    ax2.scatter((X_train.values)[:, 0], (X_train.values)[:, 1], marker='.', s=30, lw=0, alpha=0.7,
                c=colors, edgecolor='k')

    # Labeling the clusters
    centers = clusterer.cluster_centers_
    # Draw white circles at cluster centers
    ax2.scatter(centers[:, 0], centers[:, 1], marker='o',
                c="white", alpha=1, s=200, edgecolor='k')

    for i, c in enumerate(centers):
        ax2.scatter(c[0], c[1], marker='$%d$' % i, alpha=1,
                    s=50, edgecolor='k')

    ax2.set_title("The visualization of the clustered data.")
    ax2.set_xlabel("Feature space for the 1st feature")
    ax2.set_ylabel("Feature space for the 2nd feature")

    plt.suptitle(("Silhouette analysis for KMeans clustering on sample data "
                  "with n_clusters = %d" % n_clusters),
                 fontsize=14, fontweight='bold')

plt.show()