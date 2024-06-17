import scipy.stats as stats

embeds = ['fasttext', 'glove', 'word2vec' ]
clusters = ['birch', 'gmm', 'kmeans', 'spectral']
metrics = ["Silhouette Score", "ARI Score", "Dunn Index", "DB Score"]

d = {}

for embed in embeds:
    for cluster in clusters:
        file = open('data\\'+embed+'_'+cluster+'_kfold_clustering_metrics.csv', 'r')
        fileData = file.read()
        fileData = fileData.split("\n")
        d[embed+'+'+cluster] = {}
        for i, line in enumerate(fileData):
            fileData[i] = line.split(",")
        for i, metric in enumerate(metrics):
            d[embed+'+'+cluster][metric] = []
            for j in range(1,6):
                d[embed+'+'+cluster][metric].append(float(fileData[j][i+1]))

file = open("stats.csv", "w") 
file.writelines("combination,pvalue,statistic \n")
for embed in embeds:
    for cluster in clusters:
        for cluster2 in clusters:
            if cluster != cluster2:
                for metric in metrics:
                    st = stats.wilcoxon(d[embed+'+'+cluster][metric], d[embed+'+'+cluster2][metric])
                    file.writelines(embed+ " " +cluster+"+"+cluster2+" "+metric+","+ str(st.pvalue)+","+ str(st.statistic)+ "\n")