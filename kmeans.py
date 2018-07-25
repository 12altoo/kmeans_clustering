import numpy as np
import matplotlib.pyplot as plt



def cal_distance(a,b):
	return np.linalg.norm(a-b)		# calculates distance between pt a and pt b

def kmeans(dataset,K,e=0):

	nrow,ncol=dataset.shape			# extracting size of the array

	centroids=dataset[np.random.randint(0,nrow-1,size=K)]		#assigning random values to the centroids
	print("random centroids are")
	print(centroids)

	old_centroids=np.zeros(centroids.shape)						#location of old cecntroids

	belongs_to=np.zeros((nrow,1))

	norm=cal_distance(centroids,old_centroids)					# distance between old centroids and current centroids
	iteration=0		

	while norm>e:
	 	iteration+=1

	 	norm=cal_distance(centroids,old_centroids)			

	 	old_centroids=centroids

	 	""" now we'll fing distance of each centroid from each data pt
	 		and store that distance in a distabce vector"""

	 	for index_d,data in enumerate(dataset):
	 		dist_vec=np.zeros((K,1))

	 		for index_c,cent in enumerate(centroids):
	 			dist_vec[index_c]=cal_distance(cent,data)
	 			print('distance dist_vec')
	 			print(dist_vec)

	 		belongs_to[index_d,0]=np.argmin(dist_vec)			#finding index of the least distance of data pt x from centroids

	 	tmp_cent=np.zeros((K,ncol))


	 	""" now we'll find the mean of all the data pts which are close to 
	 		that particular centroid"""								

	 	for index in range(len(centroids)):
	 		close_x=[i for i in range(len(belongs_to)) if belongs_to[i]==index]	
	 		centroid = np.mean(dataset[close_x],axis=0)

	 		print("centroid {}".format(centroid))
	 		tmp_cent[index, : ]=centroid

	 		print(tmp_cent)

	 	
	 	centroids=tmp_cent
	 	print("centroids")
	 	print(centroids)
	print(iteration)
	return centroids,belongs_to


def main():
	
	dataset=np.loadtxt('data.txt')

	centroids,belongs_to=kmeans(dataset,2)

	color=['r','g']

	for index in range(dataset.shape[0]):											#plotting th egivin data
		close_x = [i for i in range(len(belongs_to)) if belongs_to[i] == index]
		for index_d in close_x:
			plt.scatter(dataset[index_d][0],dataset[index_d][1],color=color[index])        

	plt.show()



if __name__=='__main__':
	main()		